
# coding: utf-8

# In[15]:

l1 = list('abcd')
l1


# In[16]:

l2 = [1,2,3,4]


# In[17]:

l1.insert(1,'2')
l1


# In[18]:

l2.append('z')
l2


# In[22]:

l3 = l1.copy()
l3


# In[23]:

l3.extend(l2)
l3


# In[26]:

l2 = [1,2,3,4]


# In[25]:

l2.pop()


# In[27]:

l2


# In[28]:

l2.pop(1)


# In[29]:

l2


# In[30]:

l1


# In[31]:

l1.remove(1)


# In[33]:

l1.remove('2')


# In[34]:

l1


# In[35]:

l2


# In[36]:

l2.reverse()


# In[37]:

l2


# In[40]:

l3 = [4,3,6,7,9]


# In[41]:

l3.sort()


# In[42]:

l3


# In[44]:

l3.sort(reverse = True)


# In[45]:

l3


# In[48]:

l3.index(5)


# In[49]:

l3.index(7)


# 
#     list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
#     list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
#     list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
#     list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
#     list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
#     list.sort() -- sorts the list in place (does not return it). (The sorted() function shown below is preferred.)
#     list.reverse() -- reverses the list in place (does not return it)
#     list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).
# 
