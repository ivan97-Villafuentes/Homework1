#!/usr/bin/env python
# coding: utf-8

# In[4]:


a = [1,2,3]
b = [3,2,1]

c=[]
c=a
a=b
b=c

print(a)
print(b)


# # primer ejercicio

# In[5]:


alice=121
bob=77
carol=110
suma=(alice+bob+carol)/3
print(int(suma))


# In[6]:


alice=121
bob=77
carol=110
suma=(alice+bob+carol)
print(int(suma%3))


# In[11]:


alice=121
bob=77
carol=110
n=3
total=(alice+bob+carol)
dulces=total//n
residuo=total-(n*dulces)
print(total, dulces, residuo)


# In[ ]:




