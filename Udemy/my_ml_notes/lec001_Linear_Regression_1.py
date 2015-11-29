
# coding: utf-8

# In[2]:

import numpy as np
import pandas as pd
from pandas import Series,DataFrame


# In[4]:

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().magic('matplotlib inline')


# In[5]:

from sklearn.datasets import load_boston


# In[6]:

boston = load_boston()


# In[7]:

type(boston)


# In[8]:

print(boston.DESCR)


# In[9]:

plt.hist(boston.target, bins = 50)
plt.xlabel('Prices in $1000s')
plt.ylabel('Number of Houses')


# In[10]:

plt.scatter(boston.data[:,5],boston.target)
plt.xlabel('Number of Rooms')
plt.ylabel('Prices in $1000s')


# In[11]:

boston_df = DataFrame(boston.data)


# In[12]:

boston_df.columns = boston.feature_names
boston_df.head()


# In[13]:

boston_df['Price'] = boston.target
boston_df.head()


# In[14]:

sns.lmplot('RM','Price',data = boston_df)


# In[20]:

a=input("Enter a value:")


# In[21]:

a


# In[22]:

sns.lmplot('CRIM','Price',data = boston_df)


# In[23]:

X = boston_df.RM
X.head()




# In[24]:

X.shape


# In[25]:

X = np.vstack(boston_df['RM'])
X.shape


# In[26]:

X[:5]


# In[27]:

Y = boston_df['Price']


# In[28]:

X = np.array([[i,1] for i in X])


# In[29]:

X


# In[30]:

m,c = np.linalg.lstsq(X,Y)[0]


# In[31]:

print(m,c)


# In[32]:

plt.plot(boston_df['RM'],Y,'o')
x = boston_df['RM']
plt.plot(x,m*x+c,'r',label = 'Best Fit Line')
plt.xlabel('Number of Rooms')
plt.ylabel('Prices in $1000s')


# Great! We've just completed a single variable regression using the least squares method with Python! Let's see if we can find the error in our fitted line. Checking out the documentation [here](http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.lstsq.html), we see that the resulting array has the total squared error. For each element, it checks the the difference between the line and the true value (our original D value), squares it, and returns the sum of all these. This was the summed D^2 value we discussed earlier. 
# 
# It's probably easier to understand the root mean squared error, which is similar to the standard deviation. In this case, to find the root mean square error we divide by the number of elements and then take the square root. There is also an issue of bias and an unbiased regression, but we'll delve into those topics later.
# 
# For now let's see how we can get the root mean squared error of the line we just fitted.

# In[37]:

result = np.linalg.lstsq(X,Y)


# In[38]:

err = result[1]


# In[40]:

err


# computer error manually

# In[44]:

y1 = m*x + c
y1


# In[47]:

y = boston_df['Price']
y


# In[48]:

diff = y1-y


# In[49]:

manual_err = diff.dot(diff)
manual_err


# In[53]:

diff.shape


# In[55]:

np.sqrt(5)


# In[57]:

rmse = np.sqrt(manual_err/len(diff))
rmse


# Since the root mean square error (RMSE) corresponds approximately to the standard deviation we can now say that the price of a house won't vary more than 2 times the RMSE 95% of the time. Note: Review the Normal Distribution Appendix lecture if this doesn't make sense to you or check out this [link](http://en.wikipedia.org/wiki/68%E2%80%9395%E2%80%9399.7_rule).
# 
# Thus we can reasonably expect a house price to be within $13,200 of our line fit.

# ### Step 6: Using scikit learn to implement a multivariate regression

# Now, we'll keep moving along with using scikit learn to do a multi variable regression. This will be a similar apporach to the above example, but sci kit learn will be able to take into account more than just a single data variable effecting the target!
# 
# We'll start by importing the [linear regression library](http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) from the sklearn module.
# 
# The sklearn.linear_model.LinearRegression class is an estimator. Estimators predict a value based on the observed data. In scikit-learn, all estimators implement the fit() and predict() methods. The former method is used to learn the parameters of a model, and the latter method is used to predict the value of a response variable for an explanatory variable using the learned parameters. It is easy to experiment with different models using scikit-learn because all estimators implement the fit and predict methods.

# In[60]:

import sklearn
from sklearn.linear_model import LinearRegression


# In[61]:

lreg = LinearRegression()


# In[62]:

X_multi = boston_df.drop('Price',axis=1)


# In[63]:

X_multi.head()


# In[65]:

Y_target = boston_df['Price']
Y_target.head()


# In[66]:

lreg.fit(X_multi,Y_target)


# In[67]:

print('Intercept : ',lreg.intercept_)


# In[68]:

print('#Coefficients : ',len(lreg.coef_))


# In[73]:

coeff_df = DataFrame(boston_df.columns)
coeff_df


# In[74]:

coeff_df.columns = ['Features']
coeff_df


# In[75]:

coeff_df['Coefficient_Estimate'] = Series(lreg.coef_)
coeff_df


# In[81]:

X_trn,X_tst,Y_trn,Y_tst = sklearn.cross_validation.train_test_split(X,Y)


# In[82]:

print(X_trn.shape,X_tst.shape,Y_trn.shape,Y_tst.shape)


# In[83]:

127/(379+127)


# In[109]:

X_trn,X_tst,Y_trn,Y_tst = sklearn.cross_validation.train_test_split(X_multi,Y,test_size = 0.2)


# In[110]:

print(X_trn.shape,X_tst.shape,Y_trn.shape,Y_tst.shape)


# In[111]:

lreg1 = LinearRegression()


# In[112]:

lreg1.fit(X_trn,Y_trn)


# In[113]:

Y_pred_tst = lreg1.predict(X_tst)
Y_pred_trn = lreg1.predict(X_trn)
err_tst_vec = Y_pred_tst - Y_tst
err_trn_vec = Y_pred_trn - Y_trn


# In[114]:

mse_tst = err_tst_vec.dot(err_tst_vec)/len(err_tst_vec)
mse_trn = err_trn_vec.dot(err_trn_vec)/len(err_trn_vec)


# In[115]:

mse_trn


# In[116]:

mse_tst


# In[117]:

rmse_tst = np.sqrt(np.mean(err_tst_vec*err_tst_vec))
rmse_trn = np.sqrt(np.sum(err_trn_vec*err_trn_vec)/len(err_trn_vec))

print(rmse_trn,rmse_tst)


# ### Step 9 : Residual Plots

# In regression analysis, the difference between the observed value of the dependent variable (y) and the predicted value (ŷ) is called the residual (e). Each data point has one residual, so that:
# 
# $$Residual = Observed\:value - Predicted\:value $$

# You can think of these residuals in the same way as the D value we discussed earlier, in this case however, there were multiple data points considered.

# A residual plot is a graph that shows the residuals on the vertical axis and the independent variable on the horizontal axis. If the points in a residual plot are randomly dispersed around the horizontal axis, a linear regression model is appropriate for the data; otherwise, a non-linear model is more appropriate.
# 
# Residual plots are a good way to visualize the errors in your data.  If you have done a good job then your data should be randomly scattered around line zero. If there is some strucutre or pattern, that means your model is not capturing some thing. There could be an interaction between 2 variables that you're not considering, or may be you are measuring time dependent data. If this is the case go back to your model and check your data set closely.
# 
# So now let's go ahead and create the residual plot. For more info on the residual plots check out this great [link](http://blog.minitab.com/blog/adventures-in-statistics/why-you-need-to-check-your-residual-plots-for-regression-analysis).

# In[118]:

train = plt.scatter(Y_pred_trn,(Y_pred_trn-Y_trn),c='b',alpha = 0.5)
test = plt.scatter(Y_pred_tst,(Y_pred_tst-Y_tst), c='r',alpha = 0.5)
plt.hlines(y=0,xmin=-10,xmax=50)
plt.legend((train,test),('Train','Test'),loc = 'lower left')
plt.title('Residual Plots')


# Great! Looks like there aren't any major patterns to be concerned about, it may be interesting to check out the line occuring towards the bottom right, but overall the majority of the residuals seem to be randomly allocated above and below the horizontal.

# That's it for this lesson. Linear regression is a very broad topic, theres a ton of great information in the sci kit learn documentation, and I encourage you to check it out here:  http://scikit-learn.org/stable/modules/linear_model.html#linear-model

# In[ ]:



