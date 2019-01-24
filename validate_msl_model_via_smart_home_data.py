# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 13:30:07 2019
Ziel dieses Skriptes ist zunächst die Einteilung der Daten in Train/Test/Validate (70/20/10).
Danach werden die Modell an Hand der Trainigs Daten angelenrt. Anhand der Testdaten w
@author: Ewen Witte
"""

import numpy as np
import pandas as pd

smarthome_data = pd.read_csv('smarthome_dataset.csv')