#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 11:49:44 2020

@author: simplon
"""

## 1. Lire le fichier
import pandas

df=pandas.read_csv('/home/simplon/Téléchargements/Netflix/netflix_titles.csv',index_col=0)
print(df.head())

## 2. Afficher les dimensions du dataframe
df.shape

## 3. Compter les films et les séries
resultat = df["type"].value_counts()
print(resultat)


## 4. Générer le résumé statistique du dataframe
print(df.describe(include="all"))


## 5. Compter les valeurs manquantes
dfvaleur = df.isna()
dfvaleur.sum()

## 6. Explorer les valeurs manquantes

## A.

df1 = df.loc[df['director'].isna()==True]
print(df1['type'].value_counts())

## B.

df2 = df.loc[df['cast'].isna()==True]
print(df2['listed_in'].value_counts().head(10))

## 7. Supprimer les lignes dupliquées

data = df.duplicated()
print(data)
data2 = df.drop_duplicates()
print(data2)

## 8. Compter les films/séries produits par les États-Unis et par la France

FilmFrance = df[(df["country"]=="France")]
print(FilmFrance.shape)
FilmUS = df[(df["country"]=="United States")]
print(FilmUS.shape)

## seaborn

# 9. Afficher le contenu le plus vieux disponible sur Netflix

OldestFilm = df[(df["release_year"]==df["release_year"].min())]
print(OldestFilm['title'])

# 10. Afficher le film avec la durée la plus longue sur Netflix
# a. Nouvelle notion : les méthodes str
# b. Énoncé

data_movies = data.loc[data.type == 'Movie']
duree = pd.Series(data_movies['duration']).str.replace(" min", "").astype('int').sort_values(ascending=False).head(5)
print(duree)


# Affiche les 5 films avec toutes les infos

data["duration"] = pd.Series(data_movies['duration']).str.replace(" min", "").astype('int')
data_film_duration_2 = data.sort_values(by='duration', ascending=False).head(5)[["title", "duration"]]
print(data_film_duration_2)

## 11. Étudier les catégories avec le plus de contenu.

import pandas as pd
donnees=pd.read_csv("/home/simplon/Téléchargements/Netflix/netflix_titles.csv",
index_col=[0])
donnees["listed_in"].head()
", ".join(donnees["listed_in"].dropna())

donnees=pd.read_csv("/home/simplon/Téléchargements/Netflix/netflix_titles.csv",
index_col=[0])
donnees["listed_in"].head()
categories=pd.Series(", ".join(donnees["listed_in"].dropna()).split(", "))
categories.value_counts().head()



## 12. Afficher les directeurs qui ont produit le plus de films/séries 
##     disponibles sur Netflix.


donnees["director"].head(10)
categories=pd.Series(", ".join(donnees["director"].dropna()).split(", "))
categories.value_counts().head(10)


## 13. Voir si Jan Suter travaille souvent avec les mêmes acteurs


director = donnees.loc[donnees['director'].notna()]
print(director)
donnee_jan_suter =director[director['director'].str.contains('Jan Suter')]
print(donnee_jan_suter)
cast = pd.Series(", ".join(donnee_jan_suter['cast']).split(','))
print(cast.value_counts().head(5))


## 14. Représenter les dix pays qui ont produit le plus de contenus 
##     disponibles sur Netflix, avec le nombre de contenus par pays


import seaborn as sns

pays = df['country'].value_counts().head(10)
print(pays)
defpays = df.loc[df['country'].isin(pays.index)]
print(defpays)
sns.countplot(y= 'country', data = defpays)
#plt.xticks(rotation=90)

## 15. Tracer un graphe à barres du nombre de films/séries par classement 
##     de contenu (rating)

sns.countplot(y= 'rating',data=df,palette = 'dark')

plt.figure(figsize=(7,7))
sns.set(style="darkgrid")
sns.countplot(x='rating', data=netflix)

plt.title("Nombre de films/series par classment de contenu")
plt.xlabel("Notation")
plt.ylabel("Nombre de films et Series")
plt.xticks(rotation=90)
plt.show()

## 16. Afficher l’évolution du nombre de films/séries disponibles sur 
##     Netflix au cours du temps

df2 = df

df2["date_added"] = pd.to_datetime(df2["date_added"]) 

df2["year_added"] = pd.to_datetime(df2["date_added"]).dt.year 

data_date_movie = df2.groupby(["year_added", "type"]).size().reset_index(name='Count')

print(data_date_movie)



## 17. Afficher la distribution de la durée des films disponibles
##     sur Netflix

movie = donnees[(donnees["type"]=="Movie")]
duree = pd.Series(movie['duration']).str.replace("min", "").astype("int").sort_values(ascending=False)
sns.distplot(duree)



## 18. Tracer un graphique représentant le nombre de séries par
##     modalité de nombre de saisons

donnees_series = donnees.loc[donnees.type == 'TV Show']
plt.figure(figsize=[15,6])
sns.countplot(x ='duration', data = data_series)
plt.title("Nombre de Séries & de Saisons")
plt.ylabel("Nombre de Series")
plt.xlabel("Nombre de Saisons")
plt.show()








