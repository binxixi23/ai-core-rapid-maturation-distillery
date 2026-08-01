#!/usr/bin/env python3
"""
AI-Driven Rapid Maturation Distillery System
Module: dynamic_optimizer.py
Author: Automation System Engineering Team

Computes a real-time delta matrix between the Inlet Sensor Array and the Outlet Sensor Array.
Modulates the physical parameters (Pump RPM, E-Beam kW, Ultrasound Hz) during production.
"""

class DynamicBatchOptimizer:
    def __init__(self, target_profile):
        # Load the destination profile mapping boundaries
        self.target = target_profile
        
        # Hardware limits configuration
        self.MIN_PUMP_RPM = 800
        self.MAX_PUMP_RPM = 1500
        self.MAX_EBEAM_KGY = 8.0

    def compute_molecular_delta(self, inlet_data, outlet_data):
        """Calculates the real-time conversion rates across the activation zone."""
        delta = {
            "Tannin_Extraction_Rate": outlet_data["Tannin"] - inlet_data["Tannin"],
            "Aldehyde_Reduction": inlet_data["Aldehyde"] - outlet_data["Aldehyde"],
            "Esterification_Delta": outlet_data["Ester"] - inlet_data["Ester"]
        }
        return delta

    def optimize_process_parameters(self, current_telemetry, current_hardware):
        """Executes feedback loop control logic based on multi-sensor delta matrices."""
        inlet = current_telemetry["Inlet"]
        outlet = current_telemetry["Outlet"]
        
        # Analyze current transition performance inside the flow pipe
        chmbr_perf = self.compute_molecular_delta(inlet, outlet)
        current_similarity = current_telemetry["Current_Similarity_Score"]
        
        new_cmd = {
            "Pump_Speed_RPM": current_hardware["Pump_Speed_RPM"],
            "EBeam_Dose_kGy": current_hardware["EBeam_Dose_kGy"],
            "Ultrasound_Freq_Hz": current_hardware["Ultrasound_Freq_Hz"]
        }

        # NODE 1: TANNIN / WOOD OIL EXTRACTION
        # Create cavitation by dropping flow rate and raising ultrasound resonance to force alcohol deep into wood pores
        if chmbr_perf["Tannin_Extraction_Rate"] < 0.05 and current_similarity < 95.0:
            if new_cmd["Pump_Speed_RPM"] > self.MIN_PUMP_RPM:
                new_cmd["Pump_Speed_RPM"] -= 50  
                new_cmd["Ultrasound_Freq_Hz"] = 22000  # Shift toward deep cavitation frequency (22kHz)

        # NODE 2: ALDEHYDE REDUCTION (SMOOTHNESS)
        # Increase particle acceleration dose if aldehyde conversion stalls
        if chmbr_perf["Aldehyde_Reduction"] < 0.002 and outlet["Aldehyde"] > self.target["Max_Aldehyde"]:
            if new_cmd["EBeam_Dose_kGy"] < self.MAX_EBEAM_KGY:
                new_cmd["EBeam_Dose_kGy"] += 0.2  

        # NODE 3: TURBULENT MIXING OVERRIDE
        # Force high-velocity turbulent blending as similarity nears completion
        if current_similarity >= 92.0 and current_similarity < 95.0:
            new_cmd["Pump_Speed_RPM"] = self.MAX_PUMP_RPM  
            new_cmd["Ultrasound_Freq_Hz"] = 40000  # Surface polishing frequency

        return new_cmd
