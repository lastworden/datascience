
# coding: utf-8

# In[24]:

# Data Imports
import numpy as np
import pandas as pd
from pandas import Series,DataFrame

# Math
import math

# Plot imports
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().magic('matplotlib inline')

# Machine Learning Imports
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split

# For evaluating our ML results
from sklearn import metrics

# Dataset Import
import statsmodels.api as sm


# In[25]:

def logistic(val):
    return 1/(1+math.exp(-val))


# In[26]:

logistic(-500)


# In[27]:

x = np.linspace(-10,10,1000)


# In[28]:

x[:10]


# In[29]:

y = [logistic(val) for val in x]


# In[30]:

plt.plot(x,y)


# In[ ]:



