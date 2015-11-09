
# coding: utf-8

# In[5]:

import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[6]:

points = np.arange(-5,5,0.01)
points


# In[7]:

dx, dy = np.meshgrid(points,points)


# In[8]:

dx


# In[9]:

dy


# In[10]:

dx.shape


# In[11]:

dy.shape


# In[19]:

z = np.sin(dx)+np.sin(dy)
z


# In[32]:

plt.imshow(z)
plt.colorbar()
plt.title('Plot for cos(x)+cos(y)')


# In[30]:

y = np.cos(dx)+np.cos(dy)


# In[31]:

plt.imshow(y)
plt.colorbar()
plt.title('Plot for cos(x)+cos(y)')


# In[33]:

A = np.array([1,2,3,4])
A


# In[34]:

B = A.copy()*100
B


# In[36]:

C = np.array([True,False,True,False])


# In[38]:

Res = [(a if c else b) for a,b,c in zip(A,B,C)]
Res


# In[42]:

str(zip(A,B,C))


# In[44]:

res2 = np.where(C,A,B)
res2


# In[45]:

for a,b,c in zip(A,B,C):
    print(a,b,c)


# In[ ]:



