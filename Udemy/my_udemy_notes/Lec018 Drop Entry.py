
# coding: utf-8

# In[5]:

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[6]:

ser1 = Series(np.arange(4),index = ['a','b','c','d'])
ser1


# In[8]:

ser1.drop('b')


# In[12]:

df1 = DataFrame(np.arange(9).reshape((3,3)),index = ['SF','LA','NY'],columns = ['pop','size','year'])
df1


# In[13]:

df1.drop('LA')


# In[15]:

df1.drop('size', axis = 1)


# In[ ]:



