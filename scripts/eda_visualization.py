# eda_visualization.py
# author: Darwin Zhang
# date: 2024-03-14

import click
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

@click.command()
@click.option('--preprocessed-data', type=str, help='Path to the preprocessed data CSV file')
@click.option('--plot-to', type=str, help='Path to the output directory for saving visualizations')
def main(preprocessed_data, plot_to):
    '''Plot features for Exploratory Data Analysis and save visualizations'''

    # Read data from 'preprocessed_data'
    data = pd.read_csv(preprocessed_data)

    # Plot 1: Histogram of Estimated Fire Area
    plt.figure(figsize=(8, 6))
    data['Estimated_fire_area'].plot(kind='hist', bins=10, color='skyblue', edgecolor='black')
    plt.xlabel('Estimated Fire Area')
    plt.ylabel('Frequency')
    plt.title('Histogram of Estimated Fire Area')
    plt.savefig(os.path.join(plot_to, 'histogram_fire_area.png'))

    # Plot 2: Number of Fires in Each Region
    fires_by_region = data['Region'].value_counts().reset_index(name='total_fires').rename(columns={'index': 'Region'})
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Region', y='total_fires', data=fires_by_region, palette='magma')
    for index, row in fires_by_region.iterrows():
        plt.text(index, row['total_fires'], str(row['total_fires']), ha='center', va='bottom')
    plt.xlabel('Region')
    plt.ylabel('Total Number of Fires')
    plt.title('Number of Fires in Each Region')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(plot_to, 'barplot_fires_by_region.png'))

    # Correlation analysis
    # Set seed for reproducibility
    np.random.seed(238)
    numeric_df = data.select_dtypes(include=['float64', 'int64'])
    scaler = StandardScaler()
    scaled_df = scaler.fit_transform(numeric_df)
    scaled_df = pd.DataFrame(scaled_df, columns=numeric_df.columns)
    correlation_matrix = numeric_df.corr()

    # Plot correlation matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='flare', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Matrix')
    plt.savefig(os.path.join(plot_to, 'correlation_matrix.png'))

    # Relevant features based off of correlation matrix
    target_variable = 'Estimated_fire_area'
    relevant_features = correlation_matrix[target_variable].sort_values(ascending=False)[1:]
    print("Relevant features based on correlation with Estimated_fire_area:")
    print(relevant_features)

    click.echo("Exploratory data visualizations created and saved.")

if __name__ == '__main__':
    main()
