#!/usr/bin/env python
# coding: utf-8

# In[49]:


## Try numpy array to increase speed


# In[ ]:





# In[34]:


def solution(A):
    lst = [i for i in A if A.count(i)%2!=0]
    return lst[0]
lst = solution([9, 3, 9, 3, 9, 7, 9])
print(lst)


# In[ ]:


def solution(A):
    lst = [i for i in A if A.count(i)%2!=0]
    return lst[0]
lst = solution([9, 3, 9, 3, 9, 7, 9])
print(lst)


# In[48]:


def solution(A):
    if len(A)>1000:
        for i in range(5):
            m = max(A,key=A.count)
            if A.count(m)%2!=0:
                return m
            else:
                #A.remove(m)
                A = list(filter((m).__ne__, A))
                #print(A)
    lst = [i for i in A if A.count(i)%2!=0]
    return lst[0]
lst = solution([9, 3, 9, 3, 9, 7, 9])
print(lst)


# In[28]:


def solution(A):
    for i in range(10):
        cnt = A.count(i)
        if cnt ==1:
            return i
lst = solution([9, 3, 9, 3, 9, 7, 9])
print(lst)


# In[9]:


def solution(A):
    unmatched = dict()
    for i in A:
        del unmatched[i]
    if len(unmatched) == 1:
        return unmatched.keys()[0]

solution([9, 3, 9, 3, 9, 7, 9])


# In[ ]:





# In[ ]:




