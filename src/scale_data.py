import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def scale_numeric_df(data):
    '''
    Takes a data set and scales numeric values it by applying StandardScaler() onto the dataframe, then returns it
   
    Parameters:
    ----
    data (pandas dataframe): Dataset with unscaled numeric columns.
    
    Returns:
    ------
    scaled_df (pandas dataframe): Dataset with scaled columns.

    '''
    # Check if df is empty
    if data.empty:
        return None  # Return None if input is empty
    
    # Check if any numeric columns exist in the df
    if not any(data.select_dtypes(include=['float64', 'int64'])):
        return None  # Return None if no numeric columns exist
    
    np.random.seed(238) #keep seeded to ensure reproducibility
    numeric_df = data.select_dtypes(include=['float64', 'int64'])
    scaler = StandardScaler() #create scaler
    scaled_data = scaler.fit_transform(numeric_df) #apply scaler
    scaled_df = pd.DataFrame(scaled_data, columns=numeric_df.columns)
    return scaled_df