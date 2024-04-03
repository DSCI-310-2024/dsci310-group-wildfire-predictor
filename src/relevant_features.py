# relevant_features.py
# author: Darwin Zhang
# date: 2024-04-02
import pandas as pd
import numpy as np

def relevant_features(correlation_matrix, target_variable):
    return correlation_matrix[target_variable].sort_values(ascending=False)[1:]