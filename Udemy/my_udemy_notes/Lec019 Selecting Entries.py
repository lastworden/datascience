
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[8]:

ser1 = Series(range(4),index = ['A','B','C','D'])
ser1


# In[9]:

ser1 *= 2
ser1


# In[10]:

ser1['B']


# In[11]:

ser1[1]


# In[12]:

ser1[1:4]


# In[14]:

ser1[['A','C']]


# In[19]:

ser1[['True','True','False','False']]


# In[21]:

ser1[[2,3]]


# In[24]:

ser1>3


# In[22]:

ser1[ser1>3]


# In[26]:

ser1


# In[28]:

ser1[ser1>3]=10
ser1


# In[31]:

df1 = DataFrame(np.arange(25).reshape((5,5)), index = ['ind%s'%str(i+1) for i in range(5)],
               columns = ['col%s'%str(i+1) for i in range(5)])
df1


# In[33]:

df1['col1']


# In[34]:

df1[['col1','col2']]


# In[35]:

df1[[1,2]]


# In[41]:

df1[[i for i in range(3)]]


# In[42]:

df1[df1>5]


# In[43]:

df1[df1['col1']>10]


# In[44]:

df1>5


# In[46]:

df1['col1']>5


# In[48]:

df1


# In[51]:

df1.ix[['ind1','ind3']]


# In[52]:

df1.ix[2:4]


# In[54]:

df1.ix[[1,3]]


# In[ ]:



