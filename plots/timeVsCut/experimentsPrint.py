#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
sys.path.insert(0, '../common')
import numpy as np
from graphs import *



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




def timeVsCut():
    	cutoffs , timesd ,timesp, timesa = [],[],[],[]
    #for case in ["hemo","fullereno", "caroteno"]:
    	with open("results/4000it-200p.txt") as f:
	  for line in f.readlines():
             c, p , d , a  = line.strip().split("\t")
             cutoffs.append(int(c))
             timesp.append(float(p))
	     timesd.append(float(d))
	     timesa.append(float(a))		
            #for line in f.readlines():
             #   threadc, timestr = line.split("\t")
              #  vals.append((int(threadc), time2secs(timestr)))
	#vals = sorted(vals)
        #threads, vals = zip(*vals)

        params = {
            'xlabel': "Cutoff",
            'ylabel': "Tiempo(seg)",
            'xdata': cutoffs,
            'ydata': [timesp,timesa,timesd],
            'label': ['Tabla pot','Tabla deriv','Analitic'],
            'filename': 'escalabilidad-xeon-phi-.png' ,
        }
        comparativeScatter(**params)

timeVsCut()
