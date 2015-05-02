#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
sys.path.insert(0, '../common')
import numpy as np
from graphs import *


def timeVsCut():
    	cutoffs , timesd ,timesp, timesa = [],[],[],[]
       	with open("results/4000it-200p.txt") as f:
	  for line in f.readlines():
             c, p , d , a  = line.strip().split("\t")
             cutoffs.append(int(c))
             timesp.append(float(p))
	     timesd.append(float(d))
	     timesa.append(float(a))		
        params = {
            'xlabel': "Cutoff",
            'ylabel': "Tiempo(seg)",
            'xdata': cutoffs,
            'ydata': [timesp,timesa,timesd],
            'label': ['Tabla pot','Tabla deriv','Analitic'],
            'filename': 'timeComparison.png' ,
        }
        comparativeScatter(**params)

timeVsCut()
