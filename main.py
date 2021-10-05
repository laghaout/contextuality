#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 14:42:42 2021

@author: Amine Laghaout

This is a follow-up on the following pre-print: 

A. Dikme, N. Reichel, A. Laghaout, G. Björk, 
Measuring the Mermin-Peres magic square using an online quantum computer
arXiv:2009.10751 (2020)

TODO
- Add optional plotting in 2D and 3D.
- Include the Pauli operators somewhere.
"""

import numpy as np
import PeresMermin as pm

ontology = pm.PeresMermin()
ontic = ontology.ontic
real_support = ontology.hulls.real.support
unreal_support = ontology.hulls.unreal.support

mu = dict(
    R=np.array([1, 1, 1, 1, 1, .8]),
    Q=np.array([1, 1, 1, 1, 1, -1]),
    IBM=np.array([0.939, 0.887, 0.833, 0.907, 0.917, -0.504]))
print(ontology.distance(mu['R']))
