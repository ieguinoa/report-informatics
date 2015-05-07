#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
sys.path.insert(0, '../common')
import numpy as np
from graphs import *





def comparacionTiemposFinal():

#COMPARACION DATOS CON PERIODICIDAD Y MAXIMO CUTOFF
  #cpu_200=10.0
  gpu_200=2.000
  gpuPot_200=1.7884
  gpuDer_200=1.6500

  #cpu_8k=57.344
  gpu_8k=10.876853
  gpuPot_8k=9.604011
  gpuDer_8k=9.099904

  cpu_20k=57.344
  gpu_20k=20.876853
  gpuPot_20k=18.604011
  gpuDer_20k=16.099904

  labels = [u"200 átomos", u"8000 átomos", u"20000 átomos"]
  comparison = {
      #u"CPU": [cpu_200, cpu_8k, cpu_20k ],
      u"GPU Base": [gpu_200, gpu_8k, gpu_20k ],
      u"GPU Tabla Potenciales": [gpuPot_200, gpuPot_8k, gpuPot_20k ],
      u'GPU Tabla Derivadas': [gpuDer_200,gpuDer_8k, gpuDer_20k ],
  }

  params = {
      'values': comparison,
      'ticks': labels,
      'filename': u'comparacion-tiempos-sistemas.png',
      'ylabel': u'Tiempo de ejecución [s]',
      'loc': 'left'
  }

  multiComparativeBarChart(**params)


#COMPARACION DATOS CON PERIODICIDAD Y MAXIMO CUTOFF
  cpu_200=10.0
  gpu_200=2.000
  gpuPot_200=1.7884
  gpuDer_200=1.6500

  cpu_8k=57.344
  gpu_8k=10.876853
  gpuPot_8k=9.604011
  gpuDer_8k=9.099904

  cpu_20k=127.344
  gpu_20k=20.876853
  gpuPot_20k=18.604011
  gpuDer_20k=16.099904

  labels = [u"200 átomos", u"8000 átomos", u"20000 átomos"]
  comparison = {
      u"CPU": [cpu_200, cpu_8k, cpu_20k ],
      u"GPU Base": [gpu_200, gpu_8k, gpu_20k ],
      u"GPU Tabla Potenciales": [gpuPot_200, gpuPot_8k, gpuPot_20k ],
      u'GPU Tabla Derivadas': [gpuDer_200,gpuDer_8k, gpuDer_20k ],
  }

  params = {
      'values': comparison,
      'ticks': labels,
      'filename': u'comparacion-tiempos-TODOScpu.png',
      'ylabel': u'Tiempo de ejecución [s]',
      'loc': 'left'
  }

  multiComparativeBarChart(**params)



# *********CPU vs IMPLEMENTACION BASE GPU****  COMPARACION DATOS CON PERIODICIDAD Y MAXIMO CUTOFF
  cpu_200=10.0
  gpu_200=2.000
  #gpuPot_200=1.9084
  #gpuDer_200=1.8500

  cpu_8k=57.344
  gpu_8k=10.876853
  #gpuPot_8k=10.604011
  #gpuDer_8k=10.099904

  #cpu_20k=57.344
  #gpu_20k=10.876853
  #gpuPot_20k=10.604011
  #gpuDer_20k=10.099904

  labels = [u"200 átomos", u"8000 átomos"]
  comparison = {
      u"CPU": [cpu_200, cpu_8k],
      u"GPU Base": [gpu_200, gpu_8k],
      #u"GPU Tabla Potenciales": [gpuPot_200, gpuPot_8k, gpuPot_20k ],
      #u'GPU Tabla Derivadas': [gpuDer_200,gpuDer_8k, gpuDer_20k ],
  }

  params = {
      'values': comparison,
      'ticks': labels,
      'filename': u'comparacion-tiempos-CPU.png',
      'ylabel': u'Tiempo de ejecución [s]',
      'loc': 'left'
  }

  multiComparativeBarChart(**params)







comparacionTiemposFinal()
