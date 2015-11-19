
# coding: utf-8

# In[1]:

import numpy as np
from pandas import Series, DataFrame
import pandas as pd


# In[3]:

# Heres an example of what a JSON (JavaScript Object Notation) looks like:
json_obj = """
{   "zoo_animal": "Lion",
    "food": ["Meat", "Veggies", "Honey"],
    "fur": "Golden",
    "clothes": null, 
    "diet": [{"zoo_animal": "Gazelle", "food":"grass", "fur": "Brown"}]
}
"""


# In[4]:

#Let import json module
import json

#Lets load json data
data = json.loads(json_obj)


# In[5]:

#Show
data


# In[6]:

#WE can also convert back to JSON
json.dumps(data)


# In[7]:

#We can simply open JSON data after loading with a DataFrame
dframe = DataFrame(data['diet'])


# In[8]:

#Show
dframe


# In[9]:

# Theres lost of custom selection you can do, based on what you do or dont want in your DataFrame (you can specify columns..etc)


# In[ ]:

#Next up, XML and HTML file format with python!

