
# coding: utf-8

# In[3]:

import numpy as np
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')
sns.set_style('whitegrid')


# In[5]:

from sklearn import linear_model


# In[6]:

from sklearn.datasets import load_iris


# In[7]:

iris = load_iris()


# In[11]:

X = iris.data


# In[14]:

Y = iris.target


# In[15]:

X.shape


# In[16]:

Y.shape


# In[17]:

print(iris.DESCR)


# In[18]:

iris_df =DataFrame(X,columns = ['Sepal Length','Sepal Width','Petal Length','Petal Width'])


# In[19]:

iris_df.head()


# In[21]:

iris_target = DataFrame(Y,columns =['Species'])


# In[22]:

iris_target.head()


# In[24]:

a = lambda n: {1:'A',2:'B',3:'C'}[n]


# In[28]:

a(2)


# In[ ]:




# In[29]:

iris_target['Species'] = iris_target['Species'].apply(lambda num:{0:'Setosa',1:'Versicolor',2:'Virginica'}[num])


# In[30]:

iris_target.head()


# In[31]:

iris_target.tail()


# In[34]:

iris = pd.concat([iris_df,iris_target],axis  = 1)
iris.head()


# In[35]:

sns.pairplot(iris,hue='Species',size=2)


# In[39]:

sns.factorplot('Petal Length',data=iris,hue='Species',size = 10, kind = 'count')


# In[ ]:



