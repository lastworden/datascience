
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[3]:

df1 = DataFrame({'key':['X','Z','Y','Z','X','X'], 'ds1':np.arange(6)})
df1


# In[5]:

df2 = DataFrame({'key':['Q','Y','Z'],'ds2':[1,2,3]})
df2


# In[6]:

pd.merge(df1,df2)


# In[7]:

pd.merge(df1,df2, on ='key')


# In[9]:

pd.merge(df1,df2, on ='key', how = 'left')


# In[10]:

pd.merge(df1,df2, on ='key', how = 'right')


# In[11]:

pd.merge(df1,df2, on ='key', how = 'outer')


# In[20]:

df3 = DataFrame({'key':['X','X','X','Y','Z','Z'],'ds3':range(6)})
df3


# In[24]:

df4 = DataFrame({'key':['Y','Y','X','X','Z'],'ds4':range(5)})
df4


# In[25]:

pd.merge(df3,df4).shape


# In[26]:

pd.merge(df3,df4)


# In[29]:

df_left = DataFrame({'key1':['SF','SF','LA'],
                     'key2':['one','two','one'],
                     'left_data':[10,20,30]})

df_right = DataFrame({'key1':['SF','SF','LA','LA'],
                      'key2':['one','one','one','two'],
                      'right_data':[40,50,60,70]})


# In[30]:

df_left


# In[31]:

df_right


# In[32]:

pd.merge(df_left,df_right,on=['key1','key2'])


# In[33]:

pd.merge(df_left,df_right,on=['key1','key2'],how='outer')


# In[34]:

pd.merge(df_left,df_right,on='key1')


# In[35]:

pd.merge(df_left,df_right,on='key1',suffixes = ['_left','_right'])


# In[36]:

# For more info on merge parameters check out:
url = 'http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.merge.html'
import webbrowser as w
w.open(url)
# Next we'll learn how to merge on Index!


# In[ ]:



