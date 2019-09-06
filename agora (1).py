#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_excel("dados.xlsx")


# In[3]:


ae = pd.ExcelFile("dados.xlsx")


# In[4]:


aba1 = ae.parse('orcado')


# In[5]:


aba2 = ae.parse('realizado')


# In[6]:


arq2 = pd.DataFrame(aba2)


# In[7]:


arqt = arq2.T


# In[8]:


arqt.columns = ['mês', 'Realizado']


# In[9]:


res = pd.merge(aba1, arqt, on="mês")


# In[14]:


res["orcado"].plot.bar()
res["Realizado"].plot.bar(color="orange")

plt.title('Gráfico Orçamento')
plt.xlabel('Mês')
plt.ylabel('$')
plt.legend()
meses = "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
locs, labels=plt.xticks()
plt.xticks(locs,meses, rotation=45, horizontalalignment='right')
plt.rcParams['figure.figsize'] = (15,11)
plt.savefig('nova_figura.png')


# In[11]:


res["diff"] = res["orcado"]-res["Realizado"]


# In[12]:


res.to_csv('novo_arquivo.csv')

