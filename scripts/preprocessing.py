# preprocessing.py
# author: Fiona Chang
# date: 2024-03-14

import click
import pandas as pd

@click.command()
@click.option('--raw-data', type=str)
@click.option('--output-path', type=str, default='data/Processed_Data/')
def main(raw_data, output_path):
    '''
    Reads in data and preprocesses it to be used in EDA (mainly drops null values).
    Saves the preprocessed data to a CSV file.
    
    Parameters:
    --------
    raw_data: str
        Path to the raw data CSV file
    output_path: str
        Path to save the preprocessed data CSV file

    Returns:
    --------
    None
    '''
    # Read the CSV file
    df = pd.read_csv(raw_data)

    # Clean data from null values
    df_clean = df.dropna()  

    # Save preprocessed data
    output_file = os.path.join(output_path, 'Historical_Wildfires.csv')
    df_clean.to_csv(output_file, index=False)
    click.echo(f"Preprocessed data saved to {output_file}")

if __name__ == '__main__':
    main()
