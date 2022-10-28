#!/usr/bin/env python
# coding: utf-8

# In[12]:


def summe (x,y):
    s = x + y
    return s


# In[17]:


b = summe(2,5)
b


# In[14]:


b = summe(2,5)


# In[18]:


def summe (x,y):
    s = x + y
    return s
c = summe(2,5)
c


# In[9]:


def summe (x,y):
    s = x+y
    summe (2,5)


# In[24]:


def build_person(first_name, last_name, age=" "):
    person = {"first":first_name, "last" : last_name,}
    if age:
        person["age"] = age
    return person
musician = build_person("jimi", "hendrix", age = 27)


# In[26]:


print(musician)


# In[37]:


def salutation (noms):
    for nom in noms:
        mgs = "bonjour" + "" + nom
        print(mgs)


# In[38]:


nom_person =["boris", "junior" , "hermann"]


# In[39]:


salutation(nom_person)


# In[ ]:


nom_dico =["boris" :, "junior" , "hermann"]

