
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# In[2]:

from sklearn.datasets import load_boston


# In[3]:

boston = load_boston()


# In[4]:

print(boston.DESCR)


# In[5]:

boston.data.shape


# In[6]:

boston.target.shape


# In[7]:

boston_df = DataFrame(boston.data)


# In[8]:

boston_df.head()


# In[9]:

boston_df.columns = boston.feature_names


# In[10]:

boston_df.head()


# In[11]:

boston_df['target'] = boston.target


# In[12]:

boston_df.head()


# In[13]:

X = boston.data


# In[14]:

Y = boston.target


# In[15]:

m,d = X.shape


# In[16]:

one_arr = np.ones((m,1))
X = np.hstack((X,one_arr))


# In[17]:

X_sym = X.T.dot(X)


# In[18]:

X_sym.shape


# In[19]:

np.linalg.inv(np.array([[1,0,0],
                    [0,1,0],
                    [0,0,1]]))


# In[20]:

X_sym_inv = np.linalg.inv(X_sym)


# In[21]:

X_sym_inv.shape


# In[22]:

Y.shape


# In[23]:

X_trn_Y = X.T.dot(Y)


# In[24]:

W = X_sym_inv.dot(X_trn_Y)


# In[25]:

W.shape


# In[57]:

W


# In[59]:

err_vec = X.dot(W)-Y


# In[62]:

rmse = np.sqrt(np.mean(err_vec**2))


# In[63]:

rmse


# In[27]:

t = np.arange(100)+1


# In[28]:

ind = np.random.choice(t,10,replace=False)
ind


# In[29]:

t[ind]


# In[30]:

np.random.permutation(t)


# In[31]:

t


# In[32]:

X_rand = np.random.permutation(X)


# In[33]:

trn_factor = 0.8


# ### Linear Regression with Test and Train split

# In[43]:

from sklearn import cross_validation


# In[44]:

X_trn,X_tst,Y_trn,Y_tst = cross_validation.train_test_split(X,Y,test_size = 0.2)


# In[46]:

X_trn.shape


# In[47]:

Y_tst.shape


# In[69]:

X.shape


# In[229]:

def fit_reg_model(X,Y,C):
    X_sym = X.T.dot(X)
    LI = C*np.eye(X_sym.shape[0])
    W = np.linalg.inv(X_sym+LI).dot(X.T.dot(Y))
    err_vec = X.dot(W)-Y
    rmse = np.sqrt(np.mean(err_vec**2))
    return [W,rmse]


# In[117]:

def get_test_error(W,X,Y):
    err_vec = X.dot(W)-Y
    rmse = np.sqrt(np.mean(err_vec**2))
    return rmse


# In[215]:

C = 0.1


# In[216]:

X_trn_sym = X_trn.T.dot(X_trn)


# In[217]:

X_trn_sym.shape


# In[218]:

CI = C*np.eye(X_trn_sym.shape[0])


# In[219]:

CI.shape


# In[220]:

W = np.linalg.inv(X_trn_sym+CI).dot(X_trn.T.dot(Y_trn))


# In[221]:

W


# In[222]:

trn_err_vec = X_trn.dot(W)-Y_trn


# In[223]:

rmse_trn = np.sqrt(np.mean(trn_err_vec**2))


# In[224]:

rmse_trn


# In[235]:

W,rmse_trn = fit_reg_model(X_trn,Y_trn,0.1)


# In[236]:

W


# In[237]:

rmse_trn


# In[238]:

get_test_error(W,X_tst,Y_tst)


# In[242]:

W,rmse_trn = fit_reg_model(X_trn,Y_trn,1)


# In[243]:

W


# In[244]:

rmse_trn


# In[245]:

get_test_error(W,X_tst,Y_tst)


# In[256]:

W,rmse_trn = fit_reg_model(X_trn,Y_trn,0.01)


# In[257]:

W


# In[258]:

rmse_trn


# In[259]:

get_test_error(W,X_tst,Y_tst)


# In[ ]:



