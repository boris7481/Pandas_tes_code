#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[6]:


np.random.seed(0)
A = np.random.randint(0, 10, [2, 3])
A


# ## Methodes ndarray petit rappel encor sur les axes: l axe " 0 " c est l axe verticale (les colones ) et celle horizontale ou axe " 1" les lignes NB quand on ecrit A[ x ,y] x represente l index de la  ligne et y celui de la colonne

# In[7]:


A.sum() # pour faire la somme des elements de mon tableau


# In[9]:


A.sum(axis = 0)# ici on a sommer les element d une mem colone


# In[10]:


A.sum(axis = 1) ici on somme les elements horizontalement kigne par ligne


# In[13]:


A.cumsum() # ici on fait la somme cumulee


# In[14]:


A.min()


# In[15]:


A.min(axis = 0) # a chaque fois on a affiche le plus petit element verticalement


# ## voila une methode qui permet de trouber la position du minimum " argmin"

# In[18]:


A.argmin(axis=0) # en faite il nous donne les postions de chaque minimu colone par colone


# ## la methode " argsort " retourne les index dans l ordre de tri du tableau A,sans modifier le tableau A ( il n est pas trie) cette methodes est super utile pour effectuer des classement dans un tableau numpy

# ## voyons now autres choses

# In[20]:


np.exp(A) # voila coment il fau tecrire pour avoir l exponetiele des caleur dans A


# In[22]:


np.cos(A)


# In[23]:


np.sin(A)


# ## now les statistiques

# In[24]:


A.mean() # ici c est pour avoir la moyenne de A


# In[25]:


A.mean(axis=0)


# In[26]:


A.mean(axis=1)


# In[27]:


A.std() # pour avoir l ecart type de A


# In[28]:


A.var()


# In[29]:


# voyons la fonction corrcoef correlation entre les diffwerentes lignes de notre tableau
np.corrcoef(A)


# In[30]:


np.corrcoef(A)[0,1]


# ## foncton pour trouver le nombre de fois que certains  element se repetent dans un tableau Numpy: c est la fonction np.unique. elle nous retourne les differentes entites presentent dans le tableau numpy et egalement le nombre de reptition de chacune de ses identitees NB cette fonction est tres importantepour les gros tableaux

# In[31]:


np.unique(A, return_counts=True)


# In[32]:


np.random.seed(0)
B = np.random.randint(0, 10, [5, 5])
B


# In[33]:


np.unique(B, return_counts=True)


# In[34]:


values, counts = np.unique(B, return_counts=True)


# In[35]:


counts


# In[37]:


counts.argsort() # on obtient un tableau d index qui permettra de trier counts cad si on veut 
# trier counts du plus petit au plus grand ,il faut d abord placer l index 0 ensuite 2 ect...


# In[38]:


# now injectons tous ses index a l interieur du tableau Values pour voir quel nombre 
# revient le plus souvent ou le moins souvent ,üar exemple le nombre 8 apparait le plus 
# souvent ensuite le 7 ainsi de suite
values[counts.argsort()]


# In[43]:


for i,j in zip(values[counts.argsort()], counts[counts.argsort()]):
    print(f"valeur{i}apparait{j}")


# ## NAN Corrections : parfois il nous manque des nombre quand on collecte les donnees de la vrai vie ou bien on a des donnes corrompus en general ceci se traduit par la presence d une entitee dans notre tableau appelle NAN = Not a Number qui veut dire pas de nombre

# In[44]:


np.random.seed(0)
C = np.random.randint(0, 10, [5, 5])
C


# In[45]:


C = np.random.randn(5,5)
C[0, 2] = np.nan
C[4, 3] = np.nan
C


# In[49]:


C.mean() # en voulant calculer la moyenne ici on obtient en retour NAN donc ilfaut passer 
         # par un autre moyen pour le faire


# In[50]:


# voila la fonction a use
np.nanmean(C)


# In[51]:


np.nanvar(C)


# ## now coment compter le nombre de fois que l on retrouve le NAN dans notre tableau

# In[52]:


# premiere methode cette fonction nous retourne un masque avec des bouleen ou True represente
# la presence d un NAN
np.isnan(C)


# In[54]:


np.isnan(C).sum() # on vois qu on deux fois une entitee NAN dans le tableau


# ## si on veut connaitre le rapport de NAN que l on a par rapport a toute la taille de notre tableau on procede comme suit

# In[55]:


# ce resultat veut dire qu on 8 pourcent des valeurs de notre tableau qui sont des valeurs NAN
np.isnan(C).sum()/C.size


# ## Now coment se debarrasser des NAN dans untableau Numpy en utilisant Numpy avec le " Boulean indexing "

# In[56]:


np.isnan(C) # ici on obtient un masque


# In[57]:


# on peut reinjecter se masque dans " C " et dire que tous les NAN prenent la valeur " 0 "
C[np.isnan(C)] = 0
C


# ## Algebre Lineaire.   d une maniere general quand on veut faire de l agebre lineaire sur Numpy, on a Subpackage intierement dedier a cela appele Numpy.linalg

# In[59]:


C = np.ones((2, 3))
D = np.ones((3, 2))
C


# In[61]:


D


# In[62]:


# pour avoir la transposee de notre matrice
C.T


# In[63]:


# Pour la multiplication des matrices 
C.dot(D)


# In[67]:


X = D.dot(C)
X


# In[69]:


# pour le calcul du determinant par exemple on aura
np.linalg.det(B)


# In[70]:


# inversons now la matrice vu que son determinant est different de zero
np.linalg.inv(B)


# ## Now coment trouver les valeurs propre et les vecteurs propres d une matrice , ce ci peut nous etre utle dans certains algorithme du machine learnig NB eig= eigenvalues=valeures propres mais eig = eigenvecteurs = vecteurs propres

# In[71]:


np.linalg.eig(B)


# In[ ]:




