#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys
sys.path.insert(0, '../common')
import numpy as np
from graphs import *


def comparacionTiemposFinal():
#xc iteration best params
  cpu_200=781.765
  gpu_200=704.000
  gpuPot_200=1019.784
  gpuDer_200=1000.000

  cpu_8k=757.344
  gpu_8k=522.000
  gpuPot_8k=837.903
  gpuDer_8k=1000.000

  cpu_20k=2500.2070
  gpu_20k=1512.538
  gpuPot_20k=2912.617
  gpuDer_20k=1000.000

  labels = [u"200 átomos", u"8000 átomos", u"20000 átomos"]
  comparison = {
      u"CPU": [cpu_200, cpu_8k, cpu_20k ],
      u"GPU Analítico": [gpu_200, gpu_8k, gpu_20k ],
      u"GPU Tabla Potenciales": [gpuPot_200, gpuPot_8k, gpuPot_20k ],
      u'GPU Tabla Derivadas': [gpuDer_200,gpuDer_8k, gpuDer_20k ],
  }

  params = {
      'values': comparison,
      'ticks': labels,
      'filename': u'comparacion-tiempos-sistemas.png',
      'ylabel': u'Tiempo de ejecución [ms]',
      'loc': 'left'
  }

  multiComparativeBarChart(**params)



comparacionTiemposFinal()
