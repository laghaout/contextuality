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
        
        # Define the base ontic states.
        self.ontic = self()
        
        # Define the logic, i.e., the derived measurements.
        self.derived = self.logic()
        
        # Determine the hulls.
        (self.real, self.unreal) = self.hulls()
       
    def logic(self):
        """
        Determine the logical operations and the reduced space.

        Returns
        -------
        None.
        """    
        
        return None
        
    def hulls(self):
        """
        Determine the real and unreal hulls.

        Returns
        -------
        None.
        """
        
        real = SimpleNamespace(**dict(support=None, hull=None))
        unreal = SimpleNamespace(**dict(support=None, hull=None))
        
        return (real, unreal)
        
    def distance(self, mu, hull=True):
        """
        Compute the distance of various points form the hulls.

        Parameters
        ----------
        mu : np.array
            Measurement vector.
        hull : bool, optional
            Distance from the real (unreal) hull if True (False). The default 
            is True.

        Returns
        -------
        D : float
            Distance from the hull.

        """
        
        return None
