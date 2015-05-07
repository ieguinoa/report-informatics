#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
sys.path.insert(0, '../common')
import numpy as np
from graphs import *


## GRAFICO NUMERO DE ELEMENTOS DE LA TABLA vs ERROR ABSOLUTO EN LA FUERZA
def errorNumeroDeElementos():
    	elementos , errTablaPot , errTablaDer = [],[],[]
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



# GRAFICO EL ERROR ABSOLUTO EN FUNCION DEL LIMITE SUPERIOR DE LA TABLA
def errorLimiteSuperior():
    	elementos , errTablaPot , errTablaDer = [],[],[]
    	with open("errorLimiteTabla/200particulas-limites.txt") as f:
	  for line in f.readlines():
             e,d,p  = line.strip().split("\t")
             elementos.append(int(e))
             errTablaPot.append(float(p))
	     errTablaDer.append(float(d))
        params = {
            'xlabel': r"Limite superior de la tabla [$\AA$]",
            'ylabel': u"Error absoluto",
            'xdata': elementos,
            'ydata': [errTablaPot,errTablaDer],
            'label': [u'Tabla Potenciales',u'Tabla Derivadas'],
            'filename': u'errorAbsolutoLimite200.png' ,
            'notation': 'sci'
        }
        comparativeScatter(**params)


	elementos , errTablaPot , errTablaDer = [],[],[]
    	with open("errorLimiteTabla/8kpart-limites.txt") as f:
	  for line in f.readlines():
             e,d,p  = line.strip().split("\t")
             elementos.append(int(e))
             errTablaPot.append(float(p))
	     errTablaDer.append(float(d))
        params = {
            'xlabel': r'Limite superior de la tabla [$\AA$]',
            'ylabel': u"Error absoluto",
            'xdata': elementos,
            'ydata': [errTablaPot,errTablaDer],
            'label': [u'Tabla Potenciales',u'Tabla Derivadas'],
            'filename': u'errorAbsolutoLimite8k.png' ,
	    'ymax' : 0.0001,
	    #'ymax' : 2, 
	    'xmin' : 15,
	    'notation': 'sci', 
        }
        comparativeScatter(**params)









#########################################
###  LISTA DE PLOTS QUE QUIERO GENERAR
########################################
errorNumeroDeElementos()
errorLimiteSuperior()
