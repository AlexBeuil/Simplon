#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 12:13:34 2020

@author: lucas
"""


import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
engine = create_engine('mysql+pymysql://lucas:Claus5991.@localhost:3306/assur_auto')

nom = ''
prenom = ''
ville = ''
adresse = ''
code_postal =''
id_client = pd.read_sql_query("SELECT max(CL_ID) FROM CLIENTS;", engine)+1
id_client = id_client.iloc[0,0]
id_contrat = pd.read_sql_query("SELECT max(CO_ID) FROM CONTRATS;", engine)+1
id_contrat = id_contrat.iloc[0,0]
id_client_fk = id_client
tel = ''
date = datetime.today().strftime('%Y-%m-%d')
categorie = ''
bonus_malus = ''
vu = '1'
vt = '1'
id_ag = '1'


print(date)

while len(nom) == 0 or len(prenom) == 0 or len(ville) == 0 or len(adresse) == 0 or len(code_postal) == 0 or len(tel) == 0:
    
    if len(nom) == 0:
        nom = input('veuillez entrer un nom :').upper()
    
    elif len(prenom) == 0:
        prenom = input('veuillez entrer un prenom :')
        
    elif len(adresse) == 0: 
        adresse = input("veuillez entrer l'adresse :")
        
    elif len(code_postal) == 0:
        code_postal = input('veuillez entrer le code postal :')
        if code_postal.isdigit() :
           code_postal = code_postal
        else:
            print('veuillez ne rentrer que des nombres')
            code_postal = ''
        
    elif len(ville) == 0:
        ville = input('veuillez entrer la ville du client :')

              
    elif len(tel) == 0 or len(tel) > 15:
        tel = input('veuillez entrer un numéro de tel :')
        


engine.execute('INSERT INTO CLIENTS (CL_ID, CL_NOM, CL_PRENOM, CL_ADRESSE, CL_CP, CL_VILLE, CL_TEL) VALUES (%s, "%s", "%s","%s", %s,"%s","%s");' %(id_client, nom, prenom, adresse, code_postal, ville, tel))

print('Enregistrement effectué')




while len(categorie) == 0 or len(bonus_malus) == 0:
    
    if len(categorie) == 0:
        categorie = input('veuillez entrer le type de contrat:')
    
    elif len(bonus_malus) == 0:
        bonus_malus = input('veuillez entrer le taux de bonus ou de malus:')
        
        
        

engine.execute('INSERT INTO CONTRATS (CO_ID, CO_DATE, CO_CATEGORIE, CO_BONUS_MALUS, CO_CLIENT_FK, CO_VU_FK, CO_VT_FK, CO_AG_FK) VALUES (%s, "%s", "%s","%s", "%s","%s","%s", "%s");' %(id_contrat, date, categorie, bonus_malus, id_client_fk, vu, vt, id_ag))

print('enregistrement effectué')







