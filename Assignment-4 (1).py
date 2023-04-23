#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1.What exactly is [ ]?
Ans:The empty list represented by [] is a list that contains no items.
    This is similar to '' which represents an empty string


# In[ ]:


2.In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)
Ans: spam[2]='hello' (Note: Lists follows zero based indexing)


# In[1]:


# Example
spam=[2,4,6,8,10]
print(spam)
spam[2]='hello' #List uses zero based indexing
print(spam)


# In[ ]:


Let's pretend the spam includes the list ['a','b','c',d'] for the next three queries.
3. What is the value of spam[int(int('3'*2)//11)] ?
Ans: 'd' (Note that '3' * 2 is the string '33', which is passed to int() before being divided by 11. 
          This eventually evaluates to 3, spam[3] is equal to d.)


# In[2]:


spam=['a','b','c','d']
print("spam[int(int('3'*2)//11)] ->",spam[int(int('3'*2)//11)])


# In[ ]:


4. What is the value of spam[-1]?
Ans: 'd' (Lists support Negative indexing, Hence spam[-1] returs 'd')


# In[3]:


spam=['a','b','c','d']
print('spam[-1] -> ',spam[-1])


# In[ ]:


5. What is the value of spam[:2]?
Ans: spam[:2] returns all elements in the list spam from 0 to 2 excluding 2


# In[4]:


print(spam)
print(spam[:2])


# In[ ]:


Let's pretend bacon has the list [3.14,'cat',11,'cat',True] for the next three question
6. What is the value of bacon.index('cat')?
Ans: The value of bacon.index('cat') is 1 (Note: index method returns the index of first occuerence of 'cat')


# In[5]:


bacon=[3.14,'cat',11,'cat',True]
print("bacon.index('cat') ->",bacon.index('cat'))


# In[ ]:


get_ipython().set_next_input('7. How does bacon.append(99) change the look of the list value in bacon');get_ipython().run_line_magic('pinfo', 'bacon')
Ans: The append method adds new elements to the end of the list


# In[6]:


# Example
print(bacon)
bacon.append(99) # appends 99 to the end of the list
print(bacon)


# In[ ]:


get_ipython().set_next_input('9.what are the list concatenation and list replication operations');get_ipython().run_line_magic('pinfo', 'operations')
Ans: The operator for list concatenation is +, while the operator for replication is *.
    (This is the same as for strings.)


# In[7]:


# Example
list_1 = ['ML','DL','AI','CV','NLP']
list_2 = ['RNN','CNN','SVN']
print(list_1 + list_2) # List Concatenation
print(list_2*2) # List Replication


# In[ ]:


10.what is the difference between the list method append() and insert()?
Ans: While append() will add values only to the end of a list, insert() can add them anywhere in the list.


# In[8]:


#Examples
list = [1,2,3,4,5]
list.append(6)
print(list)
list.insert(2,'Demo')
print(list)


# In[ ]:


get_ipython().set_next_input('11. What are the two methods for removing items from a list');get_ipython().run_line_magic('pinfo', 'list')
Ans: The del statement and the remove() method are two ways to remove values from a list


# In[ ]:


12. Describe how list values and string values are identical.
Ans: Both lists and strings can be passed to len() function, have indexes and slices, be used in for loops,
     be concatenated or replicated, and be used with the in and not in operators.


# In[ ]:


get_ipython().set_next_input("13. What's the difference between tuples and lists");get_ipython().run_line_magic('pinfo', 'lists')
Ans: Lists are Mutable, Indexable and Slicable. they can have values added, removed, or changed.
    Tuples are Immutable but Indexable and Slicable. the tuple values cannot be changed at all.
    Also, tuples are represented using parentheses, (), while lists use the square brackets, [].


# In[ ]:


14. How do you type a tuple value that only contains the integer 42?
Ans:(42,) (The trailing comma is mandatory. otherwise its considered as a int by python Interpreter)


# In[9]:


tup1=(42)
tup2=(42,)
print(type(tup1))
print(type(tup2))


# In[ ]:


get_ipython().set_next_input("15. How do you get a list value's tuple form? How do you get a tuple value's list form");get_ipython().run_line_magic('pinfo', 'form')
Ans: The tuple() and list() functions, respectively are used to convert a list to tuple and vice versa


# In[ ]:


get_ipython().set_next_input('16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain');get_ipython().run_line_magic('pinfo', 'contain')
Ans: They contain references to list values.


# In[ ]:


17. How do you distinguish between copy.copy() and copy.deepcopy()?
Ans: The copy.copy() function will do a shallow copy of a list,
    while the copy.deepcopy() function will do a deep copy of a list.
    That is, only copy.deepcopy() will duplicate any lists inside the list.

