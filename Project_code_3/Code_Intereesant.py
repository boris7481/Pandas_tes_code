#!/usr/bin/env python
# coding: utf-8

# In[10]:


x=1

if x>0:
    print(x, "est positif")


# In[11]:


liste =[1, 3, 6 ,5 ,9]
print(liste[0])


# In[13]:


liste.count(5)


# In[19]:


if 2 in liste:
 print(2, "ist vorhanden")
else:
    print(2,"ist nicht vorhanden")


# In[22]:


liste_2 = ["boris", "hermann"",bblaure","davila"]


# In[26]:


dico ={liste :liste_2 for liste, liste_2 in zip(liste,liste_2)}


# In[41]:


dico


# In[43]:


import numpy as np
A = np.array([1, 2, 3])


# In[44]:


A.shape


# In[46]:


A = np.array([1, 2, 3])
A= A.reshape((3,1))
A.shape


# In[50]:


B= np.random.randn(4,4)
B.shape[0]


# In[51]:


B


# In[52]:


B[0]


# In[60]:


C = np.random.randint(0,10,[5,5])
C


# In[61]:


C<4


# In[63]:


C[C<4] = 10


# In[64]:


C


# In[ ]:




