# Wildfire Predictor

 Wildfire Prediction 

- Contributors: Pahul Brar, Fiona Chang, Lillian Milroy, Darwin Zhang

Predictive data analysis group project for DSCI 310 (Reproducible and Trustworthy Workflows for Data Science) at the University of British Columbia.

<h3> About Our Project</h3>

In this analysis, we train a linear regression model capable of predicting wildfire intensity, which is measured by the geographic area affected by fires. The trained model performed well when making predictions on unseen data, exhibiting an RMSE of 72.954 and a R-squared score of 0.948. 

We used data about Australian wildfires collected using thermal imaging technology and processed by IBM (Hamann and Schmude, 2021). The [data](https://github.com/Call-for-Code/Spot-Challenge-Wildfires/tree/main) was sourced from GitHub, and the specific csv we used can be accessed [here](https://github.com/Call-for-Code/Spot-Challenge-Wildfires/raw/main/data/Nov_10.zip) (Krook 2021). Each row in the dataset represents a day's worth of information about the number, spread, and intensity of fires within one of seven regions in Australia, dating back to 2005. 

The final report is found <a href="https://github.com/FionaC124/dsci310-group-analysis/blob/main/src/wildfire-prediction.ipynb" title="title">here</a>.
    
<h3> Usage </h3>

If it is your first time running the project, follow these steps:

1. Navigate to the root of this repository from the terminal
2. Run the following command to create an environment:

        conda env create --file environment.yml


3. Start Jupyter Lab with:

        jupyter lab


4. Open ```src/wildfire-prediction.ipynb``` in Jupyter Lab

5. "Under Switch/Select Kernel" choose ```Python [conda env:forestFireEnv]```.

5. Under the "Kernel" menu click "Restart Kernel and Run All Cells...". 

    
 <h3> Dependencies </h3>

You will also need need:

* conda (version 24.1.2 or higher)
* nb_conda_kernels (version 2.3.1 or higher)
+ Python and packages listed in environment.yml

--- 

<h3>  License </h3>

The code within this repository is licensed under the MIT license. See  <a href="https://github.com/FionaC124/dsci310-group-analysis/blob/main/LICENSE" title="title">license</a> for further documentation.

Please provide attribution and link to this webpage if reusing/ remixing.

<h3>  References </h3>

Hamann, H., & Schmude, J. (2021). IBM Developer. https://developer.ibm.com/data/spot-challenge-wildfires/

Krook, D. (2021). Spot Challenge Wildfires. GitHub. https://github.com/Call-for-Code/Spot-Challenge-Wildfires/tree/main