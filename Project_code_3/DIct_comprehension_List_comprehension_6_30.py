#!/usr/bin/env python
# coding: utf-8

# In[1]:


# on commence par les " listes comprehension "
# tous les carres de 0 a 9
# une "list comprehension" consiste a inserer la boucle for a l interieur de la liste elle meme
#
liste_1 = []
for i in range(10):
    liste_1.append(i**2)
print(liste_1)


# In[2]:


# voila l exemple d une liste comprehension
# on se rend compte qu on a ecris en une ligne ce qui nous avais 3 lignes avant
# 2eme raison est que ca fait plus python d ecrire de cette maniere
liste_2 = [ i ** 2 for i in range(10)]
print(liste_2)


# In[3]:


import time


# In[4]:


start = time.time()

liste_1 = []
for i in range(1000000):
    liste_1.append(i**2)
end = time.time()
print(end-start)


# In[5]:


start = time.time()

liste_2 = [i**2 for i in range(1000000)]
end = time.time()
print(end-start)


# In[6]:


# on use aussi les "list comprehension " pour creer les nasted list
# les nested list sont des liste qui contiennent d autres listes
liste_3 = [i for i in range(3)]
liste_3


# In[20]:


iiste_3 = [[i for i in range(3)] for j in range(3)]
liste_3 # malheuresement le code ne s execute pas comme prevu
# il va falloir le revoir.


# ## les Dict Comprehension

# In[28]:


dictionaire = { " 0 " : "pierre",
               " 1 " : "jean",
               " 2 " : "julle",
               " 3 " : "boris"}


# In[29]:


prenoms = [ "pierre" , "jean",  "julle",  "boris"]


# In[30]:


dico = {k : v for k, v in enumerate(prenoms)}
print(dico) # pour que ce code fonctione il fallait tous sois ecris de la meme 
# maniere au niveau de dictionaire et de prenoms


# In[31]:


dico.keys()


# In[32]:


dico.values()


# In[33]:


ages = [24, 62, 10, 23]


# In[35]:


dico_2 = { prenom:age for prenom, age in zip(prenoms , ages)}


# In[36]:


print(dico_2)


# In[37]:


dico_2 = { prenom:age for prenom, age in zip(prenoms , ages)}
dico_2


# In[39]:


# on peut maintenant introduire les conditions dans dict comprehension
dico_2 = { prenom:age for prenom, age in zip(prenoms , ages) if age >30}
dico_2


# In[40]:


dico_2 = { prenom:age for prenom, age in zip(prenoms , ages) if age < 30}
dico_2


# In[41]:


dico_2 = { prenom:age for prenom, age in zip(prenoms , ages) if age > 20}
dico_2


# ## Tuple
# 

# In[42]:


tuple_1 = (i**2 for i in range(20))
tuple_1# le message du bas signifi qu on vient de creer un objet ,qui 
# est un generateur
# le generateur est un objet tres importan pour python donc a maitriser 
# absolument


# # reponse de l exo du tuto precedent

# In[43]:


classeur = {
    " positif ":[],
    " negatif ":[],
}


# In[45]:


def trier(classeur , nombre):
    # classeur . dictionaire taille 2
    # nombre . int
    # range nombre dans " positf " au " negatif " de classeur selon le signe de nombre
    if nombre >= 0:
        classeur[ " positif "].append(nombre)
    else:
        classeur[" negatif "].append(nombre)
    return classeur


# In[51]:


trier(classeur, 50)
# il faut voir que chaque fois que j ajoutes un nombre il se rajoute a la fin
# de positif ou de negatif


# In[ ]:




