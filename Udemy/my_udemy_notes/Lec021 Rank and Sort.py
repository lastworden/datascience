
# coding: utf-8

# In[10]:

import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from numpy.random import randn


# In[4]:

ser1 = Series(np.arange(3),index = ['C','A','B'])
ser1


# In[7]:

ser1.sort_index()


# In[9]:

ser1.order()


# In[28]:

ser2 = Series(randn(10))
ser2


# In[29]:

ser2.order()


# In[30]:

ser2.rank()


# In[15]:

ser2.sort()
ser2


# In[24]:

ser3 = Series(randn(10))
ser3


# In[25]:

ser3.rank()


# In[26]:

ser3.order()


# In[27]:

ser3.rank()


# In[31]:

ser4 = Series(randn(10))
ser4


# In[33]:

ser4.sort()
ser4


# In[ ]:



