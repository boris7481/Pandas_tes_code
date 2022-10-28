#!/usr/bin/env python
# coding: utf-8

# In[1]:


liste = ["boris","hermann", "georvanie", "davila"]


# In[2]:


for i in liste:
    print(i + " " ,"bonjour toi")


# In[3]:


liste = ["boris","hermann", "georvanie", "davila"]


# In[4]:


for i in liste:
    print(i + " " ,"bienvenu a la fete")
    if i == liste[0]:
        print(liste[0] + " " ,"kommt nicht mehr")


# In[5]:


for i in liste:
    if i == liste[0]:
         print(liste[0] + " " ,"kommt nicht mehr")
    else:
        print(i + " " ,"bienvenu a la fete")


# In[6]:


liste[0]= "alex"
liste


# In[7]:


liste.insert(1,"junior")


# In[8]:


liste


# In[9]:


liste_1 = ["douala" , "yaounde", "bafang", "kribi"]


# In[10]:


liste_1.sort(reverse = True)
liste_1


# In[11]:


liste_1.sort()
liste_1


# In[12]:


len(liste)


# In[13]:


liste_2 = []
for i in range(10):
    liste_2.append(i**3)
    print(i, [liste_2])


# In[15]:


liste_2


# In[16]:


cars = ["audi", "bmw", "mercedes", "toyota" ]
cars


# In[17]:


for car in cars:
    if car == "bmw":
        print( car.upper())
    else:
        print (car)


# In[18]:


for car in cars:
    if car != "bmw":
        print( car.upper())
    else:
        print (car)


# In[ ]:


age = 12
if age<4:
    price = 0
elif age < 18:
    price = 65
elif age < 20:    
    price = 5
else:
    price = 10
print("ton entree coute" + " " + str(price))


# In[ ]:


dico = {"boris":"geo","herrmann":"emo", "alex":"geo"}


# In[ ]:


for i in set(dico.values()):
    print(i)
    


# In[ ]:


boris = input("please inter your Name")
boris = input()
print("pourquoi ?")
boris = input()
boris = input()


# In[ ]:


def nom_person(nom, prenom)


# In[ ]:





# In[ ]:




