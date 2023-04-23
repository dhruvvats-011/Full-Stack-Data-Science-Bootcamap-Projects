#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. What exactly is [ ] ?
Solution -

It is a list of empty elements.
Use to assing value at specific index.
Assume - numbers = [2, 4, 6, 8, 10]

get_ipython().set_next_input("2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value");get_ipython().run_line_magic('pinfo', 'value')
Solution - spam[2] = 'hello'


3.What is the value of spam[int(int('3' * 2) / 11)]?
 Solution - 8


4. What is the value of spam[-1]?
soution - 10


5. What is the value of spam[:2]?
solution - [2, 4]


Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.
6. What is the value of bacon.index('cat')?
solution - 1, becase index of "cat" value is one.


get_ipython().set_next_input('7. How does bacon.append(99) change the look of the list value in bacon');get_ipython().run_line_magic('pinfo', 'bacon')
Solution - [ 3.14, "cat", 11, "cat", True, 99]


get_ipython().set_next_input("8. How does bacon.remove('cat') change the look of the list in bacon");get_ipython().run_line_magic('pinfo', 'bacon')
Solution - [3.14, 11, 'cat', True, 99].

First accurence of "cat" will be removed.


get_ipython().set_next_input('9. What are the list concatenation and list replication operators');get_ipython().run_line_magic('pinfo', 'operators')
Solution -

The '+' operator can be used to concatenate two lists.
The '*' operator can be used to replicate list.

10. What is difference between the list methods append() and insert()?
Solution -

*insert()* to add a specific element at a specified index.
*append()* to add the element only at end of the list.

get_ipython().set_next_input('11. What are the two methods for removing items from a list');get_ipython().run_line_magic('pinfo', 'list')
Solution -

list.remove("value") - Remove the Element by Value.
list.pop(index) - Remove the Element by Index.

12. Describe how list values and string values are identical.
List values and string values are identical Because :-

We can access char in string by index just like elements in list.
We can do pop operation in both. etc.

get_ipython().set_next_input("13. What's the difference between tuples and lists");get_ipython().run_line_magic('pinfo', 'lists')
Solution -

The key difference between the tuples and lists is that while the tuples are immutable objects the lists are mutable.


14. How do you type a tuple value that only contains the integer 42?
Soluiton - t = (42)


get_ipython().set_next_input("15. How do you get a list value's tuple form? How do you get a tuple value's list form");get_ipython().run_line_magic('pinfo', 'form')
Solution -

tuple(list_name) will return list as tuple

list(tuple_name) will return tuple as list


get_ipython().set_next_input('16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain');get_ipython().run_line_magic('pinfo', 'contain')
Solution - Elements


17. How do you distinguish between copy.copy() and copy.deepcopy() ?
Solution -

The difference between copy and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances).

