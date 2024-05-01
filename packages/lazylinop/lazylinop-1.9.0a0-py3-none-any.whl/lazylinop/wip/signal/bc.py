from lazylinop import LazyLinOp
import sys
from lazylinop.basicops import eye, vstack
from lazylinop.wip.signal import anti_eye

sys.setrecursionlimit(100000)


def bc(L: int, n: int = 1, bn: int = 0,
       an: int = 0, boundary: str = 'periodic'):
    """Constructs a periodic or symmetric boundary
    condition lazy linear operator.
    If you apply the operator to a 2d array, it will work
    on each column and returns a 2d array.
    Symmetric boundary condition is something like:
    xN, ..., x2, x1 | x1, x2, ..., xN | xN, ..., x2, x1
    while a periodic boundary condition is something like:
    x1, x2, ..., xN | x1, x2, ..., xN | x1, x2, ..., xN

    Args:
        L: int
        Size of the input
        n: int, optional
        Duplicate signal this number of times on both side
        bn: int, optional
        Add this number of elements before
        an: int, optional
        Add this number of elements after
        boundary: str, optional
        wrap/periodic (default) or symm/symmetric boundary condition

    Returns:
        LazyLinOp

    Raises:
        ValueError
            L must be strictly positive.
        ValueError
            n must be >= 0.
        ValueError
            an and bn must be >= 0.
        ValueError
            an must be <= L.
        ValueError
            bn must be <= L.
        ValueError
            boundary excepts 'wrap', 'periodic', 'symm' or 'symmetric'.

    Examples:
        >>> from lazylinop.wip.signal import bc
        >>> import numpy as np
        >>> x = np.array([0., 1., 2.])
        >>> Op = bc(x.shape[0], n=1, bn=0, an=0, boundary='periodic')
        >>> Op @ x
        array([0., 1., 2., 0., 1., 2., 0., 1., 2.])
        >>> Op = bc(x.shape[0], n=1, bn=0, an=0, boundary='symmetric')
        >>> Op @ x
        array([2., 1., 0., 0., 1., 2., 2., 1., 0.])
        >>> X = np.array([[0., 0.], [1., 1.], [2., 2.]])
        >>> X
        array([[0., 0.],
               [1., 1.],
               [2., 2.]])
        >>> Op @ X
        array([[2., 2.],
               [1., 1.],
               [0., 0.],
               [0., 0.],
               [1., 1.],
               [2., 2.],
               [2., 2.],
               [1., 1.],
               [0., 0.]])
    """
    if L <= 0:
        raise ValueError("L must be strictly positive.")
    if n < 0:
        raise ValueError("n must be >= 0.")
    if bn < 0 or an < 0:
        raise ValueError("an and bn must be >= 0.")
    if bn > L:
        raise ValueError("bn must be <= L.")
    if an > L:
        raise ValueError("an must be <= L.")

    if boundary == 'symmetric' or boundary == 'symm':
        if (n % 2) == 0:
            Op = eye(L, n=L, k=0)
            flip = True
        else:
            Op = anti_eye(L) @ eye(L, n=L, k=0)
            flip = False
        for i in range(1, n + 1 + n):
            if flip:
                Op = vstack((Op, anti_eye(L) @ eye(L, n=L, k=0)))
                flip = False
            else:
                Op = vstack((Op, eye(L, n=L, k=0)))
                flip = True
        if bn > 0:
            if (n % 2) == 0:
                # flip
                Op = vstack((eye(bn, n=L, k=L - bn) @ anti_eye(L), Op))
            else:
                # do not flip
                Op = vstack((eye(bn, n=L, k=L - bn), Op))
        if an > 0:
            if (n % 2) == 0:
                # flip
                Op = vstack((Op, eye(an, n=L, k=0) @ anti_eye(L)))
            else:
                # do not flip
                Op = vstack((Op, eye(an, n=L, k=0)))
        return Op
    elif boundary == 'periodic' or boundary == 'wrap':
        Op = eye(L, n=L, k=0)
        for i in range(n + n):
            Op = vstack((Op, eye(L, n=L, k=0)))
        if bn > 0:
            Op = vstack((eye(bn, n=L, k=L - bn), Op))
        if an > 0:
            Op = vstack((Op, eye(an, n=L, k=0)))
        return Op
    else:
        raise ValueError("boundary is either 'periodic' ('wrap')" +
                         " or 'symmetric' (symm).")


# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
