
# coding: utf-8

# In[2]:

import numpy as np
from pandas import Series,DataFrame
import pandas as pd


# In[3]:

# Can open csv files as a dataframe
dframe = pd.read_csv('lec25.csv')

#Show
dframe


# In[4]:

# Can also use read_table with ',' as a delimiter
dframe = pd.read_table('lec25.csv',sep=',')

#Show
dframe


# In[5]:

dframe


# In[6]:

#If we dont want the header to be the first row
dframe = pd.read_csv('lec25.csv',header=None)

#Show
dframe


# In[7]:

# We can also indicate a particular number of rows to be read
pd.read_csv('lec25.csv',header=None,nrows=2)


# In[8]:

# Let's see dframe again
dframe


# In[10]:

# Now let's see how we can write DataFrames out to text files
dframe.to_csv('mytextdata_out.csv')

#You'll see this file where you're ipython Notebooks are saved (Usually under my documents)


# In[14]:

#  We can also use other delimiters

#we'll import sys to see the output
import sys 

#Use sys.stdout to see the output directly and not save it
dframe.to_csv(sys.stdout,sep='_')


# In[15]:

# Just to make sure we understand the delimiter
dframe.to_csv(sys.stdout,sep='?')


# In[17]:

#We can also choose to write only a specific subset of columns
dframe.to_csv(sys.stdout,columns=[0,1,2])


# In[18]:

#You should also check out pythons built-in csv reader and writer for more info:
# https://docs.python.org/2/library/csv.html


# In[ ]:

#Next we'll learn about reading JSON data!

