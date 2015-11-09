
# coding: utf-8

# ## Iterators and Generators

# The built-in function iter takes an 'iterable' object and returns an iterator. Each time we call the 'next' method on the iterator gives us the next element. If there are no more elements, it raises a StopIteration.

# In[15]:

# Example
str1 = 'ABCD'
i = iter(str1)
while True:
    try:
        print(next(i))
    except:
        break


# 1. Our own iterator example. We can create iterator for our own class by overloading __iter__ and __next__methods

# In[16]:

#__author__ = 'Varun'


class vector:
    data = []

    def __init__(self,d):
        self.data = d

    def __repr__(self):
        return ','.join([str(i) for i in  self]) # We are using our iterator implementation here

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.data):
            raise StopIteration
        return self.data[self.index]
        


# In[17]:

def Main():

    v1 = vector([1,2,3,4,5])
    print('value from : __repr__ via normal print : ', v1)
    print('value from : __repr__ via normal repr : ', repr(v1))
    print ('vector v is : {0}'.format(v1))

    for i in v1:
        print('vector element %d'%i)

if __name__ == '__main__':
    Main()
    


# In[19]:

v2 = vector([1,2,3,4,5])


# In[20]:

sum(v2)


# ### Generators

# A generator is simply a function which returns an object on which you can call next, such that for every call it returns some value, until it raises a StopIteration exception, signaling that all values have been generated. Such an object is called an iterator.
# 
# Normal functions return a single value using return, just like in Java. In Python, however, there is an alternative, called yield. Using yield anywhere in a function makes it a generator

# In[39]:

def getFib(n):
    i1 = 0
    i2 = 1
    i3 = 0
    k = 0
    while k < n:
        yield i3
        i1,i2 = i2,i3
        i3 = i1+i2
        k += 1
        
    


# In[50]:

gen = getFib(10)


# In[51]:

import sys
while True:
    try:
        print(next(gen))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        break


# In[10]:

gen = getFib(10)


# In[11]:

for i in gen:
    print(i)


# In[29]:

print(str(StopIteration))


# In[ ]:



