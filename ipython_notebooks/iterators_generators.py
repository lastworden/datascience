
# coding: utf-8

# ## Iterators and Generators

# The built-in function iter takes an 'iterable' object and returns an iterator. Each time we call the 'next' method on the iterator gives us the next element. If there are no more elements, it raises a StopIteration.

# In[22]:

# Example
str1 = 'ABCD'
i = iter(str1)
while True:
    try:
        print(next(i))
    except:
        break


# 1. Our own iterator example. We can create iterator for our own class by overloading __iter__ and __next__methods

# In[23]:

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
        


# In[24]:

def Main():

    v1 = vector([1,2,3,4,5])
    print('value from : __repr__ via normal print : ', v1)
    print('value from : __repr__ via normal repr : ', repr(v1))
    print ('vector v is : {0}'.format(v1))

    for i in v1:
        print('vector element %d'%i)

if __name__ == '__main__':
    Main()
    


# In[ ]:



