# test_relevant_features.py
# author: Darwin Zhang
# date: 2024-04-02
import pytest
import pandas as pd
from src.relevant_features import relevant_features

# Test with a correlation matrix containing only positive correlations
def test_relevant_features_positive_correlation():
    correlation_matrix = pd.DataFrame({
        'Feature1': [0.5, 0.3, 0.2],
        'Feature2': [0.2, 0.6, 0.8],
        'Feature3': [0.7, 0.1, 0.4],
        'Estimated_fire_area': [1.0, 0.8, 0.6]
    })
    target_variable = 'Estimated_fire_area'
    expected_relevant_features = pd.Series([0.8, 0.6], index=['Feature2', 'Feature3'])
    assert relevant_features(correlation_matrix, target_variable).equals(expected_relevant_features)

# Test with a correlation matrix containing only negative correlations
def test_relevant_features_negative_correlation():
    correlation_matrix = pd.DataFrame({
        'Feature1': [-0.5, -0.3, -0.2],
        'Feature2': [-0.2, -0.6, -0.8],
        'Feature3': [-0.7, -0.1, -0.4],
        'Estimated_fire_area': [1.0, 0.8, 0.6]
    })
    target_variable = 'Estimated_fire_area'
    expected_relevant_features = pd.Series([-0.8, -0.6], index=['Feature2', 'Feature3'])
    assert relevant_features(correlation_matrix, target_variable).equals(expected_relevant_features)

# Test with a correlation matrix containing both positive and negative correlations
def test_relevant_features_mixed_correlation():
    correlation_matrix = pd.DataFrame({
        'Feature1': [0.5, -0.3, 0.2],
        'Feature2': [-0.2, 0.6, -0.8],
        'Feature3': [0.7, -0.1, 0.4],
        'Estimated_fire_area': [1.0, 0.8, 0.6]
    })
    target_variable = 'Estimated_fire_area'
    expected_relevant_features = pd.Series([0.8, 0.6, -0.8, -0.6], index=['Feature1', 'Feature3', 'Feature2', 'Feature1'])
    assert relevant_features(correlation_matrix, target_variable).equals(expected_relevant_features)

# Test with a correlation matrix containing NaN values
def test_relevant_features_nan_values():
    correlation_matrix = pd.DataFrame({
        'Feature1': [0.5, 0.3, None],
        'Feature2': [0.2, None, 0.8],
        'Feature3': [None, -0.1, 0.4],
        'Estimated_fire_area': [1.0, 0.8, 0.6]
    })
    target_variable = 'Estimated_fire_area'
    expected_relevant_features = pd.Series([0.8, 0.6], index=['Feature2', 'Feature3'])
    assert relevant_features(correlation_matrix, target_variable).equals(expected_relevant_features)

# Test with a correlation matrix containing duplicate correlation values
def test_relevant_features_duplicate_values():
    correlation_matrix = pd.DataFrame({
        'Feature1': [0.5, 0.3, 0.5],
        'Feature2': [0.2, 0.5, 0.8],
        'Feature3': [0.5, 0.3, 0.4],
        'Estimated_fire_area': [1.0, 0.8, 0.6]
    })
    target_variable = 'Estimated_fire_area'
    expected_relevant_features = pd.Series([0.8, 0.6], index=['Feature2', 'Feature3'])
    assert relevant_features(correlation_matrix, target_variable).equals(expected_relevant_features)

# Run tests
if __name__ == "__main__":
   pytest.main()