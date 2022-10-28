#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = -3


# In[2]:


abs(x)


# In[3]:


x = 3.14
round(x)


# In[4]:


liste_1 = [0, 23, 14, -19]


# In[5]:


max(liste_1)


# In[6]:


min(liste_1)


# In[7]:


len(liste_1)


# In[8]:


sum(liste_1)


# In[9]:


liste_2 = [True, True, False]


# In[10]:


all(liste_2) # la fonction " all " nous retourne True quand tous les elements de la liste
# sont egal a True


# In[11]:


any(liste_2) #la fonction " any " nous retourne true quand au moins un element de la liste 
# est egal a true


# In[12]:


any(liste_1)


# # conversion

# In[13]:


x = 10
type(x)


# In[16]:


x = str(x)


# In[17]:


type(x)


# In[18]:


y = " 20 "
y = int(y)


# In[19]:


type(y)


# In[20]:


x = 10
float(10)


# In[21]:


# on peut aussi convertir les listes en Tuple
liste_1 = [0, 61, 63, 243]


# In[22]:


tuple(liste_1)# conversion de la liste en tuple


# In[23]:


tuple_1 = tuple(liste_1)


# In[24]:


list(tuple_1)# reconversion du tuple en liste


# In[25]:


# now avec les dictionaires
inventaire = {
    "bananes": 5000,
    "pommes" : 2000,
    " poires" : 3000
}


# In[26]:


list(inventaire.keys())# ici on obtient les clefs de notre dico sous forme de liste


# # ces autres fonction ne sont pas trop utlisees
# # voyons les quand meme

# In[27]:


bin(15)


# In[28]:


oct(15)


# In[29]:


hex(15)


# In[30]:


input()


# In[31]:


x = input(" entrer un nombre ")


# In[32]:


print(x)


# In[33]:


type(x)


# In[34]:


# convertissons now x en integer
x = int(input(" entrer un nombre "))


# In[35]:


x +5


# # deux fonctionsimportantes pour le data science
# # la fonction format et open

# In[36]:


# la fonction format permet de personaliser les chaines de caractere
# et de les rendres dynamique
message = " la temperature est de 25 degreC a Paris"
print(message)


# In[1]:


x = 30 # des que tu change la valeur de x ou le nom de la ville sa change automatiquement
ville = " Paris "
message = " la temperature est de {} degreC a {} ".format(x, ville)
print(message)


# In[50]:


#ici nous avons creer un dictionaire parametre pour un reseau de neurones tres petits
# avec la techniqe format je peut acceder au differentes couches de mon reseaU de beurones
import numpy as np

parametres = {
    "W1" : np.random.randn(2, 4),
    "b1" : np.zeros((2, 1)),
     "W2" : np.random.randn(2, 2),
    "b2" : np.zeros((2, 1))
}


# In[52]:


for i in range(1,3):
    print("couche", i)
    print(parametres ["W{}".format(i)])


# In[55]:


for i in range(1,3):
    print("couche", i)
    print(parametres ["W" + str(i)])# on a change la derniere ligne et on obtient tjrs le meme
    # resultat


# # now la fonction open qui nous permet d ouvrir ou de creer
# # des fichier et les enregistrer sous un certains nom dans notre
# # ordinateur

# In[2]:


f = open("fichier.txt", "w")# un fichier a ete creer dans mon repertoire de travail
# et lorsque tu l ouvres il contient le message bonjour


# In[3]:


f.write(" bonjour ")
f.close()


# In[4]:


# je peut aussi lire dans ce fichier
f = open(" fichier.txt", "r")
f.read()


# In[64]:


# dans la pratique voila coment n ecrit la plus part du temps dans la pratique
# on a plus besoin d ecrire f.close ici,il suffit juste d aller a la ligne
with open("fichier.txt", "r") as f:
    print(f.read())


# In[68]:


with open("fichier.txt", "w") as f:# ici tu as creer un  fichier mais les resultat ne sont
    # ordonnees
    for i in range(10):
        f.write("{}^2={}".format(i, i**2))


# In[69]:


with open("fichier.txt", "w") as f:
    for i in range(10):
        f.write("{}^2={}\n".format(i, i**2))# avec le symbol \n les resultats serons a la ligne


# # reponse de l exo precedent

# In[70]:


# exercice de 0 a 20
carres_pairs = {
    str(k) : k**2 for k in range(0, 20)
}


# In[71]:


print(carres_pairs)


# In[ ]:




