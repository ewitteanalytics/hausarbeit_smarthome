# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 13:25:30 2019
Script zu nachverarbeitung der Smarthome Daten. Ziel ist die Erstellung einer Mapping Tabelle
@author: Ewen Witte
"""


import numpy as np
import pandas as pd

##einlesen der csv Daten
raw_data = pd.read_csv('raw_data+timestamp.csv')
meta_data = pd.read_csv('meta_data+timestamp.csv')

##Erstellung Ausgabe CSV
csv_ausgabe = 'meta_data_id,raw_data_id\n'

lowerbound = 0
for meta_row in range(114):
    ##Bearbeitung des Letzten Datensatz
    if meta_row == 113:
        for raw_row in range(lowerbound, 7918):
            if meta_data['timestamp'][meta_row] >= raw_data['timestamp'][raw_row]:
                csv_ausgabe += str(meta_data['meta_data_id'][meta_row])+','+str(raw_data['raw_data_id'][raw_row])+'\n'
        break
    ##Verabeitung aller Datenseätze; Daten werden zwischen den Events zugeordnet (Event1 = Alle Daten die nach Event1 entstanden sind und For Event2 Passiert sind)
    for raw_row in range(lowerbound, 7918):
        if meta_data['timestamp'][meta_row+1] <= raw_data['timestamp'][raw_row]:
            lowerbound = raw_row
            break
        if meta_data['timestamp'][meta_row] <= raw_data['timestamp'][raw_row]:
            csv_ausgabe += str(meta_data['meta_data_id'][meta_row])+','+str(raw_data['raw_data_id'][raw_row])+'\n'
##Rauschreiben der mapping Tabelle
with open('raw_mapping.csv','w') as mapping:
    mapping.write(csv_ausgabe)