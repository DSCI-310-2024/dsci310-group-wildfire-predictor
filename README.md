# Wildfire Predictor

- Contributors: Pahul Brar, Fiona Chang, Lillian Milroy, Darwin Zhang

Predictive data analysis group project for DSCI 310 (Reproducible and Trustworthy Workflows for Data Science) at the University of British Columbia.

## About Our Project 

In this analysis, we train a linear regression model capable of predicting wildfire intensity, which is measured by the geographic area affected by fires. The trained model performed well when making predictions on unseen data, exhibiting an RMSE of 72.954 and a R-squared score of 0.948. 

We used data about Australian wildfires collected using thermal imaging technology and processed by IBM (Hamann and Schmude, 2021). The [data](https://github.com/Call-for-Code/Spot-Challenge-Wildfires/tree/main) was sourced from GitHub, and the specific csv we used can be accessed [here](https://github.com/Call-for-Code/Spot-Challenge-Wildfires/raw/main/data/Nov_10.zip) (Krook 2021). Each row in the dataset represents a day's worth of information about the number, spread, and intensity of fires within one of seven regions in Australia, dating back to 2005. 

## Report 

The final report can be found in the [`reports`](https://github.com/DSCI-310-2024/dsci310-group-wildfire-predictor/tree/main/reports) directory of the repository as both a rendered HTML and PDF document.

## Dependencies 
The software dependencies in this project are managed via the container solution [Docker](https://www.docker.com/). The `quay.io/jupyter/minimal-notebook:notebook-7.0.6` image provided the foundation for which this project's Docker image is based. A summary of the dependencies used can be found below; a comprehensive listing of dependencies exists in the [`Dockerfile`](https://github.com/DSCI-310-2024/dsci310-group-wildfire-predictor/blob/main/Dockerfile).
* conda (version 24.1.2 or higher)
* nb_conda_kernels (version 2.3.1 or higher)
* Python and packages listed in environment.yml

## Usage

The instructions below will guide you through reproducing the analysis.

### Setup

If it is your first time running the project, follow these steps:

1. Navigate to the root of this repository from the terminal

2. Run the following command to create an environment:

        conda env create --file environment.yml

3. Start Jupyter Lab with:

        jupyter lab &

4. Open ```src/wildfire-prediction.ipynb``` in Jupyter Lab

5. "Under Switch/Select Kernel" choose ```Python [conda env:forestFireEnv]```.

6. Under the "Kernel" menu click "Restart Kernel and Run All Cells...". 

### Docker-Usage 

The following steps describe how to reproduce the analysis using Docker.

1. Install and launch Docker on your computer, make sure its a Linux/amd64 type.

2. Clone our [`Wildfire Github Repository`](https://github.com/DSCI-310-2024/dsci310-group-wildfire-predictor).

### Running our analysis

1. From the command line, navigate to the root directory of the project. Enter the following command to reset the project to a clean state:

        docker-compose run --rm analysis-env make clean
   
2. Next, run the entire analysis by using the following command in the root directory:

        docker-compose run --rm analysis-env make all

### Running tests

Please refer to the [Test Suite](https://github.com/DSCI-310-2024/dsci310-group-wildfire-predictor/blob/main/tests/README.md) for more details on testing. To run tests, navigate to the root of the directory and run the `pytest` command.

### Cleaning up

To shut down the container and tidy up the leftover files, from the terminal where you launched the container, type:
    1. `Cntrl` + `C`
    2. `docker compose rm`

--- 

## License

The code within this repository is licensed under the MIT license. See  <a href="https://github.com/FionaC124/dsci310-group-analysis/blob/main/LICENSE" title="title">license</a> for further documentation.

Please provide attribution and link to this webpage if reusing/ remixing.

<h3>  References </h3>

Hamann, H., & Schmude, J. (2021). IBM Developer. https://developer.ibm.com/data/spot-challenge-wildfires/

Krook, D. (2021). Spot Challenge Wildfires. GitHub. https://github.com/Call-for-Code/Spot-Challenge-Wildfires/tree/main