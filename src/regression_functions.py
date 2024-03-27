import numpy as np

def rmse(observed, predicted):
    # Convert inputs to NumPy arrays
    observed = np.array(observed)
    predicted = np.array(predicted)

    # Calculate squared differences
    squared_diff = np.square(observed - predicted)

    # Calculate mean of squared differences
    mean_squared_diff = np.mean(squared_diff)

    # Calculate square root of mean squared differences to get RMSE
    rmse_value = np.sqrt(mean_squared_diff)

    return rmse_value

#create a function for plotting
#create a function for residual plots
#make sure to have strict tests built-in so only the requried elements are allowed.