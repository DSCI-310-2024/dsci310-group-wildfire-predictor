# test_remse_fxn.py
# author: Pahul Brar
# date: 2024-04-1
import pytest
import numpy as np
import pandas as pd

# Import the rmse function
from src.rmse_fn import rmse

# Test if the rmse function returns the correct value
def test_rmse():
    observed_values = [3, 4, 5]
    predicted_values = [2, 5, 4]
    expected_rmse = np.sqrt(((3-2)**2 + (4-5)**2 + (5-4)**2) / 3)
    calculated_rmse = rmse(observed_values, predicted_values)
    assert np.isclose(calculated_rmse, expected_rmse)

# Test if the rmse function raises a ValueError when inputs are empty
def test_rmse_empty_inputs():
    with pytest.raises(ValueError):
        rmse([], [])

# Test if the rmse function raises a ValueError when inputs have different lengths
def test_rmse_different_lengths():
    with pytest.raises(ValueError):
        rmse([1, 2], [1, 2, 3])

# Test if the rmse function raises a ValueError when inputs are not of the required types
def test_rmse_invalid_inputs():
    with pytest.raises(ValueError):
        rmse(1, 2)

# Test if the rmse function works with a Pandas Series as observed and a NumPy array as predicted
def test_rmse_pd_series_and_np_array():
    observed_series = pd.Series([3, 4, 5])
    predicted_array = np.array([2, 5, 4])
    expected_rmse = np.sqrt(((3-2)**2 + (4-5)**2 + (5-4)**2) / 3)
    calculated_rmse = rmse(observed_series, predicted_array)
    assert np.isclose(calculated_rmse, expected_rmse)

# Run tests
if __name__ == "__main__":
   pytest.main()
