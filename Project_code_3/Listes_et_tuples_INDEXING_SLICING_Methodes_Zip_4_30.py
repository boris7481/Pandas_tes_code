#!/usr/bin/env python
# coding: utf-8

# In[1]:


#listes
liste_1 = [1, 4, 2, 7, 35, 84]
villes = ["paris", "berlin", "londres", "yaounde"]
liste_2 = [liste_1, villes]
liste_3 = []


# In[2]:


#tuples
tuple_1 = (1, 2, 6, 1, 7)


# In[3]:


#string
prenom = " boris "


# In[4]:


# chaque element de la liste a un index et l index de chque liste commence par zero
print(villes[0])
print(villes[1])
print(villes[-1]) # pour acceder au dernier element de ma liste 
print(villes[-2])# pour acceder a l avant  dernier element de ma liste
# Cette technique  s appelle le INDEXING 


# In[8]:


# l autre technique est le SLICING elle nous permet d acceder a une fourchette d element
print(villes[0:3])


# In[9]:


# en general quand on fait le SLICING a partir de l index zero on l ignore dans kes crochets
print(villes[:3])


# In[10]:


# c est le meme principe ici mainteant on veut les elements d indice 2 jusqu a la fin
print(villes[2:])


# In[11]:


print(villes[1:3])


# In[12]:


#on commence par paris et on saut un element pour tomber sur le suivant car le pas est 2
print(villes[::2])


# In[13]:


# ici on utilise le pas en l envers c est utile de le savoir
print(villes[::-1])


# In[14]:


#SLICING aussi sur les string
print(prenom[:3])


# In[18]:


# on peut aussi modifier les element d une liste 
villes[0] = " douala "
print(villes)


# In[19]:


# a partir d ici on verra les methodes utilisees sur les listes apres avoir ecris villes appuyer sur la touche Tab
villes.append(" Bafang ")# append permet l ajout d un element a la fin d une liste


# In[20]:


villes # remarquer qu ici j ai juste ecris le ,ot mot volles le mot print


# In[30]:


villes.insert(2,"lyon")
villes # ici je dois souligner qu il y a un problem


# In[31]:


villes_2 = [" amsterdam", "rome"]
villes.extend(villes_2)# extend pour ajouter une liste a la fin d une autre
villes


# In[32]:


len(villes) # nombre  d element de ma liste


# In[33]:


villes.sort()# pour sortir les donnes de la liste par ordre alphabetique
villes


# In[34]:


villes.sort(reverse = True )# pour les donnes par ordre anti-alphabetique
villes


# In[35]:


liste_2 = [52, 51, 23, 61, 3, 2, 78, 24]
liste_2.sort()# ici on sort les donnees par ordre croissant de la liste
liste_2


# In[37]:


liste_2 = [52, 51, 23, 61, 3, 2, 78, 24]
liste_2.sort(reverse = True)# ici on sort les donnees par ordre decroissant de la liste
liste_2


# In[38]:


#methode qui permet de compter combien de fois une valeur apparait dans une liste
villes.count("regensburg")


# In[45]:


villes.count(" douala ")# ca ne fonctione pas ici et je ne sais pourquoi


# In[40]:


villes.count(" lyon ")# ca ne fonctione pas ici et je ne sais pourquoi


# In[44]:


if " paris " in villes:
 print(" oui ")
else:
    print(" non ")


# In[46]:


if " douala " in villes:
 print(" oui ")
else:
    print(" non ")


# In[47]:


for i in villes:
    print(i)


# In[49]:


for index, valeur in enumerate(villes):# ici tu peut imprimer l index et la valeur correspondante
    print(index, valeur)


# In[50]:


# la commeande zip nous permet d utiliser la boucle for avec deux listes en parallele
for a, b in zip(villes, liste_2):# il faut noter que a boucle for s arretra la ou la liste la plus courte va s arreter
    print(a, b)


# In[53]:


#reponse de l exo du tuto precedent
def fibonacci(n):
    a = 0
    b = 1
    while a < n:
        print(a)
        a, b = b, a+b


# In[54]:


fibonacci(1000)


# In[ ]:




