# Import external packages

from multiprocessing.connection import wait
import pandas as pd
from datetime import datetime
import numpy as np
import re
from sys import platform

# Classes 

class Subject():
    def __init__(self, file_name):

        ### Aufgabe 1: Interpolation ###

        __f = open(file_name) #Kommando open öffnet Datei "file_name"
        self.subject_data = pd.read_csv(__f) #Daten der Datei werden ausgelesen
        self.subject_data = self.subject_data.interpolate(method='quadratic', axis=0) 
        #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html
        #Daten werden interpoliert und mit "quadratic" werden Datenpunkte erstellt um die Lücken in __f auszugleichen
                # VORSICHT BEI WINDOWS MUSS DIE 1 in Eckigen Klammern weg
        if platform == "darwin":
            print("Mac")
                # Windows...<
            __splited_id = re.findall(r'\d+',file_name)[1]
        else:
    # Windows...<
            __splited_id = re.findall(r'\d+',file_name)     
        self.subject_id = ''.join(__splited_id)
        self.names = self.subject_data.columns.values.tolist()
        self.time = self.subject_data["Time (s)"]        
        self.spO2 = self.subject_data["SpO2 (%)"]
        self.temp = self.subject_data["Temp (C)"]
        self.blood_flow = self.subject_data["Blood Flow (ml/s)"]
        print('Subject ' + self.subject_id + ' initialized')


        

### Aufgabe 2: Datenverarbeitung ###

#https://www.geeksforgeeks.org/how-to-calculate-moving-average-in-a-pandas-dataframe/

def calculate_CMA(df,n):
    return df.expanding(n).mean()
    pass
    

def calculate_SMA(df,n):
    return df.rolling(n).mean()
    pass

#Aufgabe 4.1
#Bei Signalen mit Rauschen und Ausreißern gut, da Kurve gelättet wird. Bei Echtzeit Signalen ungeeignet.
#Aufgabe 4.2
#Je höher man das n wählt, desto stärker werden die Extrema/Ausreißer geglättet
