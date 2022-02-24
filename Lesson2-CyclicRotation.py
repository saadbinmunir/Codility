#!/usr/bin/env python
# coding: utf-8

# In[4]:


from collections import deque
def solution(A, K):
    # write your code in Python 3.6
    d=deque(A)
    d.rotate(K)
    lst = list(d)
    return lst

