
# coding: utf-8

# In[3]:

import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[6]:

points = np.arange(-5,5,0.01)
points


# In[7]:

dx, dy = np.meshgrid(points,points)


# In[8]:

dx


# In[9]:

dy


# In[10]:

dx.shape


# In[11]:

dy.shape


# In[19]:

z = np.sin(dx)+np.sin(dy)
z


# In[32]:

plt.imshow(z)
plt.colorbar()
plt.title('Plot for cos(x)+cos(y)')


# In[30]:

y = np.cos(dx)+np.cos(dy)


# In[31]:

plt.imshow(y)
plt.colorbar()
plt.title('Plot for cos(x)+cos(y)')


# 
# 
#     In brief, numpy.meshgrid is modelled after Matlab's meshgrid command. It is used to vectorise functions of two variables, so that you can write
# 
#     x = numpy.array([1, 2, 3])
#     y = numpy.array([10, 20, 30]) 
#     XX, YY = numpy.meshgrid(x, y)
#     ZZ = XX + YY
# 
#     ZZ => array([[11, 12, 13],
#              [21, 22, 23],
#              [31, 32, 33]])
# 
#     So ZZ contains all the combinations of x and y put into the function.
# <http://stackoverflow.com/questions/12402045/mesh-grid-functions-in-python-meshgrid-mgrid-ogrid-ndgrid>

# In[33]:

A = np.array([1,2,3,4])
A


# In[34]:

B = A.copy()*100
B


# In[36]:

C = np.array([True,False,True,False])


# In[38]:

Res = [(a if c else b) for a,b,c in zip(A,B,C)]
Res


# In[42]:

str(zip(A,B,C))


# In[44]:

res2 = np.where(C,A,B)
res2


# In[45]:

for a,b,c in zip(A,B,C):
    print(a,b,c)


# In[3]:

np.meshgrid(np.arange(4),np.arange(4))


# In[5]:

from numpy.random import randn


# In[7]:

arr = randn(5,5)
arr


# In[9]:

np.where(arr<0,0,1)


# In[4]:

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr


# In[5]:

arr.sum()


# In[6]:

arr.sum(0)


# In[7]:

arr.sum(1)


# In[13]:

arr.max()


# In[14]:

arr.max(0)


# In[15]:

arr.sum(1)


# In[16]:

arr.dot(arr)


# In[17]:

arr


# In[18]:

arr.mean()


# In[19]:

arr.std()


# In[21]:

arr.var()


# In[22]:

arr.std()**2


# In[23]:

barr = np.array([True,False,True,False])
barr


# In[24]:

barr.any()


# In[31]:

help(barr.any)


# In[26]:

barr.sum()


# In[27]:

barr.all()


# In[29]:

help(np.all)


# In[35]:

arr = randn(9)
arr


# In[37]:

arr.sort()
arr


# In[40]:

arr = randn(3,3)
arr


# In[41]:

arr.sort()
arr


# In[47]:

countries = np.array(['India','Australia','China','USA','India', 'Russia','China'])
countries


# In[48]:

np.unique(countries)


# In[49]:

np.in1d(['USA','India','England','Spain'],countries)


# In[3]:

s = np.array([1,0,0,1,1,1])


# In[4]:

s>=1


# In[5]:

s[s>=1]


# In[6]:

s.reshape(3,2)


# In[7]:

s>=1


# In[8]:

s[s>=1]


# In[ ]:



