#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 10:40:59 2017

@author: mikejensen

Thise functions can be used to calculate the thiele-small parameters for a griven
loudspeaker.

what is needed:
    For off box calculations
        Voice-coil resistance RE
        Piston radius a
        Resonance f_s
        Voltage accrose speaker VB
        Voltage accrose resistor VA
        Resistance at resonance R_ES
        f1
        f2
    for box calculations
        Resonance f_CT
        Voltage accrose speaker VB
        Voltage accrose resistor VA
        Resistance at resonance R_ECT
        f1
        f2
"""
import numpy as np
import pandas as pd

def paste():
    """
    This function past, wath is stored in cliopboard
    """
    return pd.read_clipboard().values

def save(file_name,variable):
    """
    Save parameter to text file
    
    Input:
        File name
        Variable to be saved
    """
    np.savetxt('file_name', variable, delimiter=',')

def q_vaules(RE,fs,f1,f2,RES):
    """
    This function calculates Q values for a loudspeaker driver.

    ------------------------- OFF BOX -----------------------------------\n
    For off box calculatoins the imputs should be
        Voice-coil resistance RE
        Resonance frequency f_s
        Voltage accrose speaker VB
        Voltage accrose resistor VA
        Resistance at resonance R_ES
        f1, the frequency to the left of f_s where R1 is located on the impedance curve
        f2, is located on the right of f_s
    
    The function returns off box parameters
        Mechanical quality factor Q_MS
        Electrical quality factor Q_ES
        Total quality factor Q_TS
    
    ---------------------- CLOSED BOX ---------------------------------\n
    For off box calculatoins the inputs should be
    And note that CT standds for closed test box
        Resonance frequency f_CT
        Voltage accrose speaker VB
        Voltage accrose resistor VA
        Resistance at resonance R_ECT
        f1, the frequency to the left of f_CT where R1 is located on the impedance curve
        f2, is located on the right of f_CT

    The function then returns the closed box quality factors
        Mechanical quality factor Q_MCT
        Electrical quality factor Q_ECT
        Total quality factor Q_TCT
    """

    qms = fs/(f2-f1)*np.sqrt((RE+RES)/RE)
    
    qes = (RE/RES)*qms
    
    qts = (RE/(RE+RES))*qms
    
    return qms, qes, qts

def vas(v_t,fct,fs,qect,qes):
    """
    Calculates Volume compliance
    
    Inputs:
        Test box volume V_T
        In box resonance frequency f_CT
        Of box resonance frequency fs
        Electrical quality factor Q_ECT
        Electrical quality factor Q_ES
        
    Return:
        Volume compliance
    """
    return v_t*(((fct/fs)*(qect/qes))-1)

def kf(fs,V_AS,c,a):
    """
    Mass correction factor.
    
    This is a factor that is used to convert Q factors, from free air to infinit baffel
    
    Inputs:
        Resonance frequency fs
        Volume compliance V_AS
        Speed of sound c
        Pistion radius a
        
    Returns kf    
    """
    return np.sqrt(1+10.65*((fs**2*V_AS)/(c**2*a)))

def eff(c,fs,vas,qes):
    """
    Calculates the efficiency of the driver
    
    Inputs:
        Speed of sound c
        Off box resonance frequency
        Volume compliance V_AS
        Electrical quality factor Q_ES
    Return:
        n_0
    """
    return ((4*np.pi**2)/c**3)*((fs**3*vas)/qes)

