#!/usr/bin/env python
# coding: utf-8

# ## la fonction la plus importante use en data science dans les tableau est la fonction shape elle nous permet de voir la forme de notre tableau cad combien de ligne ,de colone, quelle est sa profondeur( dans le cas d un tableau a trois dimensions) et le scond est l attribut size qui nous retourne le nombre d element qu il ya dans notre tableau (les autres attributs pourrons etre appris au fur et a mesure) NB: ne pas oublier que l attribut shape est un tuple cest tres important

# In[1]:


import numpy as np


# In[4]:


A = np.array([1, 2, 3])# ici on a creer un tableau a une dimension
A                       # important de voir la syntaxA


# In[5]:


A.ndim # cette ligne de code permet de verifier le nombre de dimensions


# In[6]:


A.shape # cette ligne de code permet de voir sa forme ca npous indique que sur son unique 
        # dimension il ya trois elements


# In[11]:


B = np.zeros((3,2))# cette fonction initialise notre tableau plein de zeros
B # dans les parantheses on a un shape oder tuple pour donner les dimesnsions de notre tableau


# In[12]:


B.ndim


# In[15]:


B.shape # verification de la forme du tableau


# In[16]:


type(B.shape) # juste pour verifier qu on bien a faire a un tuple


# In[17]:


B.size # pour verifier la taille de notre tableau qui est le produit des
       # differentes dimensions de notre tableau


# In[19]:


C = np.ones((3,4)) # on initialise notre tableau avec trois ligne et quatres colones
C


# In[26]:


np.random.randn(3,4) # c est cette initialisition qui nous interesse le plus souvent en machine
                     # learnig
    # NB bien voir qu ici on a pas use untuple pour entrer les dimensions de notre tableau


# In[25]:


np.random.seed(0) # pour tjr avoir les memes valeurs aleatoire apres execution
np.random.randn(3,4)


# In[27]:


# juste pour info ,creation de la matrice identite
np.eye(4)


# # now voyons deux autres types de constructeurs "linspace" et " arange "

# In[28]:


# voila pour linspace , np.linspace (debut, fin,quantite)
np.linspace(0, 10, 20)


# In[29]:


# np.arange(debut, fin, pas)
np.arange(0, 10, 1)


# # on va parler du dtype cad datatype qui permet de dire quelles genres de donnees je veut avoir dans mon tableau

# In[30]:


np.linspace(0, 10, 20,dtype = np.float64) # mais avec le type float le programme sera lent 
                                          # a l execution
    # 64 veut dire que chaque element occupe 64 bit de notre memoire


# In[31]:


np.linspace(0, 10, 20,dtype = np.float16) # ici les resultats sont mois precis mais le 
# programme est plus rapide a l execution


# # methodes qui nous permettent de manipuler les tableau

# In[32]:


D = np.zeros((3,2))
E = np.ones((3,2))


# In[33]:


print(D)


# In[34]:


print(E)


# In[39]:


# Assemblons now les tableaux pour assembler horizontalement
F = np.hstack((D,E))
F


# In[40]:


F.shape


# In[42]:


# now colons les tableaux verticalement
G = np.vstack((D,E))
G


# In[43]:


G.shape


# ## il ya aussi une autre methode qui permet d aboutir au meme resultat, c est la methode concatenate, cette methode est meme a priviligier car elle nous permettra de mieux comprendre les axes des tableaux numpy et de 2 pour les tableaux a trois dimensions elle est la seule qui peut agir. ilfaut juate savoir bien definir l axe d assemblage des tableaux

# In[44]:


H = np.concatenate((D,E),axis = 0)
H# dans unarrays a deux dimensions 0 est l axe des ordonnees et 1 est celui des abcisses


# In[45]:


I = np.concatenate((D,E),axis = 1)
I


# ## une autre methode tres importante , c est la methode reshape elle nous permet de remanipuler la forme d un tableau pour lui donner une nouvelle forme mais attention elle ne fonctione que si le nombre d elements qu on a la fin est egal au nombre d elements final NB le remaniment de la forme d un tableau a evidement impact sur la facon dont les nombres sont disposees dans notre tableau

# In[47]:


F = F.reshape((3,4))
F


# In[48]:


K = np.array([1, 2, 3,])
K.shape # mais cette ecriture derange souvent au niveau des algorithmes
# raison pour laquelle on aime bien la changer


# In[50]:


# voila coment on peut redimensioner la Matrice F
K = np.array([1, 2, 3,])
K = K.reshape(K.shape[0], 1)# ici on genre juste la forme d apparution de l ecriture 
                            # de la forme
K.shape 


# In[51]:


# si aussi on veut revenir a l ecriture initiale on use la methode "squeeze"
K = K.squeeze() # elle permet de faire disparaitre toutes les dimensions dans lesquelles on a 
                # le chiffre 1


# In[53]:


K.shape


# # voyons now la methode ravel qui permet d applatir un tableau a une seule dimension

# In[54]:


F = F.reshape((3,4))
F


# In[56]:


F = F.reshape((3,4))
F.ravel() # on affiche tous les elements sur une meme dimension


# In[57]:


F.ravel().shape # ici on verifi juste que la dimension n a pas change


# In[ ]:




