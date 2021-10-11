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
- Double check the optimizations.
"""

import numpy as np
import PeresMermin as pm

# Side of the Peres-Mermin square. 
# WARNING: Values above 4 will take an inordinate amount of time.
side = 3  # <-- EDIT. Choose either 2, 3, or 4.
ontology = pm.PeresMermin(side)

# Selection of possible measurement vectors ``mu`` with an optional 
# ``delta_mu`` error vector. Choose one vector and pass it to 
# ``ontology.violation()`` below.
mu = dict(
    # Real vector for the Peres-Mermin square.
    R=dict(mu=np.ones(2*side, dtype=np.int)),
    # Unreal vector for the Peres-Mermin square.
    U=dict(mu=np.concatenate((np.ones(2*side-1), -np.ones(1)))),
    # Empirical vector for the 3D Peres-Mermin square.
    IBM=dict(
        mu=np.array([0.939, 0.887, 0.833, 0.907, 0.917, -0.504]),
        delta_mu=np.array([3.79, 5.09, 6.12, 4.64, 4.41, 9.55])*1e-3))

# %% Save into variables.

violation = ontology.violation(**mu['IBM'])  # <-- EDIT
ontic = ontology.ontic
real_support = ontology.hulls.real.support
unreal_support = ontology.hulls.unreal.support

