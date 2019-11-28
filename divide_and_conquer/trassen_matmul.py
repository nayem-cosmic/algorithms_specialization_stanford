# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 19:03:35 2019

@author: Cosmic
"""

import numpy as np

# matrix must be square and dim be even
def trassen_matmul(X, Y):
    X_shape = X.shape
    Y_shape = Y.shape
    n = X_shape[0]
    
    # base case
    if n == 1:
        return X*Y
    
    if X_shape[0] != X_shape[1] or Y_shape[0] != Y_shape[1]:
        raise Exception('Matrix must be square.')
    if X_shape[0]%2 != 0:
        raise Exception('Matrix dim must be even.')
    n_2 = int(n/2)
    
    # Split matrix in quadrants
    # X
    A = X[:n_2, :n_2]
    B = X[:n_2, n_2:]
    C = X[n_2:, :n_2]
    D = X[n_2:, n_2:]
    
    # Y
    E = Y[:n_2, :n_2]
    F = Y[:n_2, n_2:]
    G = Y[n_2:, :n_2]
    H = Y[n_2:, n_2:]
    
    # 7 products
    P1 = trassen_matmul(A, F-H)
    P2 = trassen_matmul(A+B, H)
    P3 = trassen_matmul(C+D, E)
    P4 = trassen_matmul(D, G-E)
    P5 = trassen_matmul(A+D, E+H)
    P6 = trassen_matmul(B-D, G+H)
    P7 = trassen_matmul(A-C, E+F)
    
    # Accumulate result quadrants
    C1 = np.vstack((P5+P4-P2+P6,
                       P3+P4))
    C2 = np.vstack((P1+P2,
                   P1+P5-P3-P7))
    mulMat = np.hstack((C1, C2))
    
    return mulMat

if __name__ == '__main__':
    X = np.array([[1, 2, 3, 4],
                  [4, 5, 6, 7],
                  [5, 6, 7, 8],
                  [6, 7, 8, 9]])
    Y = np.array([[2, 3, 4, 5],
                  [5, 6, 7, 8],
                  [6, 7, 8, 9],
                  [7, 8, 9, 10]])
    
    print('matmul numpy builtin:\n', X.dot(Y))
    
    print('trassen_matmul:\n', trassen_matmul(X, Y))
