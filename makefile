#Date: 2024-03-25
#Author: Fiona Chang


# All will create each of the targets below
all: data/Raw/Historical_Wildfires.csv \
     data/Processed\ Data/preprocessed_data.csv \
	 src/figures/histogram.png \
	 src/figures/barplot.png \
	 src/figures/scatterplot.png \
	 src/figures/lineplot.png \
     src/figures/corr_matrix.png \
     src/figures/lineplot-pred.png \
     src/figures/lineplot-resid.png \
	 src/figures/coefficients.csv \
	 src/figures/model_metrics.csv

DOWNLOAD_CMD := curl -sL https://github.com/Call-for-Code/Spot-Challenge-Wildfires/raw/main/data/Nov_10.zip -o /tmp/Nov_10.zip && \
                unzip -j -o /tmp/Nov_10.zip -d data/Raw && \
                rm -f /tmp/Nov_10.zip

# Download Data - Run the download command
data/Raw/Historical_Wildfires.csv:
	$(DOWNLOAD_CMD)

# Preprocessing data for use
data/Processed\ Data/preprocessed_data.csv: scripts/preprocessing.py data/Raw/Historical_Wildfires.csv
	python scripts/preprocessing.py \
		--raw-data=data/Raw/Historical_Wildfires.csv \
		--data-to=data/Processed\ Data/preprocessed_data.csv

# Perform EDA and save plots
src/figures/corr_matrix.png src/figures/barplot.png src/figures/histogram.png src/figures/scatterplot.png src/figures/lineplot.png: scripts/eda_visualization.py data/Processed\ Data/preprocessed_data.csv
	python scripts/eda_visualization.py \
		--preprocessed-data=data/Processed\ Data/preprocessed_data.csv \
		--plot-to=src/figures

# Perform analysis and save resulting figures
src/figures/coefficients.png src/figures/model_metrics.csv src/figures/lineplot-pred.png src/figures/lineplot-resid.png: scripts/regression_model.py data/Processed\ Data/preprocessed_data.csv
	python scripts/regression_model.py \
		--preprocessed-data=data/Processed\ Data/preprocessed_data.csv \
		--results-to=src/figures

# Clean all the targets created above
clean:
	rm -f data/Raw/*
	rm -f data/Processed\ Data/*
	rm -f src/figures/*
