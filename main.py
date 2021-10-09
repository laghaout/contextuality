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

mu = dict(
    R=dict(mu=np.array([1, 1, 1, 1, 1, 1])),
    Q=dict(mu=np.array([1, 1, 1, 1, 1, -1])),
    IBM=dict(
        mu=np.array([0.939, 0.887, 0.833, 0.907, 0.917, -0.504]),
        delta_mu=np.array([3.79, 5.09, 6.12, 4.64, 4.41, 9.55])*1e-3))

# %% Save into variables

ontic = ontology.ontic
real_support = ontology.hulls.real.support
unreal_support = ontology.hulls.unreal.support
violation = ontology.violation(**mu['Q'])

print("Distance from the real hull:", violation.D)
