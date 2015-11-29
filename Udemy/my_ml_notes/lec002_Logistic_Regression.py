
# coding: utf-8

# In[1]:

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


# In[2]:

def logistic(val):
    return 1/(1+math.exp(-val))


# In[3]:

logistic(-500)


# In[4]:

x = np.linspace(-10,10,1000)


# In[5]:

x[:10]


# In[6]:

y = [logistic(val) for val in x]


# In[7]:

plt.plot(x,y)


# -----------
# ### Part 3: Dataset Analysis
# Let us go ahead and take a look at the [dataset](http://statsmodels.sourceforge.net/stable/datasets/generated/fair.html)
# 
# The dataset is packaged within Statsmodels. It is a data set from a 1974 survey of women by Redbook magazine. Married women were asked if they have had extramarital affairs. The published work on the data set can be found in:
# 
# [Fair, Ray. 1978. “A Theory of Extramarital Affairs,” `Journal of Political Economy`, February, 45-61.](http://fairmodel.econ.yale.edu/rayfair/pdf/1978a200.pdf)
# 
# It is important to note that this data comes from a self-reported survey, which can have many issues as far as the accuracy of the data. Also this analysis isn't trying to promote any agenda concerning women or marriage, the data is just interesting but its accuracy should be met with a healthy dose of skepticism.
# 
# We'll ignore those issues concerning the data and just worry about the logistic regression aspects to the data.

# In[8]:

df = sm.datasets.fair.load_pandas().data


# In[9]:

df.head()


# In[10]:

df['affairs']>0


# In[11]:

df['label'] = np.where(df['affairs']>0,1,0)


# In[12]:

np.sum(df['label'])


# In[13]:

len(df)


# In[14]:

df.head()


# In[15]:

df.drop('label',axis = 1,inplace=True)


# In[16]:

df.head()


# In[17]:

df['Had_Affair'] = df['affairs'].apply(lambda rec: 1 if rec >0 else 0)


# In[18]:

df.head()


# In[19]:

np.sum(df['Had_Affair'])


# In[20]:

df.groupby('Had_Affair').mean()


# In[21]:

plt.scatter(df['yrs_married'],df['affairs'])


# In[22]:

sns.factorplot('age',data=df,hue='Had_Affair',palette = 'coolwarm',kind = 'count')


# In[27]:

order1 = sorted(np.unique(df['yrs_married']))


sns.factorplot('yrs_married',data=df,kind = 'count',palette = 'coolwarm',hue = 'Had_Affair',x_order = order)


# In[26]:

order = sorted(np.unique(df['yrs_married']))
order


# In[28]:

sns.factorplot('children',data=df,kind = 'count',palette = 'coolwarm',hue = 'Had_Affair',x_order = sorted(np.unique(df['children'])))


# In[29]:

sns.factorplot('educ',data=df,kind = 'count',palette = 'coolwarm',hue = 'Had_Affair',x_order = sorted(np.unique(df['educ'])))


# In[ ]:



