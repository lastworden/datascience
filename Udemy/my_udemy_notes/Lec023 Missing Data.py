
# coding: utf-8

# In[2]:

import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# In[5]:

ser1 = Series(['One','Two',np.nan,'Three'])
ser1


# In[7]:

ser1.isnull()


# In[8]:

ser1.dropna()


# In[10]:

df1 = DataFrame([[1,2,3],[np.nan,4,5],[7,np.nan,9],[np.nan,np.nan,np.nan]])
df1


# In[11]:

df1.isnull()


# In[13]:

clean_df = df1.dropna()
clean_df


# In[ ]:




# In[14]:

df1.dropna(how = 'all')


# In[17]:

df1.dropna(axis = 1)


# In[18]:

df1.dropna(axis = 1,how = 'all')


# In[19]:

df2 = DataFrame(np.)


# In[36]:

npn = np.nan
df2 = DataFrame([[1,2,3,npn],[2,npn,5,6],[npn,7,npn,9],[npn,npn,npn,npn]])
df2


# In[37]:

df2.dropna(thresh = 2)


# In[40]:

df2.dropna(thresh = 3,axis = 1)


# In[41]:

df2


# In[44]:

df2.fillna('1')


# In[45]:

df2.fillna('NotApplicable') #NotApplicable is not keyword


# In[46]:

df2.fillna({0:10,1:11,2:22,3:33})


# In[47]:

df2


# In[48]:

df2.fillna(0,inplace = True)


# In[49]:

df2


# In[ ]:



