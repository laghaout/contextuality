#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 14:42:42 2021

@author: Amine Laghaout
"""

import numpy as np

# Run either locally or from the Docker container.
try:
    import PeresMermin as pm
except:
    from . import PeresMermin as pm

# %% Run the ontology.

def main(
        side=3, 
        mu='IBM'):
    """
    Return the ontology and the violation on a given measurement vector.
    
    NOTE: This only accommodates the Peres-Mermin square for now, but other 
    ontologies could also be used.
    
    Parameters
    ----------
    side : int, optional
        Number of sides in the Peres-Mermin square. The default is 3.
        WARNING: Values above 4 will take an inordinate amount of time.
    mu : str, dict, optional
        Measurement vector. This can be specified by a string, in which case it
        is hard-coded (cf. `mus` below) or a dict, in which case it has to be 
        passed as a dictionary containing a numpy array `mu` (the measurement
        vector itself) and, optionally, another numpy array `delta_mu` (the 
        uncertainty on the measurement vector).

    Returns
    -------
    ontology : Ontology object
        Ontology object.
    violation : SimpleNamespace
        Description of the violation consisting of the Euclidean distance `D`
        to the real hull, the closest point `closest` on the real hull, the 
        closest convex combination of the real vectors `p_pi`, as well as the 
        standard error `stderr` corresponding to the uncertainty around the 
        measurement vector.
        
    """
    
    # Selection of possible measurement vectors ``mu`` with an optional 
    # ``delta_mu`` error vector. Choose one vector and pass it to 
    # ``ontology.violation()`` below.
    if isinstance(mu, str):
        mus = dict(
            # Real vector for the Peres-Mermin square.
            R=dict(mu=np.ones(2*side, dtype=np.int32)),
            # Unreal vector for the Peres-Mermin square.
            U=dict(mu=np.concatenate((np.ones(2*side-1), -np.ones(1)))),
            # Empirical vector for the 3D Peres-Mermin square.
            IBM=dict(
                mu=np.array([0.939, 0.887, 0.833, 0.907, 0.917, -0.504]),
                delta_mu=np.array([3.79, 5.09, 6.12, 4.64, 4.41, 9.55])*1e-3))
        mu = mus[mu]
    else:
        assert isinstance(mu, dict) and 'mu' in mu.keys()
    
    ontology = pm.PeresMermin(side)
    
    violation = ontology.violation(**mu) 
    
    return ontology, violation

# %% Save into variables.

if __name__ == '__main__':
    ontology, violation = main()
    ontic = ontology.ontic
    derived = ontology.derived
    real_support = ontology.hulls.real.support
    unreal_support = ontology.hulls.unreal.support    
