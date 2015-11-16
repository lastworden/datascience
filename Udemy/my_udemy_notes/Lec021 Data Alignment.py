
# coding: utf-8

# In[2]:

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[3]:

ser1 = Series([0,1,2],index = ['A','B','C'])
ser1


# In[4]:

ser2 = Series([3,4,5,6], index = ['A','B','C','D'])
ser2


# In[5]:

ser1+ser2


# In[18]:

df1 = DataFrame(np.arange(4).reshape((2,2)),columns = list('AB'),index = ['NYC','LA'])
df1


# In[22]:

df2 = DataFrame(np.arange(9).reshape((3,3)), index = ['NYC','SFO','LA'], columns = list('ADC'))
df2


# In[23]:

df1+df2


# In[24]:

df1


# In[25]:

df2


# In[27]:

df1.add(df2,fill_value = 0)


# In[28]:

df2.ix[2]


# In[30]:

ser3 = df2.ix[0]
ser3


# In[36]:

df2-ser3


# In[ ]:



