#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
sys.path.insert(0, '../common')
import numpy as np
from graphs import *



#   TODAS LAS TABLAS DE DATOS ESTAN EN FORMATO   CUTOFF - 512x1 - 1x512 - 1x1

def blockSizeComparison():
     
#PRIMERO GRAFICO time vs cutoff PARA DISTINTOS TAMAÑOS DE BLOQUES (SOLUCION ANALITICA)
    	cutoffs , best ,mid, worst = [],[],[],[]
       	with open("data/analitic.txt") as f:
	  for line in f.readlines():
             c, b, m, w  = line.strip().split("\t")
             cutoffs.append(int(c))
             best.append(float(b))
	     mid.append(float(m))
	     worst.append(float(w))		
        params = {
            'xlabel': u"Cutoff",
            'ylabel': u"Tiempo de ejecución [s]",
            'xdata': cutoffs,
            'ydata': [best,mid,worst],
            'label': [u'Bloques 512x1',u'Bloques 1x512',u'Bloques 1x1'],
            'filename': 'timeComparison-Analitic.png' ,
        }
        comparativeScatter(**params)
	
#MISMO GRAFICO GRAFICO time vs cutoff PARA DISTINTOS TAMAÑOS DE BLOQUES (SOLUCION TABLA POT.)
    	cutoffs , best ,mid, worst = [],[],[],[]
       	with open("data/potential.txt") as f:
	  for line in f.readlines():
             c, b, m, w  = line.strip().split("\t")
             cutoffs.append(int(c))
             best.append(float(b))
	     mid.append(float(m))
	     worst.append(float(w))		
        params = {
            'xlabel': u"Cutoff",
            'ylabel': u"Tiempo de ejecución [s]",
            'xdata': cutoffs,
            'ydata': [best,mid,worst],
            'label': [u'Bloques 512x1',u'Bloques 1x512',u'Bloques 1x1'],
            'filename': 'timeComparison-Potential.png' ,
        }
        comparativeScatter(**params)
	
	
#MISMO GRAFICO GRAFICO time vs cutoff PARA DISTINTOS TAMAÑOS DE BLOQUES (SOLUCION TABLA DERIV.)
    	cutoffs , best ,mid, worst = [],[],[],[]
       	with open("data/derivative.txt") as f:
	  for line in f.readlines():
             c, b, m, w  = line.strip().split("\t")
             cutoffs.append(int(c))
             best.append(float(b))
	     mid.append(float(m))
	     worst.append(float(w))		
        params = {
            'xlabel': u"Cutoff",
            'ylabel': u"Tiempo de ejecución [s]",
            'xdata': cutoffs,
            'ydata': [best,mid,worst],
            'label': [u'Bloques 512x1',u'Bloques 1x512',u'Bloques 1x1'],
            'filename': 'timeComparison-Derivative.png' ,
        }
        comparativeScatter(**params)
	

	

blockSizeComparison()
