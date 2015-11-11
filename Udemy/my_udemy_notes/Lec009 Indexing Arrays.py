
# coding: utf-8

# In[1]:

import numpy as np


# # Indexing in 1d array

# In[11]:

arr = np.arange(0,11)


# In[12]:

arr


# In[13]:

np.arange(0,12,2)


# In[14]:

arr[3]


# In[15]:

arr[2:5]


# In[16]:

arr[3:5] = [1,1]


# In[17]:

arr


# In[19]:

arr[3:6] = 100


# In[20]:

arr


# In[23]:

arr[3:6] = np.zeros(3)


# In[24]:

arr


# In[26]:

arr = np.arange(0,11)
arr


# In[27]:

arr[:]


# In[29]:

arr[4:]


# In[30]:

arr[:5]


# In[31]:

arr[-1]


# In[32]:

arr[-5:-1]


# In[34]:

arr[-10:]


# In[37]:

arr[-2:111]


# In[38]:

arr[12]


# In[40]:

slice_arr = arr[0:5]
slice_arr


# In[41]:

slice_arr[:] = 100
slice_arr


# Assignment creates only a sallow copy. the slice_arr here will be just a view of the original array

# In[42]:

arr


# user array.copy() method if you want a deep copy of the array

# In[46]:

arr


# In[47]:

arr2 = arr.copy()


# In[48]:

arr2


# In[49]:

arr2[:] = 5


# In[50]:

arr2


# In[53]:

arr


# # Indexing in 2d array

# In[56]:

[[1,2,3]]*5 #example for normal lists multiplication


# In[57]:

arr2d = np.array([[1,2,3],[11,12,15],[20,25,30]])


# In[58]:

arr2d


# In[59]:

arr2d[1]


# In[60]:

arr2d[0:2]


# In[65]:

arr2d[1][2]


# In[67]:

arr2d[0:2,1:3]


# In[68]:

arr2d[1,2]


# In[88]:

arr_2d= np.zeros((10,10))


# In[89]:

arr_2d


# In[90]:

arr_2d.shape


# In[91]:

arr_len = arr_2d.shape[0]
arr_len


# # Fancy Indexing

# In[92]:

for i in range(arr_len):
    arr_2d[i] = i


# In[93]:

arr_2d


# In[98]:

arr_2d[[1,3,7]]


# In[99]:

arr_2d[[6,1,3]]


# In[102]:

arr_2d[[6,1,3],1]


# In[103]:

arr_2d[[6,1,3],[1,2]]


# In[ ]:



