#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 


# In[2]:


A = np.array([[2, 5, 6],
             [5, 5, 6],
             [4, 6, 8]])
A


# In[3]:


A[0 , 1]
A.min()


# In[4]:


A<10


# In[5]:


A[A<10]=2
A


# In[6]:


A.shape


# In[7]:


A.sum( axis = 0)


# In[8]:


A.mean(axis = 0)


# In[9]:


B = [2 , 4, 6]
B


# In[10]:


C = {"boris" :1,
     "thibaut ":2,
     "tondjua" :3}
C


# In[11]:


C["boris"]


# In[12]:


C["boris"] = 10


# In[13]:


C


# In[14]:


C.values()


# In[15]:


C.keys()


# In[16]:


C.items()


# In[17]:


C["junior"] = 50
C


# In[18]:


E = ({"boris" :1, "thibaut ":2,
     "tondjua" :3, "emo" : 40,
      "figo" : 20 , "davila" : 60}
)


# In[19]:


E


# In[20]:


E["papi"] = 100


# In[21]:


E


# In[22]:


for k,v in E.items():
    #print("k" + k)
    #print("v" + v)
    print(k,v)


# In[23]:


for k,v in E.items():
    print("\n k" + k)
    print("v" + str(v))
    


# In[24]:


for i in E.keys():
    
    print("keys" + " " +(i)+" " + "ist good")


# In[25]:


for i in E.values():
    
    print("keys" + " " +str(i)+" " + "ist good")


# In[26]:


C = {"boris" :1, "thibaut ":2, "tondjua" :3}
C


# In[27]:


C_0 = {"hermann" :1, "alex":2, "bebi" :3}
C_1 = {"emo" :1, "thibaut":2, "tondjua" :3}
C_2 = {"doudou" :1, "boris":2, "tondjua" :3}


# In[28]:


D = [C_0, C_1, C_2]
D


# In[29]:


F = ["boris", "junior", "tondjua", "thibaut"]


# In[30]:


for i in F:
    print(i, "ist gut")


# In[31]:


F[1:3]


# In[32]:


F[:2]
    


# In[33]:


F[:]


# In[34]:


E


# In[35]:


G = pd.Series(E)
G


# In[36]:


G["boris"]


# In[37]:


X = pd.Series([10, 20, 30, 40, 50, 60, 70])
X


# In[38]:


Y = pd.DataFrame(E, X)
Y


# In[39]:


df = Y
df


# In[40]:


df.shape


# In[41]:


df.loc[10:20]


# In[42]:


df[10:20]


# In[43]:


df.index[0]


# In[44]:


df["pipo"]=" berto"
df


# In[45]:


df["kabi"] = "carine"


# In[46]:


df


# In[47]:


df["boris"]


# In[48]:


df["alex"]= df["emo"]/df["figo"]


# In[49]:


df


# In[51]:


rang = np.random.RandomState(42)
ser = pd.Series(rang.randint(0, 10, 4))


# In[52]:


ser


# In[53]:


df.dropna()


# In[56]:


df_2 = pd.DataFrame([[1, np.nan, 2],
                     [3, 3, 5],
                    [np.nan, 4, 6]])


# In[57]:


df_2


# In[58]:


df_2.dropna()# par defaut j enleve toutes les lignes ayant le nan


# In[60]:


df_2[3] = np.nan
df_2


# In[63]:


df_2.dropna(axis = "columns", how = "all")


# In[64]:


df_2.dropna(axis = "columns", how = "any")


# In[65]:


df_2.dropna(axis = "rows", how = "any")


# In[66]:


df_2.dropna(axis = "rows", how = "all")


# In[68]:


df_2.fillna


# In[69]:


df_2.fillna(0)# remplacw les nan par des zeros


# In[73]:


x = [2, 3, 4]
y = [6, 8, 10]
z = [1, 2, 3]
np.concatenate([x,y,z])


# In[76]:


df_3 = pd.concat([df, df_2])# suivant les lignes 


# In[77]:


df_3


# In[83]:


df_3.shape


# In[80]:


df_4 = pd.concat([df, df_2], axis = 1)# suivant les colonnes


# In[81]:


df_4


# In[101]:


df_4.shape


# In[102]:


df_5 = pd.concat([df, df_2], join = "outer" )


# In[103]:


df_5


# In[113]:


df_5.isna()


# In[115]:


df_5.isna().sum()


# In[117]:


df_5.isna().sum()/df_5.shape[0]


# In[123]:


df_5.isna().sum()/df_5.shape[0]<0.7 # obtention d un mask


# In[132]:


df_6 = df_5.columns[df_5.isna().sum()/df_5.shape[0]<0.7]
df_6


# In[127]:


df_5.dtypes


# In[128]:


plt.figure(figsize=(20,10))
sns.heatmap(df_5.isna(),cbar=False)


# In[129]:


df_5.dtypes.value_counts()


# In[130]:


df_5.dtypes.value_counts().plot.pie()


# In[144]:


df_5.describe()


# In[146]:


df_5


# In[147]:


df_5.groupby("alex")


# In[148]:


df_5.groupby("alex").sum()


# In[149]:


df_5.groupby("boris").sum()


# In[150]:


df_5["kabi"].unique()


# In[151]:


df_5["pipo"].unique()


# In[152]:


for col in df.select_dtypes("object"):
    print( col, df[col].unique())


# In[153]:


for col in df.select_dtypes("float"):
    print( col, df[col].unique())


# In[154]:


df_5["alex"].unique()


# In[156]:


get_ipython().run_line_magic('pinfo', 'unique')


# In[157]:


get_ipython().run_line_magic('pinfo', 'square')


# In[ ]:




