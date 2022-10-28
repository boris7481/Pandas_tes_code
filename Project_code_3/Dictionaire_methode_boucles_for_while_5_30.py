#!/usr/bin/env python
# coding: utf-8

# In[7]:


traduction = {
    " chien " : " dog ",
    " chat " : " cat ",
    " souris " : " mouse ",
    " oiseau " : " bird "
}
# tres important de savoir que dans un dico on ne peut pas avoir la meme clef deux fois chacune est unique
#par exemple je ne peut pas recreer  la clef oiseau deux fois mais la valeur bird je apparaitre plusieur fois
# dans mon dico


# In[2]:


inventaire = {
    " bananes " : 500,
    " pommes " : 200,
    " poires " : 300,
    " serises " : 400
}
inventaire


# In[3]:


inventaire.values()


# In[4]:


inventaire.keys()


# In[5]:


len(inventaire)


# In[13]:


# on peut creer une nouvelle clef et une nouvelle valeur associe a cette clwf
inventaire[" abricots "] = 500
inventaire # dans un dictionaire il n ya pas d ordre comme dans les liste cad il n xa pas de 
# debut pas de fin


# In[10]:


# essayons toute meme de use certaines methodes comme get pour voir
inventaire.get(" peches ")


# In[11]:


# en realite ca n a rien retourne car il n ya pas de peches dans mon dico inventaire
# maintenant imprimons ce mot a l ecran " none" qui veut dire rien
print(inventaire.get(" peches "))


# In[12]:


# je peut egalement retouner une valeur par defaut dans notre methode get
print(inventaire.get(" peches ", 1))


# In[27]:


# essayons maintenat de retourner la valeur des serises la valeur par defaut "1" ici
# ne joue aucun role
print(inventaire.get(" serises ", 1))


# In[28]:


# utilisons now la methode " fromkeys " elle nous permet de creer un dico toutes entier
# a partir d une liste de clef que l on fournit
liste_1 = ("paris ", " londres ", " berlin" )
inventaire.fromkeys(liste_1)


# In[29]:


# bien voir que plus haut je n ai pas donne de valeur a mes clef c est pouquoi j ai 
# " none" par defaut qui veut dire rien
# je peut donner une valeur par defaut a mes differents clefs
inventaire.fromkeys(liste_1, 150)


# In[62]:


# utilisons now la boucle " for " dans les dictionaire
# ici nous avons juste afficher les clef
for i in inventaire:
    print(i)


# In[63]:


ici nous avons juste afficher les valeurs des clefs
for i in inventaire.values():
    print(i)


# In[64]:


# pour( afficher les clefs et les valeurs on va use la methode " items "
for k,v in inventaire.items():
    print(k, v)


# In[69]:


# reponse a l exo du dernier Tuto
def fibonacci(n):
    a = 0
    b = 1
    fib = [a]
    while b< n:
        a, b = b, a+b
        fib.append(a)
    return fib
print(fibonacci(1000))   


# In[ ]:




