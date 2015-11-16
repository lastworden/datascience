
# coding: utf-8

# In[23]:

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[2]:

arr = np.array([[1,2,np.nan],[np.nan,3,4]])
arr


# In[4]:

df1 = DataFrame(arr,index = ['A','B'],columns = ['One','Two','Three'])
df1


# In[5]:

df1.sum()


# In[6]:

df1.sum(axis=1)


# In[7]:

df1.min()


# In[8]:

df1.min(axis =1)


# In[13]:

df1.idxmin()


# In[10]:

df1.mean()


# In[11]:

df1


# In[12]:

df1.mean(axis = 1)


# In[14]:

df1.cumsum()


# In[18]:

df1


# In[17]:

df1.describe()


# In[ ]:

from IPython.display import YouTubeVideo
# For more information about Covariaance and Correlation
# Check out these great videos!
# Video credit: Brandon Foltz.

#CoVariance
YouTubeVideo('xGbpuFNR1ME')


# In[ ]:

#Correlation
YouTubeVideo('4EXNedimDMs')


# In[6]:

import pandas.io.data as pdweb
import datetime as dt


# In[7]:

prices = pdweb.get_data_yahoo(['CVX','XOM','BP'],start=dt.datetime(2010,1,1)
                             ,end = dt.datetime(2013,1,1))['Adj Close']


# In[8]:

prices.head()


# In[9]:

type(prices)


# In[10]:

len(prices)


# In[11]:

volume = pdweb.get_data_yahoo(['CVX','XOM','BP'],start=dt.datetime(2010,1,1)
                             ,end = dt.datetime(2013,1,1))['Volume']


# In[12]:

len(volume)


# In[13]:

volume.head()


# In[14]:

rets = prices.pct_change()


# In[15]:

rets.head()


# In[16]:

#correlation of the stocks
corr = rets.corr


# In[17]:

get_ipython().magic('matplotlib inline')
prices.plot()


# In[18]:

prices.columns


# In[19]:

type(prices.index)


# In[20]:

import seaborn as sns
import matplotlib.pyplot as plt


# In[21]:

sns.corrplot(rets, diag_names = False, annot =False)


# In[25]:

ser1 = Series(list('wwxyzwwxyxa'))
ser1


# In[26]:

ser1.unique()


# In[27]:

ser1.value_counts()


# In[ ]:



