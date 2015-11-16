
# coding: utf-8

# In[2]:

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[6]:

obj = Series([3,6,9,12])
obj


# In[7]:

obj.values


# In[8]:

obj.index


# In[9]:

ww2_cas = Series([8700000,4300000,3000000,2100000,400000], index = ['USSR','Germany','China','Japan','USA'])
ww2_cas


# In[10]:

ww2_cas['USSR']


# In[11]:

ww2_cas[ww2_cas>4000000]


# In[15]:

'USSR' in ww2_cas


# In[16]:

'India' in ww2_cas


# Series behaves like an ordered dictionary. So we can even convert them to dictionary

# In[18]:

ww2_dict = dict(ww2_cas)
ww2_dict


# In[19]:

ww2_cas.to_dict()


# In[20]:

ww2_series= Series(ww2_dict)
ww2_series


# In[21]:

countries = ['USSR','USA','India']


# In[22]:

obj2 = Series(ww2_dict,index = countries)
obj2


# In[25]:

dict(zip(['1','b','c'],[1,2,3]))


# In[26]:

dict(a=1,b=2,c=88)


# In[28]:

dict({1:2,2:3,3:4})


# In[29]:

pd.isnull(obj2)


# In[30]:

pd.notnull(obj2)


# In[31]:

obj2


# In[32]:

ww2_series


# In[34]:

ww2_series+obj2


# In[37]:

obj2.name = 'world war 2 casualties'
obj2


# In[39]:

obj2.index.name = 'Countries'
obj2

