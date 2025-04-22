#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('awards.csv')


# In[3]:


print(df.columns)
df.head()


# In[4]:


#Number of Awards per Year
plt.figure(figsize=(8,5))
df['year'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Number of Awards per Year')
plt.xlabel('Year')
plt.ylabel('Number of Awards')
plt.xticks(rotation=0)
plt.show()


# In[6]:


#Count of Awards per Category
plt.figure(figsize=(10,6))
df['category'].value_counts().plot(kind='barh', color='orange')
plt.title('Number of Awards per Category')
plt.xlabel('Count')
plt.ylabel('Category')
plt.show()


# In[7]:


#Top 10 Most Nominated Artists
plt.figure(figsize=(10,6))
df['artist'].value_counts().head(10).plot(kind='bar', color='green')
plt.title('Top 10 Most Nominated Artists')
plt.xlabel('Artist')
plt.ylabel('Nominations')
plt.xticks(rotation=45)
plt.show()


# In[8]:


#Number of Wins vs Nominations
plt.figure(figsize=(6,6))
df['winner'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['#66b3ff','#ff9999'], labels=['Win', 'Nomination'])
plt.title('Wins vs Nominations')
plt.ylabel('')
plt.show()


# In[9]:


#Distribution of Nominations by Year
plt.figure(figsize=(10,6))
sns.boxplot(x='year', y='year', data=df)
plt.title('Distribution of Nominations by Year')
plt.show()


# In[10]:


#Most Frequent Workers (Top 10)
from collections import Counter

# Flatten all workers into a single list
all_workers = df['workers'].dropna().str.split(', ').sum()
top_workers = Counter(all_workers).most_common(10)

# Plot
plt.figure(figsize=(10,6))
worker_names, counts = zip(*top_workers)
plt.bar(worker_names, counts, color='purple')
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Most Frequent Workers')
plt.ylabel('Count')
plt.show()


# In[11]:


#Number of Awards by Nominee
plt.figure(figsize=(12,6))
df['nominee'].value_counts().head(10).plot(kind='bar', color='teal')
plt.title('Top 10 Nominees')
plt.xlabel('Nominee')
plt.ylabel('Number of Awards')
plt.xticks(rotation=45)
plt.show()


# In[12]:


#Winners by Category
plt.figure(figsize=(12,6))
sns.countplot(data=df[df['winner']==True], y='category', order=df['category'].value_counts().index, palette='cool')
plt.title('Winners by Category')
plt.xlabel('Count')
plt.ylabel('Category')
plt.show()


# In[13]:


#Award-Winning Artists by Year
plt.figure(figsize=(10,6))
winners_per_year = df[df['winner']==True].groupby('year')['artist'].nunique()
plt.plot(winners_per_year.index, winners_per_year.values, marker='o', linestyle='-', color='crimson')
plt.title('Unique Winning Artists per Year')
plt.xlabel('Year')
plt.ylabel('Number of Unique Winning Artists')
plt.grid(True)
plt.show()


# In[14]:


#Win Rate per Artist (Top 10 by Nominations)
artist_counts = df.groupby('artist')['winner'].agg(['count', 'sum'])
artist_counts['win_rate'] = artist_counts['sum'] / artist_counts['count']
top10 = artist_counts.sort_values('count', ascending=False).head(10)

plt.figure(figsize=(10,6))
top10['win_rate'].plot(kind='bar', color='gold')
plt.title('Win Rate of Top 10 Most Nominated Artists')
plt.ylabel('Win Rate')
plt.xticks(rotation=45)
plt.show()


# In[15]:


df_corr = df.copy()
df_corr['winner'] = df_corr['winner'].astype(int)
df_corr['year'] = pd.to_numeric(df_corr['year'], errors='coerce')

plt.figure(figsize=(6,4))
sns.heatmap(df_corr[['year', 'winner']].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()


# In[ ]:




