#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Write a Python program to get the Fibonacci series between 0 to 50


# In[2]:


a=0
b=1
for i in range(50):
    print(a,end=',')
    c=a+b
    b=a
    a=c

