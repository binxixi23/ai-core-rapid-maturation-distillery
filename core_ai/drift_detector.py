#!/usr/bin/env python3
"""
AI-Driven Rapid Maturation Distillery System
Module: drift_detector.py
Author: Automation System Engineering Team

Computes the Mahalanobis Distance (DM) for incoming spectrum vectors.
Flags unexpected agricultural or chemical variances that distort the machine learning models.
"""

import numpy as np

class ModelDriftDetector:
    def __init__(self, mean_vector, inv_covariance_matrix, critical_threshold_t2):
        self.mu = np.array(mean_vector)
        self.inv_cov = np.array(inv_covariance_matrix)
        self.critical_limit = critical_threshold_t2 # Hotelling's T^2 Ellipse Boundary Limit

    def evaluate_spectral_drift(self, live_spectrum_vector):
        """Calculates multi-dimensional distance of raw data vector from calibration base."""
        x = np.array(live_spectrum_vector)
        
        # Mahalanobis Distance Math Execution
        delta = x - self.mu
        mahalanobis_distance_sq = np.dot(np.dot(delta, self.inv_cov), delta.T)
        mahalanobis_distance = np.sqrt(mahalanobis_distance_sq)
        
        # Evaluate drift boundary breach
        if mahalanobis_distance > self.critical_limit:
            return {
                "DRIFT_ALERT": True, 
                "Distance": mahalanobis_distance, 
                "Action": "TRIGGER_LAB_GCMS_SAMPLING"
            }
            
        return {
            "DRIFT_ALERT": False, 
            "Distance": mahalanobis_distance, 
            "Action": "PROCEED"
        }
