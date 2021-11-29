# The Dave's Tello Data Science Portfolio.
## This is a portfolio that contains the projects that I've been working on.
## [Project 1. Data Analysis & Visualization in Finance](https://github.com/Dave10T/Dave-s-Data-Science-Portfolio-)
   Technical Analysis of Bitcoin and some other cryptocurrencies using Python
   
**Project description:** with an increase in the penetration of analytics into numerous facets of our lives, finance is definitely one of the earliest to catch onto this trend. In this project I have attempted to showcase how data analytics and visualization techniques can be incorporated in the world of cryptocurrencies. Bitcoin aswell as other cryptocurrencies such as ETH, XRP, ADA and many others are the most profitable assets today


## Understanding data & general statistics
For this analysis, I have used 6 years of historical data from around First-Jan 2015 to Nov-2021 of bitcoin. The data was taken from Yahoo Fianance. 
```Import necessary libraries —
   import numpy as np 
   import pandas as pd
   import matplotlib.pyplot as plt
   import seaborn as sns
   import datetime
   import warnings
   warnings.filterwarnings('ignore')
```
### Objectives of this project: to investigate the general variation in the stock price, day-to-day percentage change(Daily returns), trend Analysis, daily returns and volume trading, correlation analysis of stocks with pair plot and joint plots and volatility analysis.

## > Results obtained:

## Price:
![](https://github.com/Dave10T/Dave-s-Data-Science-Portfolio-/blob/main/images/BTC-Price.png)

## We wish to see how the stock was trending in past 5 years. This can be visualized as a pie chart
![](https://github.com/Dave10T/Dave-s-Data-Science-Portfolio-/blob/main/images/PieChart.png)

## Daily Volume Trade
![](https://github.com/Dave10T/Dave-s-Data-Science-Portfolio-/blob/main/images/DailyVolume%20trade.png)

## Correlation
![](https://github.com/Dave10T/Dave-s-Data-Science-Portfolio-/blob/main/images/CorrelationPairpng.png)

## Volatility Analysis 
![](https://github.com/Dave10T/Dave-s-Data-Science-Portfolio-/blob/main/images/VolBTC.png)
![](https://github.com/Dave10T/Dave-s-Data-Science-Portfolio-/blob/main/images/VOL3Crypto.png)

## [Project 2. Data Analysis & Visualization in Finance](https://github.com/Dave10T/Dave-s-Data-Science-Portfolio-)
   Predicting customer attrition using supervised machine learning algorithms in Python
   
   **Project descrption:** Customer attrition (a.k.a customer churn) is one of the biggest expenditures of any organization. If one could figure out why a      customer leaves and when they leave with reasonable accuracy, it would immensely help the organization to strategize their retention initiatives manifold. We make     use of a customer transaction dataset from Kaggle to understand the key steps involved in predicting customer attrition in Python.
   Supervised Machine Learning is nothing but learning a function that maps an input to an output based on example input-output pairs. A supervised machine learning    algorithm analyzes the training data and produces an inferred function, which can be used for mapping new examples. Given that we have data on current and prior     customer transactions in the telecom dataset, this is a standardized supervised classification problem that tries to predict a binary outcome (Y/N).
   
   ## Objectives of the project: To solve some of the key business challenges pertaining to customer attrition such as, 
          ## (1) what is the likelihood of an active customer leaving an organization? 
          ## (2) what are key indicators of a customer churn? 
          ## (3) what retention strategies can be implemented based on the results to diminish prospective customer churn?
 
