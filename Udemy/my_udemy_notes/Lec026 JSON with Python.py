
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# In[2]:

# Heres an example of what a JSON (JavaScript Object Notation) looks like:
json_obj = """
{   "zoo_animal": "Lion",
    "food": ["Meat", "Veggies", "Honey"],
    "fur": "Golden",
    "clothes": null, 
    "diet": [{"zoo_animal": "Gazelle", "food":"grass", "fur": "Brown"}]
}
"""


# In[3]:

json_obj


# In[4]:

import json


# In[7]:

dat = json.loads(json_obj)


# In[8]:

dat


# In[9]:

json.dumps(dat)


# In[11]:

df = DataFrame(dat['diet'])


# In[12]:

df


# In[ ]:



