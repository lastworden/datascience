
# coding: utf-8

# In[4]:

import numpy as np
from pandas import Series,DataFrame
from numpy.random import randn
import pandas as pd


# In[5]:

ser1 = Series(randn(6),index = [[1,1,1,2,2,2],list('abcabc')])
ser1


# In[7]:

ser1.index


# In[13]:

ser1[1]['a']


# In[15]:

ser1[1,'a']


# In[16]:

ser1[:,'a']


# In[21]:

ser1


# In[20]:

df1 = ser1.unstack()
df1


# In[27]:

df2 = DataFrame(np.arange(16).reshape((4,4)),
               index = [['a','a','b','b'],['1','2','1','2']],
               columns = [['NY','NY','LA','SF'],['cold','hot','hot','cold']])
df2


# In[30]:

df2.index.names = ['INDEX_1','INDEX_2']
df2.columns.names = ['CITIES','TEMPERATURE']


# In[31]:

df2


# In[32]:

df2.swaplevel('CITIES','TEMPERATURE',axis= 1)


# In[34]:

df2.swaplevel('INDEX_1','INDEX_2')


# In[36]:

df2.sortlevel(1)


# In[38]:

df2.swaplevel('INDEX_1','INDEX_2').sortlevel(0)


# In[40]:

df2.swaplevel('CITIES','TEMPERATURE',axis = 1).sortlevel(0,axis = 1)


# In[48]:

df2


# In[51]:

df2.sum(level = 'TEMPERATURE',axis =1)


# In[ ]:




# In[ ]:



