
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# In[2]:

from pandas import read_html


# In[3]:

url = 'http://www.fdic.gov/bank/individual/failed/banklist.html'


# In[4]:

df_list = pd.io.html.read_html(url)


# In[6]:

df1 = df_list[0]


# In[7]:

df1


# In[9]:

df1.columns


# In[10]:

df1.columns.values


# In[ ]:



