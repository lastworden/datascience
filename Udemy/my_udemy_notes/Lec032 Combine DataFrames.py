
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[4]:

ser1 = Series([2,np.nan,4,np.nan,6,np.nan],index = ['Q','R','S','T','U','V'])
ser1


# In[5]:

ser2 = Series(np.arange(len(ser1)),dtype = np.float64,index = ['Q','R','S','T','U','V'])
ser2


# In[9]:

Series(np.where(pd.isnull(ser1),ser2,ser1),index = ser1.index)


# In[10]:

ser1.combine_first(ser2) 


# In[12]:

nn = np.nan
df_odds = DataFrame({'X':[1,nn,3,nn],
                        'Y':[nn,5,nn,7],
                        'Z':[nn,9,nn,11]})
df_odds


# In[15]:

df_evens = DataFrame({'X':[2.,4.,nn,6.,8.],
                     'Y':[nn,10.,12.,14.,16.]})
df_evens


# In[16]:

df_odds.combine_first(df_evens)


# In[ ]:



