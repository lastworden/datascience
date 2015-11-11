
# coding: utf-8

# In[2]:

import numpy as np


# In[2]:

arr =np.arange(50).reshape((10,5))


# In[3]:

arr


# In[16]:

tarr = arr[:,1]
tarr


# In[18]:

tarr.shape


# In[19]:

tarr = arr.T


# In[20]:

tarr


# Even Tanspose is not a deep copy.

# In[21]:

tarr[0,0] =100
tarr


# In[22]:

arr


# In[25]:

arr1 = np.arange(6).reshape(2,3)
arr1


# In[27]:

arr2 = np.arange(6,12).reshape(3,2)
arr2


# In[29]:

arr_dot = arr1.dot(arr2)
arr_dot


# In[8]:

arr3d = np.arange(18).reshape((3,2,3))
arr3d


# In[9]:

arr3d[0]


# In[10]:

arr3d[0][1]


# In[11]:

arr3d.T


# In[12]:

arr3d


# In[14]:

arr3d.shape


# In transpose function, the argument is new permutation of axes. For example, If you pass (1,0,2) as argmet, the element arr[x,y,z] -> arr[y,x,z] in the result
# 
# 

# In[13]:

arr3d.transpose((1,0,2))


# In[44]:

arr = np.array([[1,2,3]])


# In[45]:

arr.swapaxes(0,1)


# Convert n d array to n+1 d array
# <http://stackoverflow.com/questions/5954603/transposing-a-numpy-array>

# In[19]:

arr = np.array([1,2,3])[None]


# In[20]:

arr


# In[22]:

t = np.array(50)
t


# In[23]:

print(t)


# In[24]:

t.shape


# In[26]:

np.ndim(arr3d)


# In[27]:

np.ndim(t)


# In[ ]:



