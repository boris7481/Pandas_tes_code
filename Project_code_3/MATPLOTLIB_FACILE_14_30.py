#!/usr/bin/env python
# coding: utf-8

# ## Matplotlbpour les graphes

# ## 1) Pyplot

# In[3]:


import numpy as np


# In[5]:


x = np.linspace(0, 2, 10)


# In[6]:


y = x**2
print(x)


# In[7]:


import matplotlib.pyplot as plt


# In[8]:


plt.plot(x,y)# x sur l axe des abcisses et y sur celui des ordonnees


# In[9]:


# pour avoir unnuage de point on use la fonction " scater " NB si tu ne travail pas sur 
# ilte faut ecrire la ligne de code plt.show() pour voir le graphe
plt.scatter(x, y)


# In[10]:


# pour travailler sur la courbe on va choisir des parametre le parametre " c " c est pour 
# la couleur
plt.scatter(x, y, c ="red" )


# In[12]:


# le parametre " lw " nous permet de choisir l epaisseur de notre ligne
plt.scatter(x, y, c ="red" ,lw =3)


# In[17]:


# le dernier parametre est le " ls= linestxle "
plt.plot(x, y, c ="red" ,lw =3, ls = "--")


# ## La chose la plus importante a comprendre dans Matplotlib est ;" Le cycle de vie d une figure "

# In[22]:


plt.figure(figsize=(12, 8)) # ici on donne les dimensions en inch de notre figure
plt.plot(x,y)


# In[24]:


plt.figure()
plt.plot(x,y)
plt.plot(x, x**3)# on a ajoute ce plot a la fihure


# In[25]:


plt.figure()
plt.plot(x,y)
plt.plot(x, x**3)# on a ajoute ce plot a la fihure
plt.title(" figure 1")# on lui ajoute un titre


# In[29]:


plt.figure()
plt.plot(x,y)
plt.plot(x, x**3)# on a ajoute ce plot a la fihure
plt.title(" figure 1")# on lui ajoute un titre
plt.xlabel(" axe x ")# on donne les noms aux axes
plt.ylabel(" axe y" )# de l axe ordonnes 


# ## vois a peu pres dans le code du bas tous les elements qui constituent le cycle de vie d une figure dans Matplotlib 

# In[35]:


plt.figure()
plt.plot(x,y, label= " quadratique ")
plt.plot(x, x**3, label= " cubique ")# on a ajoute ce plot a la fihure
plt.title(" figure 1")# on lui ajoute un titre
plt.xlabel(" axe x ")# on donne les noms aux axes
plt.ylabel(" axe y" )# de l axe ordonnes 
plt.legend()# ajoutons now une legende a notre graphe et ca ca se fait en haut du code
plt.show()# en realite on est pas oblige d ecrire cette ligne dans Jupyther notbook
plt.savefig("figure.png")# pour savegarder la figure dans notre repertoire de travail


# ## parfois on a envie d afficher plusieurs fonctions sur un meme graphe, pour cela on use la fonction subplot

# In[43]:


plt.subplot(2,1, 1)
plt.plot(x,y, c = "black")# bien coller " black dans les guillemets"


# In[45]:


plt.subplot(2,1, 1)
plt.plot(x,y, c = "black")# bien coller " black dans les guillemets"
plt.subplot(2,1, 2)
plt.plot(x,y, c = "blue")


# ## la seconde methode orientee objet pour le tracage des graphe n est pas a recommender car la premiere methode vu plus haut est largement suffisante pour tracer tous les graphes donc nous aurons besoin raison pour laquelle j ai üas continuer avec les autres codes

# In[ ]:




