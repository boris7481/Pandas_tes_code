#!/usr/bin/env python
# coding: utf-8

# ##### 14-2-1. Numéro 1
# #### Écrire un programme qui, à partir de la saisie d'un rayon et d'une hauteur, calcule le volume d'un cône droit.
# 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import math


# In[6]:


def volume_cone(rayon , hauteur):
    rayon = float(input())
    print(" der wer Wert von dem Rdius ist :", rayon)
    hauteur = float(input())
    print(" der wer Wert von der höhe ist :", hauteur)
    Volume = (rayon**2 * math.pi * hauteur)/3.0
    print(f" das Volumen ist :", Volume)


# In[7]:


volume_cone(10,23)


# ### Numéro 2
# 
# #### Une boucle while : entrez un prix HT (entrez o pour terminer) et affichez sa valeur TTC.
# 

# ### Numéro 3
# 
# #### Une autre boucle while : calculez la somme d'une suite de nombres positifs ou nuls. Comptez combien il y avait de données et combien étaient supérieures à 100.
# 
# #### Entrer un nombre inférieur ou égal à 0 indique la fin de la suite.
# 

# In[11]:


# -*- coding : utf8 -*-
"""Somme d'entiers et nombre d'entiers supérieurs à 100."""

# Programme principal =========================================================
somme, nombreTotal, nombreGrands = 0, 0, 0

x = int(input("x (0 pour terminer) ?"))
while x > 0:
    somme += x
    nombreTotal += 1
    if x > 100:
        nombreGrands += 1
    x = int(input("x (0 pour terminer) ?"))

print("\nSomme :", somme)
print(nombreTotal, "valeur(s) en tout, dont", nombreGrands, "supérieure(s) à 100")


# ### Numéro 4
# 
# #### L'utilisateur donne un entier positif n
# #### et le programme affiche PAIR s'il est divisible par 2, IMPAIR sinon.

# ### Numéro 5
# 
# #### L'utilisateur donne un entier positif et le programme annonce combien de fois de suite cet entier est divisible par 2.
# 

# In[12]:


# -*- coding : utf8 -*-
"""Nombre de fois qu'un entier est divisible par 2."""

# Programme principal =========================================================
n = int(input("Entrez un entier strictement positif :"))
while n < 1:
    n = int(input("Entrez un entier STRICTEMENT POSITIF, s.v.p. :"))
save = n

cpt = 0
while n%2 == 0:
    n /= 2
    cpt += 1

print(save, "est", cpt, "fois divisible par 2.")


# Numéro 8
# 
# 
# Un gardien de phare va aux toilettes cinq fois par jour. Or les WC sont au rez-de-chaussée…
# 
# Écrire une procédure (donc sans return) hauteurParcourue qui reçoit 
# deux paramètres, le nombre de marches du phare et la hauteur 
# de chaque marche (en cm), et qui affiche :

# In[31]:


def hauteurParcourue(nb , h):
     print("Pour {} marches de {} cm, il parcourt {} m par semaine !"
           .format(nb, h, nb*h*2*5*7/100.0))

#        Programme principal =========================================================

nbMarches = int(input("Combien de marches ?"))
hauteurMarche = int(input("Hauteur d'une marche (cm) ?"))

hauteurParcourue(nbMarches, hauteurMarche)


# In[32]:


nbMarches = int(input("Combien de marches ?"))
hauteurMarche = int(input("Hauteur d'une marche (cm) ?"))


def hauteurParcourue(nb , h):
     print("Pour {} marches de {} cm, il parcourt {} m par semaine !"
           .format(nb, h, nb*h*2*5*7/100.0))

#        Programme principal =========================================================


hauteurParcourue(nbMarches, hauteurMarche)


#  Numéro 11 ?
# ▲
# 
# Un programme principal saisit une chaîne d'ADN valide et une séquence d'ADN valide (valide signifie qu'elles ne sont pas vides et sont formées exclusivement d'une combinaison arbitraire de "a", "t", "g" ou "c").
# 
# Écrire une fonction valide qui renvoie vrai si la saisie est valide, faux sinon.
# 
# Écrire une fonction saisie qui effectue une saisie valide et renvoie la valeur saisie sous forme d'une chaîne de caractères.
# 
# Écrire une fonction proportion qui reçoit deux arguments, la chaîne et la séquence et qui retourne la proportion de séquence dans la chaîne (c'est-à-dire son nombre d'occurrences).
# 
# Le programme principal appelle la fonction saisie pour la chaîne et pour la séquence et affiche le résultat.
# 
# Exemple d'affichage :
#  
# Sélectionnez
# 
# chaîne : attgcaatggtggtacatg
# séquence : ca
# Il y a 10.53 % de "ca" dans votre chaîne.
# 
# 

# In[39]:


# -*- coding : utf8 -*-
"""Proportion d'une séquence dans une chaîne d'ADN."""

# Définition de fonction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def valide(seq) :
    """Retourne vrai si la séquence est valide, faux sinon."""
    ret = any(seq)
    for c in seq :
        ret = ret and c in "atgc"
    return ret

def proportion(a, s) :
    """Retourne la proportion de la séquence <s> dans la chaîne <a>."""
    return 100*a.count(s)/len(a)

def saisie(ch) :
    s = input("{} :".format(ch))
    while not valide(s) :
        print("'{}' ne peut contenir que les chaînons 'a', 't', 'g' et 'c'"
              " et ne doit pas être vide".format(ch))
        s = input("{} :".format(ch))
    return s

# Programme principal =========================================================
adn = saisie("chaîne")
seq = saisie("séquence")

print('Il y a {} % de"{}" dans votre chaîne.'.format(proportion(adn, seq), seq))


# . Numéro 12
# 
# Il s'agit d'écrire, d'une part, un programme principal et, d'autre part, une fonction utilisée 
# dans le programme principal.
# 
# La fonction listAleaInt(n, a, b) retourne une liste de n entiers aléatoires dans [a .. b] en utilisant 
# la fonction randint(a, b) du module random.
# 
# Dans le programme principal :
# 
#     construire la liste en appelant la fonction listAleaInt() ;
#     calculer l'index de la case qui contient le minimum ;
#     échangez le premier élément du tableau avec son minimum.
# 
# 

# In[49]:


### Echanger ###

from random import seed , randint

def listAleaInt(n, a, b) :
    return [randint(a,b) for i in range(n)]

# Programme principal
seed() # initialise le générateur de nombres aléatoires

t = listAleaInt(100,2,125) # construction de la liste

iMin  = t.index(min(t))

print("avant echange : ")
print("\tt[0] =", t[0], "\tt[iMin] =", t[iMin])
t[0], t[iMin] = t[iMin], t[0] # échange
print("Apres échange :")
print("\tt[0] =", t[0], "\tt[iMin] =", t[iMin])


#  Numéro 13
# 
# 
# Comme précédemment, il s'agit d'écrire, d'une part, un programme principal et, d'autre part, une fonction utilisée dans le programme principal.
# 
# La fonction listAleaFloat(n) retourne une liste de n flottants aléatoires en utilisant la fonction random() du module random.
# 
# Dans le programme principal :
# 
#     saisir un entier n dans l'intervalle : [2 .. 100] ;
#     construire la liste en appelant la fonction listAleaFloat() ;
#     afficher l'amplitude du tableau (écart entre sa plus grande et sa plus petite valeur) ;
#     afficher la moyenne du tableau.
# 
# 

# In[57]:


"""Amplitude et moyenne d'une liste de flottants."""

from random import seed, random

# Définition de fonction

def listAleaFloat(n) :
    "Retourne une liste de <n> flottants aléatoires"
    return [random() for i in range(n)]

# Programme principal
n = int(input("Entrez un entier [2 .. 100] :"))
while not(n >= 2 and n <= 100) :
    n = int(input("Entrez un entier [2 .. 100], s.v.p. :"))

seed() # initialise le générateur de nombres aléatoires
t = listAleaFloat(n) # construction de la liste

print(" Amplitude ist {}".format(max(t)- min(t)))
print(" moyenne ist {}".format(sum(t)/n))


# In[58]:


"""Amplitude et moyenne d'une liste de flottants."""

from random import seed, random

# Définition de fonction

def listAleaFloat(n) :
    "Retourne une liste de <n> flottants aléatoires"
    return [random() for i in range(n)]

# Programme principal
n = int(input("Entrez un entier [2 .. 100] :"))
while (n >= 2 and n <= 100) :
    n = int(input("Entrez un entier [2 .. 100], s.v.p. :"))

seed() # initialise le générateur de nombres aléatoires
t = listAleaFloat(n) # construction de la liste

print(" Amplitude ist {}".format(max(t)- min(t)))
print(" moyenne ist {}".format(sum(t)/n))


#  Numéro 14
# ▲
# 
# Fonction renvoyant plusieurs valeurs sous forme d'un tuple.
# 
# Écrire une fonction minMaxMoy() qui reçoit une liste d'entiers et qui renvoie le minimum, le maximum et la moyenne de cette liste. Le programme principal appellera cette fonction avec la liste : [10, 18, 14, 20, 12, 16].
# 

# In[64]:


# -*- coding : utf8 -*-
"""Min, max et moyenne d'une liste d'entiers."""

# Définition de fonction ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def minMaxMoy(liste) :
    """Renvoie le min, le max et la moyenne de la liste."""
    min, max, som = liste[0], liste[0], float(liste[0])
    for i in liste[1:]:
        if i < min :
            min = i
        if i > max :
            max = i
        som += i
    return (min, max, som/len(liste))

# Programme principal =========================================================
lp = [10, 18, 14, 20, 12, 16]

print("liste =", lp)
l = minMaxMoy(lp)
print("min : {0[0]}, max : {0[1]}, moy : {0[2]}".format(l))


# . Numéro 15
# ▲
# 
# Saisir un entier entre 1 et 3999 (pourquoi cette limitation ?). L'afficher en nombre romain.
# 

# In[ ]:





# In[ ]:




