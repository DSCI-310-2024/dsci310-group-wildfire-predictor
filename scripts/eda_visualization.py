# eda_visualization.py
# author: Darwin Zhang
# date: 2024-03-14

import click
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)\

from src.scale_data import scale_numeric_df

@click.command()
@click.option('--preprocessed-data', type=str, help='Path to the processed data file')
@click.option('--plot-to', type=str, help='Path to the output directory for saving visualizations')
def main(preprocessed_data, plot_to):
    '''Plot features for Exploratory Data Analysis and save visualizations'''

    # Read data from 'preprocessed_data'
    data = pd.read_csv(preprocessed_data)

    # Plot 1: Histogram of Estimated Fire Area
    plt.figure(figsize = (6, 5))
    data['Estimated_fire_area'].plot(kind = 'hist', bins=30, log=True, color='#8CBCD9')
    mean_val = np.mean(data['Estimated_fire_area'])
    median_val = np.median(data['Estimated_fire_area'])
    plt.axvline(mean_val, color='red', linestyle='--', label = f'Mean: {mean_val: .2f}')
    plt.axvline(median_val, color='blue', linestyle='--', label = f'Median: {median_val: .2f}')
    plt.legend()
    plt.xlabel('Estimated Fire Area (km2)')
    plt.ylabel('Frequency')
    plt.title('Histogram of Estimated Fire Area')
    plt.savefig(os.path.join(plot_to, 'histogram.png'))

    # Plot 2: Number of Fires in Each Region
    fires_by_region = data['Region'].value_counts().reset_index(name='total_fires').rename(columns={'index': 'Region'})
    plt.figure(figsize=(6, 5))
    sns.barplot(x='Region', y='total_fires', data=fires_by_region, color='#8CBCD9')
    for index, row in fires_by_region.iterrows():
        plt.text(index, row['total_fires'], str(row['total_fires']), ha='center', va='bottom')
    plt.xlabel('Region')
    plt.ylabel('Total Number of Fires')
    plt.title('Number of Fires in Each Region')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(plot_to, 'barplot.png'))

    # Plot 3: Fire Area vs. Fire Brightness
    plt.figure(figsize = (7,5))
    sns.scatterplot(data=data, x = "Estimated_fire_area", y = "Mean_estimated_fire_brightness", hue = 'Region', palette = 'colorblind', alpha=0.3) 
    plt.xlabel("Estimated Fire Area (km2)")
    plt.ylabel("Mean Estimated Fire Brightness")
    plt.title("Scatterplot of Estimated Fire Area vs. Mean Estimated Fire Brightness")
    plt.legend(title = "Region")
    plt.grid(True)
    plt.savefig(os.path.join(plot_to, 'scatterplot.png'))

    # Plot 4: Fire Area By Region Over Time
    df_by_yr = data.copy()
    df_by_yr['Date'] = pd.to_datetime(df_by_yr['Date'])
    df_by_yr['Year'] = df_by_yr['Date'].dt.year

    plt.figure(figsize = (7,5))
    sns.lineplot(data = df_by_yr, x = "Year", y = "Estimated_fire_area", hue = 'Region', 
                 palette = 'colorblind', errorbar = None) 
    plt.xlabel("Year")
    plt.ylabel("Estimated Fire Area (km2)")
    plt.title("Estimated Fire Area by Region Over Time")
    plt.legend(title = "Region", loc = 'upper left')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(plot_to, 'lineplot.png'))

    # Correlation analysis
    # Set seed for reproducibility
    scaled_df = scale_numeric_df(data)
    correlation_matrix = scaled_df.corr()

    # Plot correlation matrix
    plt.figure(figsize=(5, 4))
    sns.heatmap(correlation_matrix, annot=True, cmap='flare', fmt=".2f", linewidths=0.5)
    plt.xticks(rotation=45)
    plt.title('Correlation Matrix')
    plt.savefig(os.path.join(plot_to, 'corr_matrix.png'))

    # Relevant features based off of correlation matrix
    target_variable = 'Estimated_fire_area'
    relevant_features = correlation_matrix[target_variable].sort_values(ascending=False)[1:]
    print("Relevant features based on correlation with Estimated_fire_area:")
    print(relevant_features)

    click.echo("Exploratory data visualizations created and saved.")

if __name__ == '__main__':
    main()
