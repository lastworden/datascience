
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[2]:

df1 = pd.read_csv('lec25.csv')
df1


# In[3]:

df1 = pd.read_csv('lec25.csv',header = None)
df1


# In[4]:

df1 = pd.read_table('lec25.csv',sep=',',header = None)
df1


# In[5]:

pd.read_csv('lec25.csv',header = None, nrows =2)


# In[6]:

df1.to_csv('lec25_write_csv.csv')


# In[7]:

import sys


# In[9]:

df1.to_csv(sys.stdout)


# In[11]:

df1.to_csv(sys.stdout, sep = '|', header = None,index = None)


# In[13]:

df1.to_csv(sys.stdout, sep = '|', header = None,index = None,columns = [0,1,2])


# In[14]:

df1.to_csv(sys.stdout, sep = '|',columns = [0,1,2])


# In[ ]:

#You should also check out pythons built-in csv reader and writer for more info:
# https://docs.python.org/2/library/csv.html

