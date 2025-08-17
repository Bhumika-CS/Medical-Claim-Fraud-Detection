#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 00:58:14 2025

@author: Bhumika
"""

#1. Load and Inspect the Data

import pandas as pd

df = pd.read_excel("/Users/Bhumika/Desktop/python/medical_claims_dummy_dataset_2000.xlsx")


#2. Add Anomaly Detection Logic (Manual Rule-Based)

def get_suspicion_score(row):
    if row['Claim Amount'] > 100000 and row['Procedure Count'] > 6:
        return "High Risk"
    elif row['Claim Amount'] > 50000 or row['Procedure Count'] > 4:
        return "Medium Risk"
    else:
        return "Normal"

df['Suspicion Score'] = df.apply(get_suspicion_score, axis=1)

# 3. Add Provider Risk Score

provider_risk = df[df['Suspicion Score'] == 'High Risk'].groupby('Provider ID').size().reset_index(name='High Risk Claims')

df = df.merge(provider_risk, on='Provider ID', how='left')

df['High Risk Claims'] = df['High Risk Claims'].fillna(0)


import seaborn as sns
import matplotlib.pyplot as plt

top_providers = df[df['Suspicion Score'] == 'High Risk']['Provider ID'].value_counts().head(10)

plt.figure(figsize=(10,6))
plt.figure(figsize=(10,6))
