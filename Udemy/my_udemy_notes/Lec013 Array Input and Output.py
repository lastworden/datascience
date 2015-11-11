
# coding: utf-8

# In[2]:

import numpy as np


# In[4]:

arr = np.arange(5)
arr


# In[5]:

np.save('arr_save_example',arr)


# In[8]:

arr = np.arange(10)


# In[9]:

arr


# In[11]:

b = np.load('arr_save_example.npy')
b


# In[12]:

np.savez('arr_zip_file.npz',x=arr,y=b)


# In[13]:

arch_arr = np.load('arr_zip_file.npz')
arch_arr


# In[14]:

arch_arr['x']


# In[16]:

arch_arr['y']


# In[20]:

mat1 = np.arange(9).reshape((3,3))+1
mat1


# In[23]:

np.savetxt('arr_txt_file.txt',mat1,delimiter = ',')


# In[27]:

mat2 = np.loadtxt('arr_txt_file.txt',delimiter = ',')
mat2


# In[28]:

mat2.dtype


# In[30]:

mat1.dtype


# In[ ]:



