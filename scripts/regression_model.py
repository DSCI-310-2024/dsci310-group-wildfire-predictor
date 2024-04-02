# regression_model.py
# Milestone 2 author: Darwin Zhang 
# date: 2024-03-14
# Milestone 3 author: Pahul Brar
# date: 2024-04-1

import click
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from src.rmse_fn import rmse

@click.command()
@click.option('--preprocessed-data', type=str, help='Path to the processed data file')
@click.option('--results-to', type=str, help='Path directory for where results will be output to')
def main(preprocessed_data, results_to):
    '''Train a linear regression model and save coefficients and predicted values'''

    # Read data from the processed data file
    data = pd.read_csv(preprocessed_data)
    
    # Sort features (X) and target variable (Y)
    X = data[['Count', 'Mean_confidence', 'Mean_estimated_fire_brightness', 'Mean_estimated_fire_radiative_power']]
    y = data['Estimated_fire_area']

    # Split test, train 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=58)

    # Linear regression model 
    model = LinearRegression()

    # Fit model into training data
    model.fit(X_train, y_train)

    # Make predictions on testing
    y_pred = model.predict(X_test)

    # Evaluating model 
    rmse_value = rmse(y_test, y_pred)
    print("RMSE:", rmse_value)


    r_squared = model.score(X_test, y_test)
    print("R-squared score:", r_squared)

    # Model coefficients
    coefficients = model.coef_

    # Display coefficients in a dataframe
    coefficients_df = pd.DataFrame({'Feature': X.columns, 'Coefficient': coefficients})
    print(coefficients_df)

    # Save coefficients table
    coefficients_df.to_csv(os.path.join(results_to, 'coefficients.csv'), index=False)

    # Plot predicted vs. actual values
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred)
    plt.xlabel('Actual Fire Area')
    plt.ylabel('Predicted Fire Area')
    plt.title('Predicted vs. Actual Fire Area')
    plt.savefig(os.path.join(results_to, 'predicted_vs_actual.png'))
    
    # Line plot for regression model 
    plt.figure(figsize=(6, 4))
    plt.plot(y_test, y_pred, 'o', color='orangered', alpha=0.5)
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], '--', color='black', lw=2)
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.title('Line Plot on Predicting Wildfire Intensity')
    plt.savefig(os.path.join(results_to, 'line_plot.png'))

    # Residual plot for regression model
    residuals = y_test - y_pred
    plt.figure(figsize=(6, 4))
    plt.scatter(y_pred, residuals, color='orangered', alpha=0.5)
    plt.axhline(y=0, color='black', linestyle='--', lw=2)
    plt.xlabel('Predicted')
    plt.ylabel('Residuals')
    plt.title('Residual Plot on Predicting Wildfire Intensity')
    plt.savefig(os.path.join(results_to, 'residual_plot.png'))

    click.echo("Modeling results saved.")

if __name__ == '__main__':
    main()