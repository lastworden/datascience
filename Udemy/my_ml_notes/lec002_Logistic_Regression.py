
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


# In[23]:

order1 = sorted(np.unique(df['yrs_married']))


sns.factorplot('yrs_married',data=df,kind = 'count',palette = 'coolwarm',hue = 'Had_Affair',x_order = order1)


# In[24]:

order = sorted(np.unique(df['yrs_married']))
order


# In[25]:

sns.factorplot('children',data=df,kind = 'count',palette = 'coolwarm',hue = 'Had_Affair',x_order = sorted(np.unique(df['children'])))


# In[26]:

sns.factorplot('educ',data=df,kind = 'count',palette = 'coolwarm',hue = 'Had_Affair',x_order = sorted(np.unique(df['educ'])))


# In[27]:

occ_dummies = pd.get_dummies(df['occupation'])
hus_occ_dummies = pd.get_dummies(df['occupation_husb'])


# In[28]:

hus_occ_dummies.head()


# In[29]:

occ_dummies.columns = ['occ%d'%i for i in range(1,7)]
occ_dummies.columns


# In[30]:

hus_occ_dummies.columns = ['hocc%d'%i for i in range(1,7)]
hus_occ_dummies.columns


# In[31]:

X = df.drop(['occupation','occupation_husb','Had_Affair'],axis = 1)
X.head()


# In[32]:

dummies = pd.concat([occ_dummies,hus_occ_dummies],axis = 1)
dummies.head()


# In[33]:

X = pd.concat([X,dummies],axis = 1)
X.head()


# In[34]:

Y = df['Had_Affair']


# In[35]:

Y.head()


# In[36]:

X = X.drop(['occ1','hocc1','affairs'],axis =1)


# In[37]:

X.head()


# In[38]:

type(Y)


# In[39]:

Y = np.ravel(Y)


# In[40]:

Y[:10]


# In[41]:

log_reg = LogisticRegression()


# In[42]:

log_reg.fit(X,Y)


# In[43]:

log_reg.score(X,Y)


# In[44]:

Y.mean()


# In[45]:

coeff_df = DataFrame(list(zip(X.columns,list(log_reg.coef_[0]))))
coeff_df


# In[54]:

X_trn,X_tst,Y_trn,Y_tst = train_test_split(X,Y,test_size = 0.25)


# In[55]:

X_trn.shape


# In[56]:

X_tst.shape


# In[57]:

Y_trn.shape


# In[58]:

Y_tst.shape


# In[59]:

log_reg2 = LogisticRegression()


# In[60]:

log_reg2.fit(X_trn,Y_trn)


# In[61]:

Y_pred = log_reg2.predict(X_tst)


# In[64]:

np.sum(Y_pred == Y_tst)/(len(Y_tst))


# In[67]:

log_reg2.score(X_tst,Y_tst)


# In[68]:

metrics.accuracy_score(Y_tst,Y_pred)


# In[ ]:



