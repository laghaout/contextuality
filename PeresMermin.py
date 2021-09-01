#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 14:29:08 2021

@author: Amine Laghaout
"""
    
import numpy as np
import pandas as pd

from types import SimpleNamespace

import Ontology as ont

class PeresMermin(ont.Ontology):

    def __init__(self, side=3, **kwargs):
        
        super().__init__(side=side, **kwargs)
    
    def __call__(self):
        
        side = self.side
        
        return np.array([self.bin2square(k, side) for k in range(2**side**2)])

    @staticmethod
    def bin2square(k, side):
        
        k = bin(k)[2:]
        k = '0'*(side**2 - len(k)) + k
        square = np.array([(-1)**int(j) for j in k]).reshape(side, side)
        
        return square
    
    def logic(self):
        
        rows = self.ontic.prod(axis=1)
        cols = self.ontic.prod(axis=2)
        derived = pd.DataFrame(
            np.hstack((rows, cols)), 
            columns=[f'r{k}' for k in range(1, self.side)] + \
                [f'c{k}' for k in range(1, self.side)])
        
        return derived

    def hulls(self):

        real = SimpleNamespace(**dict(
            support=self.derived.drop_duplicates(inplace=False), 
            hull=None))
        unreal = SimpleNamespace(**dict(
            support=None, 
            hull=None))
        
        return real, unreal
