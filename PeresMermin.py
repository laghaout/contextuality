#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 14:29:08 2021

@author: Amine Laghaout
"""
    
import numpy as np
import pandas as pd

import Ontology as ont

class PeresMermin(ont.Ontology):

    def __init__(self, side=3, **kwargs):
        
        super().__init__(side=side, **kwargs)
    
    def define_ontic(self):
        
        ontic = np.array([self.bin2square(k, self.side) 
                          for k in range(2**self.side**2)]).T
               
        ontic = pd.DataFrame(
            ontic, 
            index=np.array([[f'a{r}{c}' for c in range(1, self.side+1)] 
                            for r in range(1, self.side+1)]).flatten(),
            columns=[f'p{k}' for k in range(1, ontic.shape[1]+1)])
        
        return ontic

    @staticmethod
    def bin2square(k, side):
        """
        Generate a array of binary characters that corresponds to the binary 
        encoding of integer ``k``.

        Parameters
        ----------
        k : TYPE
            DESCRIPTION.
        side : TYPE
            DESCRIPTION.

        Returns
        -------
        square : TYPE
            DESCRIPTION.

        """
        
        k = bin(k)[2:]  # Convert ``k`` to its binary representation string.
        k = '0'*(side**2 - len(k)) + k  # Pad with '0's.
        square = np.array([(-1)**int(j) for j in k])
        
        return square
    
    def compute_derived(self):
        
        # Reshape the squares into the N·K matrix.
        derived = self.ontic.values.T.reshape(
            self.ontic.shape[1], self.side, self.side)
        
        # Compute the row and column products.
        rows = derived.prod(axis=1)
        cols = derived.prod(axis=2)
        
        # Concatenate the row and column products.
        derived = np.hstack((rows, cols)).T
        
        # Drop duplicate derived vectors.
        derived = np.unique(derived, axis=1)
        
        derived = pd.DataFrame(
            derived, 
            index=[f'r{k}' for k in range(1, self.side+1)] + \
                [f'c{k}' for k in range(1, self.side+1)],
            columns=[f'p{j}' for j in range(1, derived.shape[1]+1)])
            
        return derived

    def compute_hulls(self):

        hulls = super().compute_hulls()   
        
        hulls.unreal.support = self.compute_complement(hulls.real.support)
        
        return hulls

    @staticmethod
    def compute_complement(df):

        dim = df.shape[0]   

        df = (df+1)/2
        v = np.array([2**k for k in range(dim)], dtype=np.int32)  # TODO replace 6
        v = v.reshape((v.shape[0], 1))
        df = v*df
        df = df.sum()
        df = set(np.int32(df.values))
        whole_space = set(np.arange(2**dim, dtype=np.int32))
        complement = whole_space - df
        
        return complement

        
        