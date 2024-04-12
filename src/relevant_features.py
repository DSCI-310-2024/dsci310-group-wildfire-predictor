# relevant_features.py
# author: Darwin Zhang
# date: 2024-04-02
import pandas as pd
import numpy as np
def relevant_features(correlation_matrix, target_variable):
    '''
    Takes a correlation matrix and a target variable and returns a list of relevant features.

    Parameters:
    ----------
    correlation_matrix (pandas dataframe): Correlation matrix.
    target_variable (str): Target variable.

    Returns:
    -------
    relevant_features (list): List of relevant features.

    '''
    # Check for empty inputs
    if target_variable not in correlation_matrix.columns:
        return None

    # Check if empty 
    if correlation_matrix.empty:
        return None

    # Check if any numeric columns exist in the df
    relevant_features = correlation_matrix[target_variable].sort_values(ascending=False)[1:]
    return relevant_features