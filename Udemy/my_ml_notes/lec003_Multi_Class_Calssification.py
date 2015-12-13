
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')
sns.set_style('whitegrid')


# In[2]:

from sklearn import linear_model


# In[3]:

from sklearn.datasets import load_iris


# In[4]:

iris = load_iris()


# In[5]:

X = iris.data


# In[6]:

Y = iris.target


# In[7]:

X.shape


# In[8]:

Y.shape


# In[9]:

print(iris.DESCR)


# In[10]:

iris_df =DataFrame(X,columns = ['Sepal Length','Sepal Width','Petal Length','Petal Width'])


# In[11]:

iris_df.head()


# In[12]:

iris_target = DataFrame(Y,columns =['Species'])


# In[13]:

iris_target.head()


# In[14]:

a = lambda n: {1:'A',2:'B',3:'C'}[n]


# In[15]:

a(2)


# In[ ]:




# In[16]:

iris_target['Species'] = iris_target['Species'].apply(lambda num:{0:'Setosa',1:'Versicolor',2:'Virginica'}[num])


# In[17]:

iris_target.head()


# In[18]:

iris_target.tail()


# In[19]:

iris = pd.concat([iris_df,iris_target],axis  = 1)
iris.head()


# In[20]:

sns.pairplot(iris,hue='Species',size=2)


# In[21]:

sns.factorplot('Petal Length',data=iris,hue='Species',size = 10, kind = 'count')


# In[22]:

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split


# In[23]:

X_trn,X_tst,Y_trn,Y_tst = train_test_split(X,Y,test_size = 0.4,random_state=3)


# In[24]:

X_trn.shape


# In[25]:

X.shape


# In[26]:

lreg = LogisticRegression()


# In[27]:

lreg.fit(X_trn,Y_trn)


# In[28]:

from sklearn import metrics


# In[29]:

Y_pred = lreg.predict(X_tst)


# In[30]:

Y_pred


# In[ ]:




# In[31]:

res = np.sum(Y_pred==Y_tst)/len(Y_pred)


# In[32]:

res


# In[35]:

metrics.accuracy_score(Y_pred,Y_tst)


# In[34]:

from sklearn.neighbors import KNeighborsClassifier


# In[ ]:




# In[ ]:



