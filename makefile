#Date: 2024-03-25
#Author: Fiona Chang


# All will create each of the targets below
all: data/Raw/Nov_10/Historical_Wildfires.csv \
	data/Processed_Data/Historical_Wildfires.csv \
	src/figures/correlation_matrix.png \
	src/figures/barplot_fires_by_region.png \
	src/figures/histogram_fire_area.png \
	src/figures/predicted_vs_actual.png \
	src/figures/line_plot.png \
	src/figures/residual_plot.png


# Download Data
data/Raw/Nov_10/Historical_Wildfires.csv: scripts/download_data.py
	python scripts/download_data.py \
		--url=https://github.com/Call-for-Code/Spot-Challenge-Wildfires/raw/main/data/Nov_10.zip \
		--output_path=data/Raw/Nov_10 \
		--csv_file=Historical_Wildfires.csv

# Preprocessing data for use
data/Processed_Data/Historical_Wildfires.csv: scripts/preprocessing.py data/Raw/Nov_10/Historical_Wildfires.csv
	python scripts/preprocessing.py \
		--raw-data=data/Raw/Nov_10/Historical_Wildfires.csv \
		--data-to=data/Processed_Data/Historical_Wildfires.csv

# Perform EDA and save plots
src/figures/correlation_matrix.png src/figures/barplot_fires_by_region.png src/figures/histogram_fire_area.png: scripts/eda_visualization.py data/Processed_Data/Historical_Wildfires.csv
	mkdir -p src/figures
	python scripts/eda_visualization.py \
		--preprocessed-data=data/Processed_Data/Historical_Wildfires.csv \
		--plot-to=src/figures

# Perform analysis and save resulting figures
src/figures/predicted_vs_actual.png src/figures/line_plot.png src/figures/residual_plot.png: scripts/regression_model.py data/Processed_Data/Historical_Wildfires.csv
	python scripts/regression_model.py \
		--preprocessed-data=data/Processed_Data/Historical_Wildfires.csv \
		--results-to=src/figures

# Clean all the targets created above
clean:
	rm -f data/Raw/Nov_10/Historical_Wildfires.csv
	rm -f data/Processed_Data/Historical_Wildfires.csv
	rm -rf src/figures
