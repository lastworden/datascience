
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

#pip install xlrd
#pip install openpyxl


# In[3]:

xlfile = pd.ExcelFile('lec_28_test.xlsx')


# In[5]:

df1 = xlfile.parse('Sheet1')


# In[6]:

df1


# In[ ]:

#

