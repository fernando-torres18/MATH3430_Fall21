# -*- coding: utf-8 -*-
""" 
HOMEWORK 1
Problem #1
Write an algorithm to implement scalar-vector multiplication

Q1: What do we have?
 - We have one vector stored on a computer as a list, denoted by vector_a. We also have a scalar value  denoted as scalar_a

Q2: What do we want?
 - We want to find the value of vector_a multiplied by the scalar value of scalar_a

Q3: How will we get there?
 - We can create an empty list of an arbitrary size (whatever vector_a would be in this scenario) and take the individual 
 sum of each component scalar_a amount of times.

def mult_vector(vector_a, scalar_a):

	# Set up our result as a new vector
result: w = scalar_a * vector_a

	# define our vector, our scalar, and do the multiplication
scalar_a = a
vector_a = array([n,m])
w = (some scalar value a for scalar_a) * (vector array of vector_a)

	# Get our result
return (w=)

Problem #2
Q1: What do we have?
 - We have one matrix stored in a computer, as well as one scalar value

Q2: What do we want?
 - We want the computer to return a new value for the matrix that is a new matrix as a product of the original and the scalar value

Q3: How do we get there?
 - We can store our matrix as a set of any arbitrary amount of lists, and then multiply each component of each list by our scalar value

def scal_mat_mult(matrix_a, scalar_a)

	#Set up our matrix as a collection of lists, define our scalar value
scalar_a = a
matrix_a = ([], [])
	# All values (our lists/columns) in matrix_a are multiplied by scalar_a and get replaced with the product in our resulting matrix 
matrix_a[columns][rows] = matrix_a [columns][rows] * scalar_a

	# Look at our new matrix_a, which is our result
return matrix_a

Problem #3
Write an algorithm to implement matrix addition

Q1: What do we have?
 - We have two matrices stored as lists in our computer

Q2: What do we want?
 - We want to find a new matrix that is the sum of both matrices 

Q3: How would we get there?
 - We can create a new list (our resulting matrix) by taking corresponding elements [a,b] from both matrices and adding them together to 
 return our summation matrix (adding lists together)

	# Have our two matrices defined
def mat_mult(matrix_a, matrix_b)
Let matrix_a = A
Let matrix_b = B

	# Define the elements in our matrices 
Let a in range(A) and b in range(B)

C[a][b] = A[a][b]+B[a][b]

	#store our resulting matrix

C = A

Problem #4
Write an algorithm implementing matrix-vector mult. using linear combination of column method.

Q1: What do we have?
 - We have a matrix and a vector stored on a computer

Q2: What do we want?
 - We want to find the resulting matrix that is the product of the initial matrix multiplied by the vector

Q3: How do we get there?
 - Creating a result vector of 0's', they will have the sme size as a column on our input matrix. Then, multiply components from the matrix 
 by corresponding element in the vector

	# 

Problem #5
Write an algorithm to implement matrix-matrix multiplication using your algorithm from #4

Q1: What do we have?
 - We have two matrices stored as two lists

Q2: What do we want?
 - We are looking. for the product of the matrices, returned as a new list

Q3: How will we get there?
 - Initialize result matrix as copy of matrix B, we get new matrix named result. Overwrite with output, called mat_vec(matrix_a, component)
 """
 
 #test_vector_01 = [1, 2, 4]
 #test_vector_02 = [3, 1, 2]

# Problem 1
import numpy as np
arr1=np.array([1, 2, 4])
scalar2=np.array([2])
c = np.multiply(arr1, scalar2) 
print(c)

import numpy as np
arr1=np.array([3, 1, 2])
scalar2=np.array([3])
c = np.multiply(arr1, scalar2)
print(c)
 
# Problem 2
import numpy as np
matrix1=np.array([1, 2, 4])
scalar1=np.array([2])
c = np.multiply(matrix1, scalar1)
print(c)

# Forgot we couldn't use numpy. Gave up :( 








