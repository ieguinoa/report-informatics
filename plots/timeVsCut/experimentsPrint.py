#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
sys.path.insert(0, '../common')
import numpy as np
from graphs import *


def timeVsCut():

	#PRIMERO GRAFICO time vs cutoff PARA SIMULACION EN COND. DE PERIODICIDAD
    	cutoffs , timesd ,timesp, timesa = [],[],[],[]
       	with open("results/4000it-200p-periodic.txt") as f:
	  for line in f.readlines():
             c, p, d, a  = line.strip().split("\t")
             cutoffs.append(int(c))
             timesp.append(float(p))
	     timesd.append(float(d))
	     timesa.append(float(a))		
        params = {
            'xlabel': u"Cutoff",
            'ylabel': u"Tiempo(seg)",
            'xdata': cutoffs,
            'ydata': [timesp,timesa,timesd],
            'label': [u'Tabla potenciales',u'Analítico',u'Tabla derivadas'],
            'filename': 'timeComparison-periodic.png' ,
        }
        comparativeScatter(**params)
	
	cutoffs , timesd ,timesp, timesa = [],[],[],[]
	#MISMO GRAFICO PERO PARA NO PERIODIC	
	with open("results/4000it-200p-NOperiodic.txt") as f:
	  for line in f.readlines():
             c,d, p  , a  = line.strip().split("\t")
             cutoffs.append(int(c))
             timesp.append(float(p))
	     timesd.append(float(d))
	     timesa.append(float(a))		
        params = {
            'xlabel': "Cutoff",
            'ylabel': "Tiempo(seg)",
            'xdata': cutoffs,
            'ydata': [timesp,timesa,timesd],
            'label': [u'Tabla potenciales',u'Analítico',u'Tabla derivadas'],
            'filename': 'timeComparison-NOperiodic.png' ,
        }
        comparativeScatter(**params)



timeVsCut()
