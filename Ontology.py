#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 14:29:08 2021

@author: Amine Laghaout
"""

from types import SimpleNamespace

class Ontology:
    
    def __init__(self, **kwargs):
        
        # Set the kwargs as attributes.
        [self.__setattr__(k, v) for k, v in kwargs.items()]
        
        # Define the base ontic states (i.e., the attributes that are assumed 
        # to be real).
        self.ontic = self.define_ontic()
        
        # Determine the derived states (i.e., the transformed or measured 
        # attributes that follow from the base ontic states).
        self.derived = self.compute_derived()
        
        # Determine the hulls that result from the derived states.
        self.hulls = self.compute_hulls()

    def define_ontic(self):
        """
        Define the base ontic states.

        Returns
        -------
        ontic : np.array 
            Array of dimension `N·K` where `N` is the number of attributes and 
            `K` the number of such combinations.
        """    
        
        ontic = None
        
        return ontic
 
    def compute_derived(self):
        """
        Define the logical operations that (potentially) reduced space the 
        "real of possibilities". These operations, which typically correspond 
        to measurements, produce a set of derived states.

        Returns
        -------
        derived : np.array
            Array of dimension `N'·K'` where `N'` is the number of derived 
            attributes (typically one derived attribute per context) and `K'` 
            is the number of combinations of such attributes.
        """        
        derived = None
        
        return derived
        
    def compute_hulls(self):
        """
        Determine the real and unreal hulls.

        Returns
        -------
        hulls : SimpleNamespace
            Real and unreal hulls together with their support vectors.
        """
        
        real = SimpleNamespace(**dict(support=self.derived, hull=None))
        unreal = SimpleNamespace(**dict(support=None, hull=None))
        hulls = SimpleNamespace(**dict(real=real, unreal=unreal))
        
        return hulls
        
    def distance(self, mu, hull='real'):
        """
        Compute the distance of various points form the hulls.

        Parameters
        ----------
        mu : np.array
            Measurement vector.
        hull : bool, optional
            Distance from the hull ``hull``

        Returns
        -------
        D : float
            Distance from the hull. This is positive if outside the hull and
            negative if inside it.
        """
        
        assert hull in self.hulls.__dict__.keys()
        
        if hull == 'real':        
            distance = self.hulls.real.hull.find_simplex(mu)
        elif hull == 'unreal':
            distance = self.hulls.unreal.hull.find_simplex(mu)
        
        return distance
