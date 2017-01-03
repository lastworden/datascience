
# coding: utf-8

# https://courses.edx.org/courses/course-v1:Microsoft+DAT210x+4T2016/courseware/12621a4064aa4d92874a9d8a953734c5/773fbbcfe42c47fc85a5da26001a32f3/

# In[1]:

pwd


# In[2]:

import pandas as pd


# In[4]:

df = pd.read_csv("Datasets/tutorial.csv")


# In[7]:

df


# In[8]:

df.columns

Row and Column Indexing

A dataframe is essentially one or more series which have been 'stitched' together into a new data type. Pandas exposes many equivalent methods for slicing out those underlying series. You can slice by location, the way you would normally index into a regular Python list. You can slice by label, the way you would normally index into a Python dictionary. And like NumPy arrays, you can also index by boolean masks:

>>> df.col0
>>> df['col0']
>>> df[['col0']]
>>> df.loc[:, 'col0']
>>> df.loc[:, ['col0']]
>>> df.iloc[:, 0]
>>> df.iloc[:, [0]]
>>> df.ix[:, 0]

row0  -0.722876
row1   1.160396
row2  -1.062870

row3   0.437078

Name: col0, dtype: float64

Assuming it is labeled col0, any of the above commands will return the first series, e.g. column, in the dataframe. The first three statements of selection by column name, are compact and easily discernible. These are the preferred syntaxes for use while you are learning, doing interactive work and prototyping. The difference between df['col0'] and df[['col0']] is that you can pass in additional comma separated column names with the latter to do multivariate selection.

Once you're ready to move to a production environment, Pandas recommends you use either of the last five data access methods, which are more optimized. The .loc[] selector is used to select by string index label, .iloc[] to select by integer index position, and .ix[] is used whenever you want to use a hybrid approach of either.

All code in this course will use either the df.col0 or df[['col0', ...]] data access syntaxes for maximum clarity.

You also can use any of the .loc, .iloc or .ix methods to do selection by row, noting that the expected order is [row_indexer, column_indexer]:

>>> df[0:1]
>>> df.iloc[0:1, :]

          col0      col1      col2      col3
row0 -0.722876 -1.330682  1.309208  0.232378

Don't be fooled! .loc and .iloc behave a bit differently in that iloc expects numeric values only. Another difference is that loc is inclusive in its range selection, so .loc[0:1. :] would return the 0th and 1st rows, whereas .iloc[0:1, :] would only return the 0th row!

Boolean Indexing

Your series can also be indexed with a boolean series—a series with the same dimensions as the one you are selecting from, but with every value either being set to True or False. You can create a new boolean series either by manually specifying the values, or by using a conditional:

>>> df.col0 < 0

0     True
1    False
2     True
3    False
Name: col0, dtype: bool

To index with your boolean series, simply feed it back into your regular series with using the [] bracket-selection syntax. The result is a new series that once again has the same dimensions, however only values corresponding to True values in the boolean series are returned:

>>> df[ df.col0 < 0 ]

       col0      col1      col2      col3
0 -0.722876 -1.330682  1.309208  0.232378
2 -1.062870 -0.503704 -0.238536 -1.417937

 

If you require even finer grain control of what gets selected, you can further combine multiple boolean indexing conditionals together using the bitwise logical operators "|" and "&":

>>> df[ (df.col0<0) | (df.col1<0) ]

       col0      col1      col2      col3
0 -0.722876 -1.330682  1.309208  0.232378
1  1.160396 -0.730879  0.677368  1.044722
2 -1.062870 -0.503704 -0.238536 -1.417937

This is a bit counterintuitive, as most people initially assume that Pandas would support the regular, Python boolean operators "or" and "and". The reason regular Python boolean operators cannot be used to combine Pandas boolean conditionals is because doing so causes an ambiguity. You can interpret the following incorrect statement in two ways: (df.col0<0) or (df.col1<0):

    If evaluating the statement df.col0<0 or evaluating the statement df.col1<0 results in anything besides the None, 0, or False, then select all records.
    For each row in the dataset, if either col0<0 or col1<0, then select that entire row.

Option 2 is the desired functionality, but to avoid this ambiguity entirely, Pandas overloads bitwise operators on it's dataframe and series objects. Be sure to encapsulate each conditional in parenthesis to make this work.

Writing to a Slice

Something handy that you can do with a dataframe or series is write into a slice:

>>> df[df < 0] = -100
>>> df

            col0       col1        col2        col3
row0 -100.000000 -100.00000    1.309208    0.232378
row1    1.160396 -100.00000    0.677368    1.044722
row2 -100.000000 -100.00000 -100.000000 -100.000000
row3    0.437078    0.36264 -100.000000 -100.000000

Take precaution while doing this, as you may encounter issues with non-homogeneous dataframes. It is far safer, and generally makes more sense, to do this sort of operation on a per column basis rather than across your entire dataframe.
# In[9]:

df.col0


# In[10]:

df['col1']


# In[12]:

df[['col1']]


# In[14]:

df.loc[:,'col1']


# In[18]:

df.iloc[:,0]


# In[22]:

df.iloc[:,[0,2]]


# In[26]:

df.ix[:,[2,1]]


# In[31]:

df.ix[1:2,['col2']]


# In[32]:

help(pd.DataFrame.iloc)


# In[ ]:



