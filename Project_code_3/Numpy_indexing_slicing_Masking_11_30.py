#!/usr/bin/env python
# coding: utf-8

# ## dans un tableau a deux dimensions l axe " 0 " ou verticale  correspond aux colones  et l axe " 1 " ou horitontales aux lignes NB quand on ecrit A[ x ,y] x represente l index de la  ligne et y celui de la colonne

# In[1]:


import numpy as np
A = np.array([[1, 2,3], [4, 5, 6], [7, 8, 9] ])
A


# In[2]:


A[0, 0]


# In[3]:


A[1, 1]


# In[4]:


# si par exemple je veut imprimer toute la premiere colone
A[: 0]# bon resultat n est pas ceux a quoi je m attendais


# In[5]:


A[:, 0]# il fallait mettre la virgule pour obtenir le resultat que je voulais


# In[6]:


A[0,:]# tous les elements de la premiere ligne


# ## petit astuce pour imprimer une ligne il suffit juste d ecrire le numero de la ligne entre crochet car cette ligne etant l axe principal  numpy comprendra que l on veut acceder aux elements de cet axe 

# In[7]:


A[0]


# In[8]:


A[1]


# In[9]:


A[2]


# In[13]:


# si on veut acceder a un block voila la syntaxe
A[0:2, 0:2]


# ## le subseting c est creer un petit tableau a partir d un plus grand tableau

# In[14]:


B = A[0:2, 0:2]
B


# In[15]:


B.shape # le tabeau B a pour dimension 2, 2


# In[17]:


A[0:2, 0:2] = 10
A


# In[18]:


A[:, 1:]


# In[19]:


# on peut obtenir le meme resulat avec la technique de l indexing
A[:, -2:] # ici on imprime les deux dernieres colones sans partir de la premiere colone


# In[20]:


C = np.zeros((4,4))
C


# ## ici on va use la technique du sclicing pour imprimer ce que l on veut en se rappellant que l on travail tjr axe apres axe. NB dans le sclicing cet ecriture 1:3 veut dire de 1 a 3 mais les element de la ligne 3 ne sont jamais  pris en compte, ce sont les elements de la ligne 2 qui seront affiches

# In[21]:


C[1:3 ,1:3] 


# In[22]:


C[1:3 ,1:3] = 1 # ici on les as tous attribues la valeur 1
C


# In[23]:


C[0:2, 1:3]


# In[25]:


C[1:3, 0:2]# voila ce que je vaoulais obtenir


# In[27]:


D = np.zeros((5,5))
D


# ## utilisons now le sclicing avec le pas a la fin NB en machine learnig ou en data science on ne fait jamais du slicing avec le pas var c est completement inutile et c est pas ce que l on fait quand in traite les data science cet exemple du bas est juste pour nous montrer le fonctionement

# In[29]:


D[::2, ::2] = 1
D


# ## voici now une technique qui reelement utile en machine laerning et en data science: c est la technique du " boolean indexing "

# In[42]:


E = np.random.randint(0, 10,[5, 5]) # ici on rempli une matrice " E " avec des nombre entier 
                                    # aleatoire dans une matrice de taille 5x5
E


# In[37]:


# now on peut faire des comparaisons dans ce tableau
E < 5 # ce qu on obtient comme tableau est appele un masque et on peut s en servir comme un
    # index a l interieur de n importe quel tableau numpy qui va etre de meme dimension cad 5x5
    # c est donc ca que l on applle le boulean indexing


# In[43]:


E[E < 5 ] = 20
E


# In[46]:


E[E < 10 & (E >7)] = 10
E


# In[50]:


# on peut aussi use le masque d un autre tableau " B "
F = np.random.randn(5,5)
F[E < 5]
F


# ## reponse de lexo du tuto precedent

# In[67]:


def initialisation(m, n):
    # m : nombre de ligne
    # n nombre de colonnes 
    #retourne une matrice aleatoire (m , n+1)
    # avec une colonne biais ( remolie de " 1 ") tout a droite
    X = np.random.randn(m, n)
    X = np.conjugate((X, np.ones(( X.shape[0],1 ))), axis = 1)
    return X
    # bon ca ne marche üas mais je ne vois pas mon erreur ici


# In[65]:


initialisation(3, 4)


# In[ ]:




