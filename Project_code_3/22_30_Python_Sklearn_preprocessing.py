#!/usr/bin/env python
# coding: utf-8

# ## 22_30_Python_Sklearn_preprocessing tres important pour un Datascientist car il represent 80 pourcent du travail d un Data Scientist

# In[25]:


import numpy as np
from sklearn.preprocessing import LabelEncoder


# In[3]:


y = np.array(["chat", "chien", "chat", "oiseau"])


# In[5]:


encoder = LabelEncoder()
encoder.fit(y)


# In[7]:


encoder.classes_


# In[8]:


encoder.transform(y)


# In[9]:


# pour aller plus vite on peut use la methode 
encoder = LabelEncoder()
encoder.fit_transform(y)


# In[10]:


# on peut egalement appliquer la methode inverse pour revoir nos vraie valeurers
encoder.inverse_transform(np.array((0, 0, 2,2)))


# In[17]:


X = np.array(
  [["chat", "poils"],
   ["chien", "poils"],
   ["chat", "poils"],
   ["oiseau", "plumes"]])


# In[26]:


from sklearn.preprocessing import OrdinalEncoder
encoder = OrdinalEncoder()
encoder.fit_transform(X)


# In[29]:


from sklearn.preprocessing import LabelBinarizer
encoder = LabelBinarizer()
encoder.fit_transform(y)


# In[39]:


from sklearn.preprocessing import LabelBinarizer
encoder = LabelBinarizer(sparse_output=True)
encoder.fit_transform(y)


# ## Now l une des etapes les plus importantes en Datas Science est la Normalisation

# ## 1 la normalisation min max

# In[40]:


from sklearn.preprocessing import MinMaxScaler


# In[44]:


Z = np.array([[70],
             [80],
             [120]])


# In[46]:


scaler = MinMaxScaler() ### tres important de comprendre cette transformation car elle conserve
   ### les ecarts dans nos matrices bien que les valeurs internes soient differentes
scaler.fit_transform(Z)


# In[47]:


Z_test = np.array([[90]])
scaler.transform(Z_test)

