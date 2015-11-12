
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn
    


# In[3]:

ser1 = Series(np.arange(1,5),index = ['A','B','C','D'])
ser1


# In[4]:

ser2 = ser1.reindex(['A','B','C','D','E','F'])
ser2


# In[5]:

ser1


# In[12]:

ser2.reindex(['A','B','C','D','E','F','G'], fill_value = 0)


# In[25]:

ser3 = Series(['USA','Mexico','Canada'], index = [0,5,10])
ser3


# In[29]:

r = range(15)
r


# In[32]:

ser3.reindex(r,method = 'ffill') #forward fill


# In[37]:

df1 = DataFrame(randn(25).reshape((5,5)), index = ['A','B','D','E','F'], columns = ['col1','col2','col3','col4','col5'])
df1


# In[40]:

df2 = df1.reindex(['A','B','C','D','E','F'])
df2


# In[42]:

new_cols = ['col%s'%str(i) for i in range(1,7)]
new_cols


# In[43]:

df2.reindex(columns = new_cols)


# In[45]:

df1


# In[51]:

df1.ix['A','col1']


# In[ ]:



