#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 14:29:08 2021

@author: Amine Laghaout
"""

import numpy as np
from scipy.optimize import minimize
from types import SimpleNamespace

class Ontology:
    
    def __init__(self, **kwargs):
        
        # Set the kwargs as attributes.
        [self.__setattr__(k, v) for k, v in kwargs.items()]
        
        # Define the base ontic states (i.e., the attributes that are assumed 
        # to be real).
        self.ontic = self.define_ontic()
        
        # Determine the derived states (i.e., the transformed or measured 
        # attributes that follow from the base ontic states and which serve as
        # the support \hat{A}^{(R)} for the real hull).
        self.derived = self.compute_derived()
        
        # Determine the hulls, both real and unreal, that result from the 
        # derived states.
        self.hulls = self.compute_hulls()
        
        self.validate()
        
    def validate(self):

        assert (self.hulls.real.support.values.T == self.hulls.real.hull.points).all()
        assert (self.hulls.unreal.support.values.T == self.hulls.unreal.hull.points).all()       
        
    def define_ontic(self):
        """
        Define the base ontic states.

        Returns
        -------
        ontic : pandas.DataFrame 
            Data frame of dimension `N·K` where `N` is the number of attributes 
            and `K` the number of such combinations.
        """    
        
        ontic = None
        
        return ontic
 
    def compute_derived(self):
        """
        Execute the logical operations that (potentially) reduce the "realm of 
        possibilities". These operations, which typically correspond to
        measurements, produce a set of derived states.

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
    
    @staticmethod
    def distance(mu, support, p_pi):
        
        D = mu - np.dot(support, p_pi)
        D = np.sqrt(np.dot(D, D))
        
        return D
    
    @staticmethod
    def consistency_check(p, tol=1e-7):
        """
        Check that the probabilities are in [0, 1] and add up to unity.
        """

        check = [abs(p.sum() - 1) < tol]

        for x in p:
            check += [x <= 1 + tol and x >= 0 - tol]

        return False not in check    
   
    def violation(self, mu, delta_mu=None, hull='real', method='SLSQP'):
        """
        Compute the distance of various points form the hulls.

        Parameters
        ----------
        mu : np.array
            Measurement vector.
        delta_mu : np.array, None
            Sphere of uncertainty around mu
        hull : str, optional
            Hull from which the distance to ``mu`` is computed.

        Returns
        -------
        D : float
            Distance from the hull. This is positive if outside the hull and
            negative if inside it.
        closest : np.array
            Closest point on the ``hull`` to ``mu``. This is equal to ``mu`` if
            ``mu`` is already on the ``hull``.
        p_pi : np.array
            Probability mass distribution of the support points of the ``hull``
            associated with the closest point ``closest``.
        stderr : float
            Number of standard errors from the mean of ``mu`` from the 
            ``hull``.
        """
        
        assert hull in self.hulls.__dict__.keys()
        
        if isinstance(hull, str):
            hull = getattr(self.hulls, hull).hull
        support = hull.points
            
        # TODO
        closest = np.array([np.nan]*support.shape[1])
        p_pi = np.random.rand(support.shape[0])
        p_pi /= p_pi.sum()
        if delta_mu is not None:
            stderr = np.sqrt(np.dot(delta_mu, delta_mu))
        else:
            stderr = np.nan

        closest = minimize(
            lambda x: self.distance(mu, support.T, x), 
            p_pi, 
            method=method, 
            # The probabilities should be bound within [0, 1].
            bounds=tuple([(0, 1)] * support.shape[0]), 
            constraints=([{'type': 'eq', 'fun': lambda p: p.sum() - 1}]))
        
        p_pi = closest.x
        D = self.distance(mu, support.T, p_pi)       
        closest = np.dot(support.T, p_pi)
        
        assert self.consistency_check(p_pi)
        
        print("Distance from the real hull:", round(D, 5))
        if not np.isnan(stderr):
            print("Number of standard errors:", round(D/stderr, 5))        
        
        return SimpleNamespace(
            **dict(D=D, closest=closest, p_pi=p_pi, stderr=stderr))
