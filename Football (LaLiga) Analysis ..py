#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')
# suppress warnings from final output
import warnings
warnings.simplefilter("ignore")

# set up to view all the info of the columns
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# In[27]:


laliga_df = pd.read_csv('laliga_player_stats_english.csv')


# In[21]:


laliga_df.head()


# In[28]:


laliga_df.info()


# In[29]:


laliga_df.describe()


# In[42]:


laliga_df['MinsPerMatch'] = (laliga_df['Minutes played'] / laliga_df['Games played']).astype(float)
laliga_df['GoalsPerMatch'] = (laliga_df['Goals scored'] / laliga_df['Games played']).astype(float)

laliga_df.head()


# In[40]:


Total_goals = laliga_df['Goals scored'].sum()
print(Total_goals)


# In[43]:


Total_PenaltyGoals = laliga_df ['Penalties scored'].sum()
print(Total_PenaltyGoals)


# In[46]:


Total_Penaltyattempts =laliga_df ['Penalties given away'].sum()
print(Total_Penaltyattempts)


# In[54]:


plt.figure(figsize=(13,6))
pl_not_scored = laliga_df ['Penalties given away'].sum() - Total_PenaltyGoals
data=[pl_not_scored,Total_PenaltyGoals]
labels=['Penalties missed','Penalties Scored']
color = sns.color_palette('Set1')
plt.pie(data ,labels=labels,colors=color,autopct='%.0f%%')
plt.show()


# In[55]:


#Players unique positions
laliga_df['Position'].unique()


# In[56]:


laliga_df[laliga_df['Position']=='Forward']


# In[62]:


laliga_df['Team'].value_counts().nlargest(5).plot(kind = 'bar',color = sns.color_palette("magma"))


# In[63]:


laliga_df['Team'].value_counts().nsmallest(5).plot(kind = 'bar',color = sns.color_palette("magma"))


# In[68]:


Assists_by_clubs = pd.DataFrame(laliga_df.groupby('Team',as_index=False)['Assists'].sum())
sns.set_theme(style="whitegrid",color_codes=True)
ax=sns.barplot(x='Team',y='Assists',data=Assists_by_clubs.sort_values(by="Assists"),palette='magma')
ax.set_xlabel("Team",fontsize=30)
ax.set_ylabel("Assists",fontsize=20)
plt.xticks(rotation=75)
plt.rcParams["figure.figsize"] = (20,8)
plt.title('Plot of Teams vs Total Assists',fontsize = 20)


# In[70]:


top_10_assists = laliga_df[['Name','Team','Assists','Games played']].nlargest(n=15 , columns ='Assists')
top_10_assists


# In[73]:


Goals_by_clubs = pd.DataFrame(laliga_df.groupby('Team',as_index=False)['Goals scored'].sum())
sns.set_theme(style="whitegrid",color_codes=True)
ax=sns.barplot(x='Team',y='Goals scored',data=Goals_by_clubs.sort_values(by="Goals scored"),palette='Set2')
ax.set_xlabel("Team",fontsize=30)
ax.set_ylabel("Goals",fontsize=20)
plt.xticks(rotation=75)
plt.rcParams["figure.figsize"] = (20,8)
plt.title('Plot of Teams vs Total Goals scored',fontsize = 20)


# In[75]:


top_10_goals = laliga_df[['Name','Team','Goals scored','Games played']].nlargest(n=10 , columns ='Goals scored')
top_10_goals


# In[ ]:




