
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

arr = np.arange(9).reshape((3,3))
arr


# In[3]:

np.sqrt(arr)


# In[4]:

np.exp(arr)


# In[6]:

np.log(arr+1)


# ** Create a random normal distributed array

# In[13]:

A = np.random.randn(10)
A


# In[15]:

B = np.random.randn(10)
B


# In[12]:

np.random.randn(9).reshape((3,3))


# Binary functions

# In[17]:

np.add(A,B)


# In[20]:

np.maximum(A,B)


# In[21]:

#For full and extensive list of all universal functions
website = "http://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs"
import webbrowser
webbrowser.open(website)


# In[23]:

np.bitwise_and(np.array([1,2,0,0,1]), np.array([1,0,0,1,3]))


# In[ ]:



