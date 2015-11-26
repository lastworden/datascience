
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[5]:

arr1 = np.arange(9).reshape((3,3))
arr1


# In[9]:

np.concatenate([arr1,arr1], axis =1)



# In[10]:

np.concatenate([arr1,arr1], axis =0)


# In[11]:

ser1 = Series([1,2,3],index = ['A','B','C'])
ser1


# In[13]:

ser2 = Series([4,5],index = ['D','E'])
ser2


# In[14]:

pd.concat([ser1,ser2])


# In[15]:

pd.concat([ser1,ser2],axis = 1)


# In[16]:

pd.concat([ser1,ser2],axis = 0)


# In[17]:

pd.concat([ser1,ser2], keys = ['key1','key2'])


# In[21]:

df1 = DataFrame(np.random.randn(4,3),columns = ['X','Y','Z'])
df1


# In[22]:

df2 = DataFrame(np.random.randn(3,3),columns = ['Y','Q','X'])
df2


# In[24]:

pd.concat([df1,df2])


# In[25]:

pd.concat([df1,df2], ignore_index = True)


# In[26]:

#For more info in documentation:
url='http://pandas.pydata.org/pandas-docs/dev/generated/pandas.tools.merge.concat.html'


# In[ ]:



