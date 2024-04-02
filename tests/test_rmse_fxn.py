import pytest
import numpy as np

# Import the rmse function
from src.regression_functions import rmse

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

# Run tests
if __name__ == "__main__":
   pytest.main()
