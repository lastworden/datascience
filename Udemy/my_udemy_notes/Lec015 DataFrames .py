
# coding: utf-8

# In[12]:

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[16]:

import webbrowser
website = 'http://en.wikipedia.org/wiki/NFL_win-loss_records'
webbrowser.open(website)


# In[17]:

nfl_frame = pd.read_clipboard()


# In[18]:

nfl_frame


# In[19]:

nfl_frame.columns


# In[20]:

nfl_frame.Conference


# In[22]:

nfl_frame['Team']


# In[25]:

DataFrame(nfl_frame,columns = [ 'Team', 'Won', 'Lost', 'Tied*'])


# In[27]:

DataFrame(nfl_frame,columns = [ 'Team', 'Won', 'Lost', 'Tied*','Stadium'])


# In[28]:

nfl_frame.head(3)


# In[29]:

nfl_frame.tail(2)


# In[30]:

nfl_frame.ix[1]


# In[31]:

nfl_frame


# In[32]:

nfl_frame['Stadium'] = "Levi's Stadium"


# In[33]:

nfl_frame


# In[34]:

nfl_frame['Stadium'] = np.arange(6)


# In[35]:

nfl_frame


# In[39]:

nfl_frame['Stadium'] = ['1','2','3','4','5','6']
nfl_frame


# In[40]:

stadiums = Series(['Levis Stadium','Eaden Gargens','MCG'],index = [1,2,5])
stadiums


# In[41]:

nfl_frame['Stadium'] = stadiums
nfl_frame


# In[42]:

del nfl_frame['Stadium']


# In[43]:

nfl_frame


# In[44]:

city_dict = {'City':['Mumbai','Cochin','Hyderabd'],'Population':[5000000,2500000,3000000]}
city_dict


# In[45]:

city_frame = DataFrame(city_dict)
city_frame


# In[46]:

#For full list of ways to create DataFrames from various sources go to teh documentation for pandas:
website = 'http://pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.html'
website = 'http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html'
webbrowser.open(website)


# In[11]:

nfl_frame


# In[ ]:



