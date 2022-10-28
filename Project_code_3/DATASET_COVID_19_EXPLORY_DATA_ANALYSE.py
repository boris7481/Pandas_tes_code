#!/usr/bin/env python
# coding: utf-8

# ## COVID-19
# ## 1) EXPLORY DATA ANALYSE
# 

# In[1]:


import numpy as np
import  pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


pd.set_option("display.max_row", 111) # affiche tous les resultats en entier
pd.set_option("display.max_column", 111) # affiche tous les colones du tableaux


# In[3]:


data = pd.read_excel("dataset_covid.xlsx")


# In[4]:


data.head()


# In[5]:


df = data.copy()


# In[6]:


df.shape


# In[7]:


df.dtypes


# In[8]:


df.dtypes.value_counts()


# In[9]:


df.dtypes.value_counts().plot.pie()


# In[10]:


df.isna() # cette foonction verifie si une valeur est NAN


# In[11]:


plt.figure(figsize=(20,10))
sns.heatmap(df.isna(),cbar=False) # pour voir tous notre dataset avec toutes ses 
#lignes et toutes ses colones


# In[12]:


df.isna().sum() # somme des valeurs manquantes que l on retrove dans toutes nos colonnes


# In[13]:


df.isna().sum()/df.shape[0] # on divise par le nombre de ligne de notre tableau
# on obtien un pourcentage


# In[14]:


(df.isna().sum()/df.shape[0]).sort_values(ascending = True)# ici on tri nos valeurs maquantes
# par ordre decroissantes


# ## A nalyse de fond
# ### 1 ellimation des colones inutiles

# In[15]:


df.isna().sum()/df.shape[0]<0.9 # ici on obtient un tableau booleen


# In[16]:


df.columns[df.isna().sum()/df.shape[0]<0.9]# boolean indexing pour identifier dans lesquelles 
# on a moind de 90 pourcent de valeurs manquantes


# In[17]:


df = df[df.columns[df.isna().sum()/df.shape[0]<0.9]]# on fait passer ces colonnes dans notre 
# nouveaux dataframe


# In[18]:


plt.figure(figsize=(20,10))
sns.heatmap(df.isna(),cbar=False) # pour voir tous notre dataset avec toutes ses 
#lignes et toutes ses colones


# In[19]:


df = df.drop("Patient ID", axis=1)# eliminer la colonnes patient ID car ca ne nous sert a rien


# # examen de la colonnes taget

# In[20]:


df["SARS-Cov-2 exam result"].value_counts() # pour compter les valeurs positives et negatives


# In[21]:


df["SARS-Cov-2 exam result"].value_counts(normalize = True)# pour afficher en pourcentage


# # Histogramm des variables continues

# In[22]:


for col in df.select_dtypes("float"):
    print(col)


# In[23]:


for col in df.select_dtypes("float"):
    plt.figure()
    sns.distplot(df[col]) # en observant ces courbes on de rend compte quelles sont centrees 
    # centrees en zero et quelles ont un ecart type egal a un on peut donc conclure que nos
    # donnees ont ete standardisees


# In[24]:


# analysons une autre variable 
sns.distplot(df["Patient age quantile"])


# In[25]:


df["Patient age quantile"].value_counts()


# # Variables quatitatives ou variable de type objet ou variable categorial 

# In[26]:


# on peut encore observer les deux categories qui sont presentent dans notre target
df["SARS-Cov-2 exam result"].unique()# on pouvais aussi use value:count mais je suit le tuto


# In[27]:


for col in df.select_dtypes("object"):
    print( col, df[col].unique())


# In[28]:


for col in df.select_dtypes("object"):
    print(f"{col :-<50} {df[col].unique()}") # pour un meilleur affichage voila la syntaxe
    # on vois qu on a des variables binaires 


# In[29]:


for col in df.select_dtypes("object"):
    plt.figure()
    df[col].value_counts().plot.pie()


# # relation target / variables
# ## creation de sous ensembles positifs et negatifs

# In[30]:


df["SARS-Cov-2 exam result"]=="positive"


# In[31]:


# ici on va faire du boolwan Indexing en reintegrant le code plus haut dans notre dataframe
# c est toujours la meme technique
df[df["SARS-Cov-2 exam result"]=="positive"]


# In[32]:


positive_df = df[df["SARS-Cov-2 exam result"]=="positive"]


# In[33]:


negative_df = df[df["SARS-Cov-2 exam result"]=="negative"]


# # Creation des ensembles Blood et viral

# In[34]:


missing_rate = df.isna().sum()/df.shape[0]


# In[35]:


df.columns[(missing_rate<0.9) & (missing_rate >0.88)]# on obtient toute nos colonnes de type 
# sanguin


# In[36]:


blood_columns = df.columns[(missing_rate<0.9) & (missing_rate >0.88)]


# In[37]:


viral_columns = df.columns[(missing_rate<0.88) & (missing_rate >0.75)]


# ## Visualisation de la relation Target et Blood

# In[38]:


for col in blood_columns:
    plt.figure()
    sns.distplot(positive_df[col], label="positive")
    sns.distplot(negative_df[col], label="negative")
    plt.legend()


# # relation entre la target et l age
# ## on peut proceder de la meme maniere que plus haut mais ici on voir une nouvelle fonction de seaborn important pour le data scientidt aussi
# 

# In[39]:


# ce graphique compte le nombre d apparution de chaque patient age quantile pour les 
# resultats positifs et les resultats negatifs de cette variable : c est un graphique
# tres utile et tres pratique
sns.countplot(x="Patient age quantile", hue = "SARS-Cov-2 exam result", data = df )


# ## visualisation de la relation entre la target et les variables qualitatives
# ## relation target / Viral en utilisant une crosstab (en satistique)

# In[40]:


pd.crosstab(df["SARS-Cov-2 exam result"], df["Influenza A"])


# In[41]:


for col in viral_columns:
    plt.figure()
    sns.heatmap(pd.crosstab(df["SARS-Cov-2 exam result"], df[col]),annot=True, fmt="d")


# ## Analyse plus avancee
# ## relation Variables / Variables
# ## relation taux sanguin

# In[42]:


sns.pairplot(df[blood_columns])


# In[43]:


# Affichons la correlation entre ces variables tres important
# plus une correlation est proche de 1 , plus les deux variables evoluent positivement les uns 
# avec les autres par exemple l Hemoglobin et l Hemtocrit sont fortement correles
sns.heatmap(df[blood_columns].corr())


# In[44]:


# on peut aussi visualiser cela avec la fonction Clustermap de Seaborn
sns.clustermap(df[blood_columns].corr())


# ## Relation Age / Sang

# In[45]:


#La fonction lmplot ,tres importante
for col in blood_columns:
    plt.figure()
    sns.lmplot(x="Patient age quantile" , y=col, hue="SARS-Cov-2 exam result", data=df)


# In[46]:


# affichons la correlation entre les differentes blood_variables(quantitatives)
#ici on affiche toutes les variables mais on peut filtrere cela en selectionant juste la
# variable age
df.corr()


# In[47]:


# ici on affiche juste la correlation avec l age quantile
# on se rend compte que les coefficients de correlation les plus eleves atteigne a peine
# 0.281655 c est tres petit donc pas besoin d emettre des hypotheses ici
df.corr()["Patient age quantile"]


# In[48]:


# on se rend compte que les coefficients de correlation les plus eleves atteigne a peine
# 0.281655 c est tres petit donc pas besoin d emettre des hypotheses ici
df.corr()["Patient age quantile"].sort_values()


# ## relation entre influenza et rapid test

# In[49]:


pd.crosstab(df["Influenza A"], df["Influenza A, rapid test"])


# In[50]:


pd.crosstab(df["Influenza B"], df["Influenza B, rapid test"])


# ## relation viral / sanguin
# ## creation d une nouvelle variable "est malade"

# In[51]:


df[viral_columns[:-2]] == "detected" # cette ecriture elimine les deux dernieres colonnes


# In[52]:


np.sum(df[viral_columns[:-2]] == "detected",axis=1) # pour voir s il ya des gens qui on une 
# ou plusieurs maladie


# In[53]:


np.sum(df[viral_columns[:-2]] == "detected",axis=1).plot()


# In[54]:


np.sum(df[viral_columns[:-2]] == "detected",axis=1)>=1 # pour nous indiquer si la personne 
# est teste positive


# In[55]:


# Inserons ce tableau dans une nouvelle variable appellee "est malade"
df["est malade"] = np.sum(df[viral_columns[:-2]] == "detected",axis=1)>=1 


# In[56]:


df.head()


# In[57]:


# Visulisons la relation entre la variable "est malade" et les differents tests sanguin
malade_df = df[df["est malade"]== True]
non_malade_df = df[df["est malade"]== False]


# In[58]:


# on obtient des graphiques pour d autres maladies respiratoire mais pas pour le COVID car 
# c etait notre objectif
for col in blood_columns:
    plt.figure()
    sns.distplot(malade_df[col], label="malade")
    sns.distplot(non_malade_df[col], label="non malade")
    plt.legend()


# In[59]:


def hospitalisation(df):
    if df["Patient addmited to regular ward (1=yes, 0=no)"]== 1:
        return "surveillance"
    elif df["Patient addmited to semi-intensive unit (1=yes, 0=no)"]==1:
        return "soins semi-intensives"
    elif df["Patient addmited to intensive care unit (1=yes, 0=no)"]== 1:
        return "soins intensifs"
    else:
        return "inconnu"


# In[60]:


df["statut"]= df.apply(hospitalisation,axis = 1)# ajout d une no'uvelle colonne "satut"


# In[61]:


df.head()


# In[62]:


for col in blood_columns:
    plt.figure()
    for cat in df["statut"].unique():
        sns.distplot(df[df["statut"]==cat][col],label=cat)# ici il y a le boolean indexing
    plt.legend()
    


# In[63]:


# nous avons actuelement deux types de variables dans notre dataset,les blood_columns et
#les viral_columns
blood_columns


# In[64]:


viral_columns


# In[65]:


df.dropna().count()# on vois qu il nous reste 99 valeurs par colonnes dans notre dataset
#sur les 5600 a peu pres du depart ce qui n est paa tres bien donc il va falloir travailler
# avec des valeurs manquantes 


# In[66]:


df[blood_columns].count()# voila le nombre de valeurs qui nous restera si on travail juste 
# avec les nlood_columns : environ 603


# In[67]:


df[viral_columns].count() # oila le nombre de valeurs qui nous restera si on travail juste 
# avec les viral_olumns : environ 1354


# In[68]:


df1 = df[viral_columns[:-2]]
df1["covid"]= df["SARS-Cov-2 exam result"]
df1.dropna()["covid"].value_counts(normalize=True)


# In[69]:


# les proportions ici sont meilleurs  c a d un peu plus balancees
df1 = df[blood_columns[:-2]]
df1["covid"]= df["SARS-Cov-2 exam result"]
df1.dropna()["covid"].value_counts(normalize=True)


# ## T-test

# In[70]:


from scipy.stats import ttest_ind


# In[71]:


positive_df.shape


# In[72]:


negative_df.shape


# In[73]:


negative_df.sample(550)


# In[74]:


negative_df.sample(positive_df.shape[0])


# In[75]:


balanced_neg = negative_df.sample(positive_df.shape[0])


# In[76]:


def t_test(col):
    alpha = 0.02
    stat,p = ttest_ind(balanced_neg[col].dropna(), positive_df[col].dropna())
    if p < alpha:
        return "HB rejetee"
    else:
        return 0
    


# In[77]:


for col in blood_columns:
    print(f"{col :-<50} {t_test(col)}")# il faut ecrire -<50 tous cela coller pour que 
    # ca marche


# ## tous ce code est present dans le github de guillaume juste au cas ou

# In[ ]:





# In[ ]:




