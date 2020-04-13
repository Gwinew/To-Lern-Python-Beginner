# Numpy
#
# import
#
# Before we use the function from numpy package, we need to import this package.
import numpy as np

height=[1.73,1.68,1.71,1.89,1.79]
weight=[65.4,59.2,63.6,88.4,69.7]

np_height=np.array(height)
np_weight=np.array(weight)
print("{}\n{}".format(np_height,np_weight))

bmi=np_weight/np_height**2

print(bmi)
print("{:6.3f}".format(bmi[1])) # We can not use {:6.3f} for all array.

# remarks
#
# We can not comparison many of types in once array, if we use many types then convert this value to "str".

python_list=[1,2,3]
numpy_array=np.array([1,2,3])

print(python_list + python_list)    # we get [1,2,3,1,2,3]

print(numpy_array + numpy_array)    # we get [2,4,6]

#
# numpy subsetting
#
# We can call results from array using operator
print(bmi >23)
print(bmi[bmi>23])
#
print("=======================================================")
#
# 2D numpy array:
#
type(np_height)     # numpy.ndarray     ndarray = N-dimensional array
#
# 2d numpy array
np_2d=np.array([[1.73,1.68,1.71,1.89,1.79],[65.4,59.2,63.6,88.4,69.7]])
print(np_2d)
print(np_2d.shape)  # show; 2,5     it means 2 row and 5 columns
# If we have only ona different type in array then all array covert value to str
npa_2d=np.array([[1.73,1.68,1.71,1.89,1.79],[65.4,59.2,63.6,88.4,'69.7']])
print(npa_2d)
#
#
# working on array:
#
# We can use a commend to show rows and columns:
print(np_2d[0])     # 0 row is showed
print(np_2d[0][2])  # 0 row and from 2 column is showed value: 1.71
# The same:
print(np_2d[0,2])
#
print(np_2d[:,1:3]) # show all rows and 2 value from the columns
#
#
print("=======================================================")
#
# Numpy big data:
#
# Compute the arithmetic mean along the specified axis
print(np.mean(np_2d[1,:]))
#
# Compute the median along the specified axis.
print(np.median(np_2d[0,:]))
#
# Return Pearson product-moment correlation coefficients.
print(np.corrcoef(np_2d[:,1],np_2d[:,3]))
#
# Compute the standard deviation along the specified axis.
print(np.std(np_2d[:,0]))
#
# Sum of array elements over a given axis.
print(np.sum(np_2d[0,:]))
#
# Return a sorted copy of an array.
print(np.sort(np_2d[0,:]))
#
#
# Generate data
height=np.round(np.random.normal(1.75, 0.2, 5000),2)
weight=np.round(np.random.normal(60.32, 15, 5000),2)
np_city=np.column_stack((height, weight))
#
# Do simply calculation:
print("Arithmetic mean from city is {}".format(np.mean(np_2d[:,0]),np.mean(np_2d[:,1])))
print("Median along from city is {}".format(np.median(np_2d[:,0]),np.median(np_2d[:,1])))
print("Correlation coefficients from city is {}".format(np.corrcoef(np_2d[:,0],np_2d[:,1])))
print("Standard deviation from city is {}".format(np.std(np_2d[:,0]),np.std(np_2d[:,1])))
