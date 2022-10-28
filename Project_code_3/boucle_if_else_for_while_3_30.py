#!/usr/bin/env python
# coding: utf-8

# In[5]:


x = 1
if x > 0:
    print(x,"positif")


# In[6]:


x = 0
if x > 0:
    print(x , "positif")
elif x == 0:
    print(x, "nul")
else:
    print(x , "negatif")


# In[8]:


x>0


# In[9]:


x == 0


# In[10]:


x = 1
y = 2
if (x > 0) & (y > 0):
    print(x ,y , "positif")
elif x == 0:
    print(x, "nul")
else:
    print(x , "negatif")


# In[11]:


def signe(x):
    if (x > 0):
        print(x , "positif")
    elif x == 0:
        print(x, "nul")
    else:
        print(x , "negatif")


# In[12]:


signe(0)


# In[13]:


for i in range(10):
    print("bonjour")


# In[14]:


for i in range(10):
    print(i)


# In[15]:


for element  in range(10):
    print(element)


# In[16]:


for element  in range(5, 10,2):
    print(element)


# In[17]:


for element  in range(10, -10,-1):
    print(element)


# In[18]:


for element  in range(10, -10,-1):
 signe(element)


# In[19]:


x = 0
while x<10:
    print(x)
    x +=1


# In[51]:


def e_potentielle_limite(masse, hauteur, limite, g= 9.81):
    E = masse * hauteur * g
    print(E)
    return E < limite


# In[54]:


e_potentielle_limite(50, 10, 6000)


# In[ ]:




