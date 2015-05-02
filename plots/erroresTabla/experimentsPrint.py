#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
sys.path.insert(0, '../common')
import numpy as np
from graphs import *


## GRAFICO NUMERO DE ELEMENTOS DE LA TABLA vs ERROR ABSOLUTO EN LA FUERZA, PARA TABLA DE POTENCIALES Y 
def errorNumeroDeElementos():
    	elementos , errTablaPot , errTablaDer = [],[],[]
    #for case in ["hemo","fullereno", "caroteno"]:
    	with open("numeroElementos/errorAbsoluto.txt") as f:
	  for line in f.readlines():
             e,p,d  = line.strip().split("\t")
             elementos.append(int(e))
             errTablaPot.append(float(p))
	     errTablaDer.append(float(d))
        params = {
            'xlabel': u"Número de elementos de la tabla",
            'ylabel': u"Error absoluto",
            'xdata': elementos,
            'ydata': [errTablaPot,errTablaDer],
            'label': [u'Tabla Potenciales',u'Tabla Derivadas'],
            'filename': u'errorAbsolutoElemTabla.png' ,
 	    'ymax' : 10000,
        }
        comparativeScatter(**params)





def escalabilidad_final():
    cutoffs , times = [],[]
    with open("results/tablaPot-4000it-200p.txt") as f:
           for line in f.readlines():
             t, m = line.strip().split("\t")
             cutoffs.append(int(t))
             times.append(float(m))

    params = {
                'xlabel': u"Cutoff",
                'ylabel': u"Tiempo de ejecución (seg.)",
		'xdata': cutoffs,
	        'ydata': times,
		'label': ['Experimental'],
		'filename': u'scalability-matrix-sums.png',
       		#'ylim': (3.2,3.6),
    }
    comparativeScatter(**params)







#########################################
###  LISTA DE PLOTS QUE QUIERO GENERAR
########################################
errorNumeroDeElementos()
