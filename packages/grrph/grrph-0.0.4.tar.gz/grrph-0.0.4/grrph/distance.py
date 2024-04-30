import numpy as np

import sklearn.preprocessing
from scipy.optimize import linprog

import itertools as it
from grrph.util import unique_rows


def haussdorff_distance(pdist):
    '''Compute the Haussdorff distance between sets A and B of points 
    in a metric space (M, d).

    Input: Rectangular distance matrix of shape (|A|, |B|)
    Output: $ max( max_{a \in A} min_{b \in B} d(a,b), max_{b \in B} min_{a \in A} d(a,b) )
    '''
    mina = np.min(pdist, axis=1)
    minb = np.min(pdist, axis=0)
    maxa = np.max(mina)
    maxb = np.max(minb)
    return np.max([maxa, maxb])


def metric_bases(distance_matrix, k):
    '''list all sets of k indices that result in unique representations when projecting.
    That is, if k is the metric dimension of the graph whose distance matrix we are looking
    at, the return will be the set of all metric bases of the graph.
    If k is smaller than the metric dimension, the returned set will be empty.
    '''

    bases = list()
    for idx in it.combinations(range(distance_matrix.shape[0]), k):
        projection = distance_matrix[:,idx]
        unique, _ = unique_rows(projection)
        if unique.shape[0] == distance_matrix.shape[0]:
            bases.append(idx)

    return bases


def kernel_dist(gram):
    ''' return the distance matrix corresponding to the gram matrix '''
    dg = np.diag(gram).reshape([gram.shape[0], 1])
    return np.sqrt(dg - 2 * gram + dg.T)


def generalizedMMDDistance(dist, gammas):
    '''
    Generalization of Maximum Mean Discrepancy distance presented in Definition 4 / equation (2) of
    
    Yan Sun and Jicong Fan (2024): MMD GRAPH KERNEL: EFFECTIVE METRIC LEARNING 
    FOR GRAPHS VIA MAXIMUM MEAN DISCREPANCY, ICLR.

    Not clear if we should square the kernel_dist before returning
    '''

    mmd = np.exp(-gammas[0] * dist)
    for gamma in gammas[1:]:
        mmd = np.maximum(mmd, np.exp(-gamma * dist))

    return kernel_dist(mmd)


def gromov_wasserstein(C1, C2, verbose=False):
    import ot 

    n_samples = C1.shape[0]
    if (C2.shape[0] != n_samples) or (C2.shape[1] != n_samples) or (C1.shape[1] != n_samples):
        raise ValueError(f'Incompatible shapes: {C1.shape} and {C2.shape}')

    p = ot.unif(n_samples)
    q = ot.unif(n_samples)

    gw0, log0 = ot.gromov.gromov_wasserstein(
        C1, C2, p, q, 'square_loss', verbose=verbose, log=True)

    # gw, log = ot.gromov.entropic_gromov_wasserstein(
    #     C1, C2, p, q, 'square_loss', epsilon=5e-4, log=True, verbose=True)


    # print('Gromov-Wasserstein distances: ' + str(log0['gw_dist']))
    # print('Entropic Gromov-Wasserstein distances: ' + str(log['gw_dist']))


    # pl.figure(1, (10, 5))

    # pl.subplot(1, 2, 1)
    # pl.imshow(gw0, cmap='jet')
    # pl.title('Gromov Wasserstein')

    # pl.subplot(1, 2, 2)
    # pl.imshow(gw, cmap='jet')
    # pl.title('Entropic Gromov Wasserstein')

    # pl.show()

    return log0['gw_dist']


def compute_meta_distance_matrix(f, mlist):
    ''' compute any *symmetric* distance function between anything.
    note that f(x,x) = 0 and f(x,y) = f(y,x) is assumed

    TODO should be vectorized, if possible '''
    meta_dist = np.zeros([len(mlist), len(mlist)])
    for i, a in enumerate(mlist):
        for j, b in enumerate(mlist):
            if j < i:
                meta_dist[i,j] = f(a,b)
            else:
                break
    
    return meta_dist + meta_dist.T


def alldifferences(C1, C2):
    c1 = np.vstack([C1 for _ in range(C1.shape[0])])
    c2 = np.hstack([C2 for _ in range(C1.shape[0])]).reshape([-1, C2.shape[1]])
    return c1 - c2

def sumabsdifferences(C1, C2):
    sum = np.zeros(C1.shape[1])

    for x in C2:
        sum += np.sum(np.abs(C1 - x), axis=0)
    
    return sum


def maximize_weighted_manhattan(C1, C2, w_min=0.001, compress_weights=True, normalize=True):
    '''
    C1: n1 x m matrix
    C2: n2 x m matrix
    output: 
        w vector of length m of nonnegative weights

    Linear program formulation of finding a good weight vector that 
    - minimizes weighted manhattan distance between same class objects
    - while keeping weighted manhattan distance between different class objects at least 1

    More specifically:
    given two sets of points C1, C2 of same dimension, compute weight
    vector w which minimizes 
    $ w \sum_{c \times c' \in C1} np.abs(c - c') + w \sum_{c \times c' \in C2} np.abs(c - c') $
    under constraints 
    $ w \geq w_min $
    $ w \sum_{c1 \times c2 \in C1 \times C2} np.abs(c1 - c2) \geq |C1| + |C2| $
    '''

    if C1.shape[1] != C2.shape[1]:
        raise ValueError(f'C1 and C2 must have same last dimension, but have shape {C1.shape} and {C2.shape}')
    else:
        m = C1.shape[1]
        n1 = C1.shape[0]
        n2 = C2.shape[0]

    if compress_weights:
        c11 = sumabsdifferences(C1, C1)
        c22 = sumabsdifferences(C2, C2)
        c12 = sumabsdifferences(C1, C2)

        if normalize:
            normalizer = np.sum(c12)
        else:
            normalizer = 1

        cost = c11 + c22
        design = (- c12).reshape([1, -1]) / normalizer
        bias = np.array([- n1 * n2])

        result = linprog(c=cost, A_eq=design, b_eq=bias, bounds=[w_min, None])

    else:
        c11 = sumabsdifferences(C1, C1)
        c22 = sumabsdifferences(C2, C2)
        c12 = np.abs(alldifferences(C1, C2))

        if normalize:
            normalizer = np.sum(c12)
        else:
            normalizer = 1

        cost = c11 + c22
        design = - c12 / normalizer
        bias = - np.ones(n1 * n2 ) 
        result = linprog(c=cost, A_ub=design, b_ub=bias, bounds=[w_min, None])


    if result.status == 0:
        print(result)
        return result.x
    else:
        print(result)
        raise Exception('does not compute')


def approx_Euclidean_with_weighted_manhattan(C1, C2):
    '''
    input:
        C1: n1 x m matrix
        C2: n2 x m matrix
    output: 
        w vector of length m of nonnegative weights

    Compute a weight vector w of nonnegative values that minimizes the mean squared error between 
    Euclidean distances of the given data points and weighted Manhattan distances of the given datapoints.

    For consistency with maximize_weighted_manhattan(C1, C2), we have two input sets of points, but all pairs
    of points are created and processed equally.
    '''

    c11 = np.abs(alldifferences(C1, C1))
    c22 = np.abs(alldifferences(C2, C2))
    c12 = np.abs(alldifferences(C1, C2))

    X = np.vstack([c11, c22, c12])
    y = np.hstack([np.sqrt(np.sum(c11**2, axis=1)),np.sqrt(np.sum(c22**2, axis=1)),np.sqrt(np.sum(c12**2, axis=1))])
    print(X.shape, y.shape)

    from sklearn.linear_model import LinearRegression

    model = LinearRegression(fit_intercept=False, positive=True)
    model.fit(X, y)

    return model.coef_, model.intercept_


def maximize_weighted_manhattan_nnlinreg(C1, C2, samedist=1, diffdist=10):
    '''
    C1: n1 x m matrix
    C2: n2 x m matrix
    output: 
        w vector of length m of nonnegative weights
        
    Linear regression formulation of finding a good weight vector that 
    - sets weighted manhattan distance between same class objects to samedist
    - sets weighted manhattan distance between different class objects to diffdist
    '''

    c11 = np.abs(alldifferences(C1, C1))
    c22 = np.abs(alldifferences(C2, C2))
    c12 = np.abs(alldifferences(C1, C2))

    X = np.vstack([c11, c22, c12])
    y = np.hstack([np.ones(samedist * c11.shape[0]), samedist * np.ones(c22.shape[0]), diffdist * np.ones(c12.shape[0])])
    print(X.shape, y.shape)

    from sklearn.linear_model import LinearRegression

    model = LinearRegression(fit_intercept=False, positive=True)
    model.fit(X, y)

    return model.coef_, model.intercept_


if __name__ == '__main__':
    '''test stuff'''

    d1 = np.loadtxt('testdata/distmatrix_tree_3.txt')
    d2 = np.loadtxt('testdata/distmatrix_tree_4.txt')

    print(metric_bases(d1, 2))
    print(metric_bases(d2, 2))

    a = np.array([[1,0,1],[0,1,0], [1,0,1]])

    print(a)
    print(kernel_dist(a))

    print(gromov_wasserstein(a, a, verbose=True))

    from scipy.spatial.distance import cdist
    print(haussdorff_distance(cdist(a,a)))