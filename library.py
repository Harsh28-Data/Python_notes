# import numpy as hk
# x=hk.array([12,45,78,"science",21j])
# print(x)  

# print(type(x)) #it shows the data type of variable

# print(hk.ndim(x)) #it shows the number of dimension



# print(x.shape) #it shows the shape of the array


# print(x.dtype) #high complexity of data in array

# string    u64
# complex   complex128
# float     float64
# int       int64



# x=hk.array([[12,45,78,89]])

# print(x)
# print("Type= ",type(x))
# print("Data Type= ",x.dtype)
# print("Number of Dimension",hk.ndim(x))
# print("Shape of Array= ",x.shape)

# y=hk.array([[[58,67,48,"Python",58j,True]]])


# print(y)
# print("Type= ",type(y))
# print("Data Type= ",y.dtype)
# print("Number of Dimension",hk.ndim(y))
# print("Length= ",len(y))
# print("Shape= ",y.shape)




# z=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

# ar=hk.array(z)


# print(ar)
# t=ar.shape
# print(f"There are {t[0]} Rows and {t[1]} Columns")



# x=hk.array([[12,45,56],[98,87,36]])
# print(x)


# # print(x[0][1])
# # print(x[1][2])
# # print(x[0][2])
# # print(x[0][0])
# # print(x[1][0])

# 12,45
# 87,36
# 45,56  




# import numpy as h

# x=h.array([12,45,78,89,56])
# print(x)
# # print(x.shape)


# print(x[2])
# print(x[-1])
# print(x[0])




# x=h.array([[[12,45,78,56,23]]])
# print(x)


# print(x[0,0,1])
# print(x[0,0,-1])
# print(x[0,0,0:])
# print(x[0,0,1:3])






# # print(x)
# # print(x.shape)

# # [12,45,10]
# print(x[0,0,0])


# #[8,7]
# print(x[0,0,2,1:])

# #[[12,45,10],[96,63,52]]
# print(x[0,0,0:2])

# #63
# print(x[0,0,1,1])

# #10
# print(x[0,0,0,2])

# #96
# print(x[0,0,1,0])

# #45
# print(x[0,0,0,1])



# x=h.array([[[[12,45,10],[96,63,52],[9,8,7]]]])





# # [10,45,12]
# print(x[0,0,0,::-1])

# #[63,96]
# print(x[0,0,1,-2:-4:-1])

# #[12,10]
# print(x[0,0,0,::2])

# #[7,8]
# print(x[0,0,2,:-3:-1])
# #[9,7]
# print(x[0,0,2,::2])




# ndmin = minimum number of Dimension

# x=h.array([12,45,78,89],ndmin=5)
# print(x)






# # 1.  45 to 100
# x[0,0,0,0,1]=100



# # 2.  89 to 200
# x[0,0,0,0,3]=200


# # 3.  12 to 3000
# x[0,0,0,0,0]=300


# print(x)





#----------------------------------------------------------------------------------

# 1. arrange
# 2. reshape
# 3. zero
# 4. dtype
# 5. full
# 6. one
# 7. median
# 8. sum
# 9. mean
# 10. std
# 11. variance
# 12. concatenate
# 13. transpose
# 15. argmin
# 16. argmax
# 17. fatten
# 18. 


# import numpy as h


# x=h.array([12,45,78,56],ndmin=10)

# print(x)



# y=h.array([12,45,782,56],dtype="str")
# print(y)
# print(y.dtype)




# Arange:- it is used to print the numer in the sequence
#          according to the range

# x=h.arange(starting, ending, step_size)

# x=h.arange(1,21,3)
# print(x)
# print(type(x))
# print(x.dtype)
# print(h.ndim(x))
# print(len(x))
# print(x.shape)




# x=h.arange(1,11,dtype="float")
# print(x)

# y=h.array(x,ndmin=5)
# print(y)




# x=h.arange(40,34,-1)
# print(x)




# Reshape:- it is used to convert from array to matrix with 
#             combination


# x=h.array([2,4,5,8,9,6,3,2,1])
# print(x)

# y=x.reshape(3,3)
# print(y)

# x=h.arange(1,100,4)
# print(x)
# print(len(x))

# y=x.reshape(5,5)
# print(y)


# x=h.arange(1,9)
# print(x)


# y=x.reshape(2,2,2)
# print(y)





# Concatenate:- it is used to join the array.


# x=h.array([12,3,4,5,7])
# y=h.arange(10,16)
# print(x)
# print(y)


# z=h.concatenate((x,y))
# print(z)



# x=h.array([[1,2,3],[4,5,6]])
# print(x)
# print(x.transpose())


# y=h.array([h.arange(1,9)])
# print(y)
# print(y.transpose())








#=================== zero =============================

import numpy as np



# x=np.zeros((4,5))
# print(x)


# y=np.zeros((3,5,5))
# print(y)



# z=np.ones((4,5))
# print(z)



# x=np.full((10,5),10.)
# print(x)



# Random.randit() :- It is used to generate the random Number 
                  # according to user




# x=np.random.randint(1,10,10)
# print(x)


# y=np.random.randint(1,100,50)
# print(y)




# z=np.random.randint(10,20,10)
# z=set(z)
# print(z)




# linspace() :- it is used to generate the number in sequencely
# in the same distance according to the user



# x=np.linspace(1,10,10)
# print(x)

# y=np.linspace(1,10,50)
# print(y)



# Flatten:- it is used to reduce the dimension of array
# OR it is used to convert the matrix into an array

# x=np.array([[[10,45,78,89],[10,20,30,40],[96,74,85,23]]])
# print(x)


# x=x.flatten()
# print(x)


# Diagflat :- It is used to convet the matrix to show all values in diagonal

# diad :- it extracts the diagonal value of matrix into a array


# x=np.array([[1,2,3,4],[2,6,7,2]])

# y=np.diagflat(x)
# print(y)

# z=np.diag(y)
# print(z)


# x=np.arange(1,20)
# y=np.diagflat(x)
# print(y)



# flip or fliplr :- it is used to flip ro reverse the array


# x=np.array([[12,45,78,56]])

# print(x)
# print(np.flip(x))

# print(np.fliplr(x))




#---------------------------------------------------------------
# mean :- sum of all the numberds divided by total numbers
# median :- it shows the mid value
# std :- it is the square root of the variance
# variance :- it shows the spread between the data point to mean value



# x=np.array([12,45,89,56,23,18,40])

# print("Average= ",np.mean(x))

# print("Median= ",np.median(x))

# print("Standard Deviation= ",np.std(x))

# print("Variance= ",np.var(x))

# print("Sum= ",np.sum(x))









x=np.array([[[12,45,78],[89,56,78]]])

x=x.flatten()

for i in x:
	print(i)


for i in np.nditer(x):
	print(i)