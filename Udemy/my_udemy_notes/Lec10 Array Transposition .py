
# coding: utf-8

# In[1]:

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


# In[31]:

arr3d = np.arange(48).reshape((3,4,4))
arr3d


# In[33]:

arr3d[0]


# In[34]:

arr3d[0][1]


# In[35]:

arr3d.T


# In[36]:

arr3d


# In[37]:

arr3d.transpose((1,0,2))


# In[44]:

arr = np.array([[1,2,3]])


# In[45]:

arr.swapaxes(0,1)


# In[ ]:



