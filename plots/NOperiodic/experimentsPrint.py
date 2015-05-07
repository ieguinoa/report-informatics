#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
sys.path.insert(0, '../common')
import numpy as np
from graphs import *



def comparacionTiempos1Niteraciones():
  
#**** PRIMERA COMPARACION PARA periodico
 
  gpu1_periodic=522.000
  gpuPot1_periodic=837.903
  gpuDer1_periodic=1000.000
  
  gpuN_periodic=522.000
  gpuPotN_periodic=837.903
  gpuDerN_periodic=1000.000
 

  

  labels = [u"1 iteración", u"N iteraciones"]
  comparison = {
      u"GPU Base": [gpu1_periodic, gpuN_periodic ],
      u"GPU Tabla Potenciales": [gpuPot1_periodic, gpuPotN_periodic ],
      u'GPU Tabla Derivadas': [gpuDer1_periodic,gpuDerN_periodic ],
  }

  params = {
      'values': comparison,
      'ticks': labels,
      'filename': u'comparacion-periodico.png',
      'ylabel': u'Tiempo promedio por iteración [ms]',
      'loc': 'left'
  }

  multiComparativeBarChart(**params)
  

#AHORA HACER UNA COMPARACION PARA CONDICIONES NO PERIODICAS
   
 
  gpu1_NOper=704.000
  gpuPot1_NOper=1019.784
  gpuDer1_NOper=1000.000

  gpuN_NOper=704.000
  gpuPotN_NOper=1019.784
  gpuDerN_NOper=1000.000

  

  labels = [u"1 iteración", u"N iteraciones"]
  comparison = {
      u"GPU Analítico": [gpu1_NOper, gpuN_NOper ],
      u"GPU Tabla Potenciales": [gpuPot1_NOper, gpuPotN_NOper ],
      u'GPU Tabla Derivadas': [gpuDer1_NOper,gpuDer1_NOper ],
  }

  params = {
      'values': comparison,
      'ticks': labels,
      'filename': u'comparacion-NOperiodico.png',
      'ylabel': u'Tiempo promedio por iteración [ms]',
      'loc': 'left'
  }

  multiComparativeBarChart(**params)
  
  
  
  
  
  
  
def comparacionTiemposFinalNOperiodic():
  
#**** PRIMERA COMPARACION PARA 1 ITERACION
  gpu_NOper=704.000
  gpuPot_NOper=1019.784
  gpuDer_NOper=1000.000

  
  gpu_periodic=522.000
  gpuPot_periodic=837.903
  gpuDer_periodic=1000.000

  

  labels = [u"Periódica", u"NO periódica"]
  comparison = {
      u"GPU Analítico": [gpu_NOper, gpu_periodic ],
      u"GPU Tabla Potenciales": [gpuPot_NOper, gpuPot_periodic ],
      u'GPU Tabla Derivadas': [gpuDer_NOper,gpuDer_periodic ],
  }

  params = {
      'values': comparison,
      'ticks': labels,
      'filename': u'comparacion-1iter.png',
      'ylabel': u'Tiempo de ejecución [ms]',
      'loc': 'left'
  }

  multiComparativeBarChart(**params)
  

#AHORA HACER UNA COMPARACION PARA N ITERACIONES
  
  gpu_NOper=704.000
  gpuPot_NOper=1019.784
  gpuDer_NOper=1000.000

  
  gpu_periodic=522.000
  gpuPot_periodic=837.903
  gpuDer_periodic=1000.000

  

  labels = [u"Periódica", u"NO periódica"]
  comparison = {
      u"GPU Analítico": [gpu_NOper, gpu_periodic ],
      u"GPU Tabla Potenciales": [gpuPot_NOper, gpuPot_periodic ],
      u'GPU Tabla Derivadas': [gpuDer_NOper,gpuDer_periodic ],
  }

  params = {
      'values': comparison,
      'ticks': labels,
      'filename': u'comparacion-Niter.png',
      'ylabel': u'Tiempo de ejecución [ms]',
      'loc': 'left'
  }

  multiComparativeBarChart(**params)
  




comparacionTiempos1Niteraciones()
