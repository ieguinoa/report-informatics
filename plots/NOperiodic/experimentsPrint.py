#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
sys.path.insert(0, '../common')
import numpy as np
from graphs import *


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
  




comparacionTiemposFinalNOperiodic()
