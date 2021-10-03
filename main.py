#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 14:42:42 2021

@author: Amine Laghaout

This is a follow-up on the following pre-print: 

A. Dikme, N. Reichel, A. Laghaout, G. Björk, 
Measuring the Mermin-Peres magic square using an online quantum computer
arXiv:2009.10751 (2020)
"""

import PeresMermin as pm

ontology = pm.PeresMermin()
ontic = ontology.ontic
real_support = ontology.hulls.real.support
unreal_support = ontology.hulls.unreal.support

# %%
