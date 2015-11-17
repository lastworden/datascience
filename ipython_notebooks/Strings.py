
# coding: utf-8

# In[18]:

import string as s

s1 = " hello my dear math \t"
s1


# In[19]:

s1.isalpha()


# In[44]:

'abc'.isalpha()


# In[20]:

s1.isdigit()


# In[46]:

'123'.isdigit()


# In[47]:

'\t   \n   \r'.isspace()


# In[33]:

s1.isspace()


# In[21]:

s1.strip()


# In[22]:

s1.rstrip()


# In[23]:

s1.lstrip()


# In[24]:

print(s1)


# In[26]:

s2 = 'hello how are you\n'
s2


# In[48]:

print(s2)


# In[29]:

s2.startswith('he')


# In[30]:

s2.startswith('Hel')


# In[35]:

s2.endswith('you')


# In[36]:

s2.endswith('ou\n')


# In[37]:

s2.upper()


# In[38]:

s2.lower()


# In[39]:

s2.find('are')


# In[40]:

s2.find('arey')


# In[41]:

s2.replace('you','me')


# In[42]:

s2.split(' ')


# In[43]:

s3 = '|'
s3.join(['a','b','c','d'])


# 1  str.isalpha()
# 2  str.isdigit()
# 3  str.isspace()
# 4  str.strip(), lstrip(), rstrip()
# 5  str.startswith(str2)
# 6  str.endswith(str2)
# 7  str.upper()
# 8  str.lower()
# 9  str.find(str1)
# 10 str.replace(str1,str2)
# 11 str.split('str1') 
# 12 str.join(list)
# 
# 
#     s.lower(), s.upper() -- returns the lowercase or uppercase version of the string
#     s.strip() -- returns a string with whitespace removed from the start and end
#     s.isalpha()/s.isdigit()/s.isspace()... -- tests if all the string chars are in the various character classes
#     s.startswith('other'), s.endswith('other') -- tests if the string starts or ends with the given other string
#     s.find('other') -- searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found
#     s.replace('old', 'new') -- returns a string where all occurrences of 'old' have been replaced by 'new'
#     s.split('delim') -- returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
#     s.join(list) -- opposite of split(), joins the elements in the given list together using the string as the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc
# 
