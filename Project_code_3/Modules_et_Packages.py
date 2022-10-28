#!/usr/bin/env python
# coding: utf-8

# # les modules de base les plus important pour demarer

# In[1]:


import math
import random
import statistics
import os # os = operating system
import glob


# In[2]:


print(math.pi)


# In[3]:


math.exp(5)
math


# In[4]:


print(math.exp(5))


# In[6]:


liste_1 =[0, 1, 3, 5, 10]

print(random.choice(liste_1)) # la fonction random veut dire aleatoire


# In[7]:


print(random.choice(["jean", "jule", "pierre"]))


# In[10]:


# mais en general en data science on aime avoir de l aleatoire qu on peut maitriser c est a 
# dire reproduire et pour cela on use la fonction seed
print(random.seed(0))


# In[13]:


print(random.randint(5,10))


# In[14]:


print(random.randrange(100))


# In[18]:


print(random.sample(range(100),10))


# # now le module os

# In[19]:


# pour savoir par exemple dans quel fichier nous travaillons actuelement
#on peut use la fonction suivante
os.getcwd() #cwd = current working directly cad l endoit ou je travail now 


# # le module glob

# In[20]:


glob.glob("*") # cette fonction nous retourne tous les noms des fichiers que l on a dans notre 
          # repertoire de travail


# In[21]:


print(glob.glob("*"))


# In[22]:


print(glob.glob("*.txt"))# ici je veut imprimer tous les fichiers qui se terminent par txt


# In[23]:


filenames = glob.glob("*.txt")

for file in filenames:# on aura le contenu des differents fichiers txt qui serons afficher
    with open(file, "r") as f:
        print(f.read())


# # reponse de l exodu tuto precedent 7-20
# 

# In[25]:


with open("fichier.txt", "r") as f: # en executant ce code j ai d abord eu une fehlermeldung
    # il fallait juste que je diminu les espaces entre les hauts guillemets pour que 
    # ca fonctione
    liste = f.readlines()
liste


# In[27]:


# noe tu remarque qu il ya les symbols \n a la fin
# voici ce qu il fat faire pour s en debarasser
with open("fichier.txt", "r") as f: #
    liste = f.read().splitlines()
liste


# # voici aussi une autre solution en usant les liste comprehension

# In[32]:


liste = [line for line in open("fichier.txt", "r")]
liste


# In[33]:


# on se rend compte que l on encor le meme pb que plus haut avec le symbol \n
# on va use une autre astuce pour le resoudre
liste = [line.strip() for line in open("fichier.txt", "r")]
liste


# In[ ]:




