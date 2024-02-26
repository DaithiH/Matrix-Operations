# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 15:43:02 2023

@author: daveh
"""

"""
Matrix operations with hard coded matrices
Doing this first to figure out how to code the operations, loops etc.
"""

def Matrix_Add(matrixA, matrixB):
    """
    Additon: adds the corresponding matrix elements.
    Matrices must be of the same dimension.

    """

    if len(matrixA[0]) != len(matrixB):
        #raise DimensionError("Matrices must be of the same dimension!")
        raise ValueError("Matrices must be of the same dimension!")

    # Initialize an empty matrix to push the addition results to #

    matrix_sum = [[0 for _ in range(len(matrixA))] for _ in range(len(matrixB[0]))]


    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            matrix_sum[i][j] = matrixA[i][j] + matrixB[i][j]


    for row in matrix_sum:
        print(row)

def Matrix_Sub(matrixA, matrixB):
    """
    Subtraction: subtracts the corresponding matrix elements.
    Matrices must be of the same dimension.

    """

    if len(matrixA[0]) != len(matrixB):
        #raise DimensionError("Matrices must be of the same dimension!")
        raise ValueError("Matrices must be of the same dimension!")

    # Initialize an empty matrix to push the addition results to #

    matrix_sub = [[0 for _ in range(len(matrixA))] for _ in range(len(matrixB[0]))]


    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            matrix_sum[i][j] = matrixA[i][j] - matrixB[i][j]


    for row in matrix_sub:
        print(row)


def Matrix_Mul(matrixA, matrixB):
    """
    Multiplication of matrices multiplys each row in matrix 1 by all columns in
    matrix 2 and sums the product values to get each column entry in the resulting
    matrix. Matrices must be of the same dimension. Number of rows matrix 1 must
    equal number of colums in matrix 2.

    """

    if len(matrixA) != len(matrixB[0]):
        #raise DimensionError("Matrices must be of the same dimension!")
        raise ValueError("The number of rows in matrix 1 must be equal to the number of columns in matrix 2!")

    # Initialize an empty matrix to push the element products to
    product_matrix = [[0 for _ in range(len(matrixA))] for _ in range(len(matrixB[0]))]

    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixB)):
                product_matrix[i][j] += matrixA[i][k] * matrixB[k][j]

    for row in product_matrix:
        print(row)

A =  [[1,2,3],
     [4,5,6],
     [7,8,9],
    ]

B = [[9,8,7],
     [6,5,4],
     [3,2,1]
    ]


A1 =  [[1,2,3],
      [4,5,6],
      [7,8,9],
      [1,0,-1]
     ]


B1 =  [[9,8,7,0],
      [6,5,4,1],
      [3,2,1,-1]
     ]


Matrix_Add(A, B)
print()
Matrix_Mul(A, B)
print()
Matrix_Mul(A1, B1)
