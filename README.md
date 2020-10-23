# Predicting Housing Prices Using Linear Regression

![puget_sound_seattle](data/puget_sound_seattle.jpg)

Author: Mitch Krieger

## Overview
This repository attempts to predict housing prices in King County, Washington (Seattle Area) through mutliple linear regression using various features. Ultimately, using the Recursive Feature Elimation prices for houses in a test set were predicted with an RMSE of 165802.93

## Business Problem
The goal is to predict housing as acurately as possible prices with a somewhat interpretable model.

## Data 

Our target variable in this case is the price each house sold for. The data set contains prices of hosues sold from May 2014 - May 2015 in King County and includes the features ranging detailing specifics about the home (number of bedrooms, bathrooms, square footage, grade of construction), the surrounding area (waterfront access, nearby homes), and geo-spatial data (longitude, latitude, zipcode).

All features in at the outset seem important, but the real estate phrase, "location, location, location" puts particular emphasis on features that have geospatial components. However, such geo-features given in dataset are in Latitude, Longitude and zipcode. Most people don't think in terms of these features , its more common to guage in terms of town/neighborhood. A quick glance at a map of housing prices in King County indicate that proximity to water and proximity to Seattle increase prices as color is darker along the Puget Sound, Lake Washington and Lake Sammaish, as well as trending darker closer to the city.

![prices_map](/data/king_county.png)

## Methods

After an initial Exploratory Data Analysis was formed using various viusalizations, additional features were engineered including, bedrooms per bathroom, bedrooms per square footage, age of the house, and city among others. Then, seven models were created using Multiple Linear Regression. Each progressive model used different methods for feature selection each time. R^2 and RMSE values were tracked to ultimately chose the best model, monitoring for statistical significance of various features and any possible multicolinearity between features.

## Results

Using Recursive Feature Elemination yeilded the best feature selection and that model ended up having the best RMSE of 165802.93. All redisual plots for all models were heteroscedastic indicating that there are still additional features and transformations that could stregnthen the model's predictions.


## Conclusion & Next Steps

Due to repeated heteroscedastic residual plots, the linear regression model still has room for growth. Perhaps with further exploraton a better transformation could be found using a polynomial/logarithmic feature. In addition there may be other ways to engineer features or further flesh out using dummies and/or feature interactions.

## Repository Structure

```
├── README.md           <- The top-level README for reviewers of this project
├── model_creation.ipynb<- Narrative documentation of model creation &  processes in Jupyter notebook
├── Predict_holdout.ipynb<- Narrative documentation of application of model to predictions on a holdout set
├── helper_functions.py <- .py script with functions to quickly get regression stats from SKlearn, StatsModels and residual plots from Seaborn
├── data                <- directory of csv with housing data, shape files and images including final predictions csv
├── pickle              <- directory of pickle files
└── aux_code.ipynb      <- auxilary code used in exploration
```

