
# coding: utf-8

# #### Demo for REGEX

# In[15]:

import re


# . This element matches any character except newline \n  
# \D This matches any non-digit character; this is equivalent to the class [^0-9].  
# \d This matches any decimal digit; this is equivalent to the class [0-9]  
# \s This matches any whitespace character; this is equivalent to the class [⇢\t\n\r\f\v]  
# \S This matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v]  
# \w This matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_]  
# \W This matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_]  

# In[27]:


s = input('Enter the string :')
print (s.__repr__())


# In[28]:

p = re.compile('(.*)=(.*)') #re.compile('(*)=(*)')
m = p.search(s)
print (m.group(1),m.group(2),)


# In[29]:

p = re.compile(r'hello\ngood')

st = 'hello\ngood'
print(st)
m = p.search(st)
if st:
    print(m.group(0))
else:
    print('not match')


# In[38]:

print('The search result for string {str} using the regex : {reg} is {res}'.format(str = '123',reg = 'wer',res = '234'))


# In[70]:

def outer_fun(func):
    def inner_fun(regexp, str, result):
        func('The search result for string {str} using the regex :{reg} is {res}'.format(str = repr(str),reg = regexp,res = result))
    
    return inner_fun


# In[71]:

print_reg = outer_fun(print)


# In[72]:

regexp = r'.'
st = '\n'
p = re.compile(regexp)
m = p.search(st)
print_reg(regexp,st,m)


# In[50]:

print (repr('\n'))


# In[ ]:



