
# coding: utf-8

# In[2]:

import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# In[5]:

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().magic('matplotlib inline')


# In[8]:

from sklearn.datasets import load_boston


# In[9]:

boston = load_boston()


# In[11]:

type(boston)


# In[15]:

print(boston.DESCR)


# In[16]:

plt.hist(boston.target, bins = 50)
plt.xlabel('Prices in $1000s')
plt.ylabel('Number of Houses')


# In[17]:

plt.scatter(boston.data[:,5],boston.target)
plt.xlabel('Number of Rooms')
plt.ylabel('Prices in $1000s')


# In[18]:

boston_df = DataFrame(boston.data)


# In[22]:

boston_df.columns = boston.feature_names
boston_df.head()


# In[25]:

boston_df['Price'] = boston.target
boston_df.head()


# In[27]:

sns.lmplot('RM','Price',data = boston_df)


# In[ ]:



