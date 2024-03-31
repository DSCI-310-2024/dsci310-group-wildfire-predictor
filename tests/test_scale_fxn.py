import pytest
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.scale_data import scale_numeric_df

# Test if scaled df has the same shape (rows & columns) as the original df
def test_scaled_df_shape():
    data = pd.DataFrame(np.random.randn(50, 3), columns=['A', 'B', 'C'])
    scaled_df = scale_numeric_df(data)
    assert data.shape == scaled_df.shape

# Test if scaled df has zero mean (is properly scaled) in each column
def test_scaled_df_zero_mean():
    data = pd.DataFrame(np.random.randn(50, 3), columns=['A', 'B', 'C'])
    scaled_df = scale_numeric_df(data)
    assert np.allclose(np.mean(scaled_df, axis=0), 0)

# Test if scaled df has unit variance (variance = 1) for each column
def test_scaled_df_unit_variance():
    data = pd.DataFrame(np.random.randn(50, 3), columns=['A', 'B', 'C'])
    scaled_df = scale_numeric_df(data)
    assert np.allclose(np.var(scaled_df, axis=0), 1)

# Test if scaled df values match data that's been manually scaled
def test_scaled_manual_values():
    data = pd.DataFrame(np.random.randn(50, 3), columns=['A', 'B', 'C'])
    scaled_df = scale_numeric_df(data)
    numeric_df = data.select_dtypes(include=['float64', 'int64'])
    scaler = StandardScaler()
    manual_scaled_data = scaler.fit_transform(numeric_df)
    manual_scaled_df = pd.DataFrame(manual_scaled_data, columns=numeric_df.columns)
    assert scaled_df.equals(manual_scaled_df)

#Test if function works when df entered is empty
def test_scaled_df_empty():
    data = pd.DataFrame()  # Empty DataFrame
    scaled_df = scale_numeric_df(data)
    assert scaled_df is None

# Test if the function returns None for non-numeric only df
def test_scaled_df_non_numeric():
    data = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': ['x', 'y', 'z']})  # non-numeric DataFrame
    scaled_df = scale_numeric_df(data)
    assert scaled_df is None

# Run tests
if __name__ == "__main__":
   pytest.main()