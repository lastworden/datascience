
# coding: utf-8

# In[7]:

import numpy as np


# In[8]:

my_list1 = [1,2,3,4,5]


# In[9]:

my_arr1 = np.array(my_list1)


# In[10]:

my_arr1


# In[11]:

my_list2 = [11,22,33,44,55]


# In[12]:

my_2list = [my_list1, my_list2]


# In[15]:

my_arr2d = np.array(my_2list)


# In[18]:

my_arr2d


# In[19]:

my_arr2d.shape


# In[20]:

my_arr2d.dtype


# In[21]:

np.zeros(5)


# In[28]:

my_zero_arr = np.zeros((3,4))
my_zero_arr 


# In[27]:

my_zero_arr.dtype


# In[35]:

np.ones((4,3))


# In[36]:

np.empty((3,2))


# In[37]:

np.empty(5)


# In[39]:

np.eye(4)


# In[40]:

np.arange(5)


# In[42]:

#start, end, increment_step
np.arange(1,20,3) 


# In[ ]:



