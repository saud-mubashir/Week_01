# 01. Write a NumPy program to create an array of all even integers from 30 to 70.
import numpy as np

# Create an array of even integers from 30 to 70
even_integers = np.arange(30, 71, 2)

# Print the resulting array
print(even_integers)

# 02. Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution.
import numpy as np

# Generate an array of 15 random numbers from a standard normal distribution
random_numbers = np.random.randn(15)

# Print the resulting array
print(random_numbers)

# 03. How to compute the cross-product of two matrices in NumPy?
# In NumPy, you can compute the cross-product of two matrices using the 'numpy.cross' function.

# 04. How to compute the determinant of an array using NumPy?
# Use `numpy.linalg.det()` to compute the determinant of an array in NumPy. For example: `det_value = np.linalg.det(my_array)`.

# 05. How to create a 3x3x3 array with random values using NumPy?
# We can create a 3x3x3 array with random values in NumPy using the 'numpy.random.rand' function.

# 06. How to create a 5x5 array with random values and find the minimum and maximum values using NumPy?
# We can create a 5x5 array with random values in NumPy using the 'numpy.random.rand' function and then find the minimum and maximum values using 'numpy.min' and 'numpy.max'.

# 07. How to compute the mean, standard deviation, and variance of a given array along the second axis in NumPy?
# We can compute the mean, standard deviation, and variance along the second axis of a given array in NumPy using the 'numpy.mean', 'numpy.std', and 'numpy.var' functions, respectively.