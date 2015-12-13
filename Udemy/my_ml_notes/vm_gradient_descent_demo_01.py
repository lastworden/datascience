
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')


# In[2]:

def obj_fun(x):
    return x**2-10*x+25


# In[3]:

def obj_grad(x):
    return 2*x-10


# In[4]:

X =np.linspace(1, 9, num=500)


# In[5]:

Y = np.array([obj_fun(i) for i in X])


# In[6]:

plt.plot(X,Y)


# In[7]:

from mpl_toolkits.mplot3d import Axes3D


# In[31]:

def gs1d(f,g,x,alpha=0.1,niter=2000,eps=0.001):
    
    f_val = f(x)
    
    grad = g(x)
    x = x-alpha*grad
    
    i =1
    
    while(i<niter and np.abs(f_val-f(x))>eps):
        print("iter : %s x:%f grad:%f fval : %f"%(i,x,grad,f(x)))
        f_val = f(x)
        grad = g(x)
        x = x-alpha*grad
        i+=1
        
    print("i:%d"%i)
    return x
    


# In[32]:

x1 = gs1d(obj_fun,obj_grad,0.1,niter=100)

x1


# In[30]:

np.abs(-5)


# In[33]:

x2 = gs1d(obj_fun,obj_grad,50,niter=100)

x2


# In[64]:

def obj_fun2d(x,y):
    return x**2+y**2-10*x-10*y+50


# In[65]:

X1,Y1 = np.meshgrid(X,X)


# In[72]:

Z = np.array([obj_fun2d(x,y) for x,y in zip(np.ravel(X1),np.ravel(Y1))])


# In[73]:

Z.shape


# link : [http://stackoverflow.com/questions/9170838/surface-plots-in-matplotlib]

# In[71]:

from mpl_toolkits.mplot3d import Axes3D


# In[77]:

Z1 = Z.reshape(X1.shape)


# In[86]:


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X1, Y1, Z1)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')


# In[80]:

5


# In[ ]:



