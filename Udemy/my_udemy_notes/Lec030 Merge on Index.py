
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from pandas import Series,DataFrame


# In[7]:

df_left = DataFrame({'key':['X','Y','Z','X','Y'],'data':range(5)})
df_left


# In[8]:

df_right = DataFrame({'group_data':[10,20]},index = ['X','Y'])
df_right


# In[9]:

pd.merge(df_left,df_right,left_on = 'key',right_index = True)


# In[10]:

pd.merge(df_left,df_right,left_on = 'key',right_index = True, how = 'left')


# In[11]:

pd.merge(df_left,df_right,left_on = 'key',right_index = True, how = 'outer')


# In[16]:

df_left_hr = DataFrame({'key1':['SF','SF','SF','LA','LA'],
                        'key2':[10,20,30,20,30],
                        'data_Set':np.arange(5)})
df_left_hr


# In[19]:

df_right_hr = DataFrame(np.arange(10).reshape((5,2)),
                        index = [['LA','LA','SF','SF','SF'],
                                 [20,10,10,10,20]],
                        columns = ['col1','col2'])
df_right_hr


# In[20]:

pd.merge(df_left_hr,df_right_hr,left_on = ['key1','key2'],right_index = True)


# In[21]:

df_left_hr


# In[22]:

df_left


# In[23]:

df_right


# In[24]:

df_left.join(df_right)

