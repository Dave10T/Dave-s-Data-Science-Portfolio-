import numpy as np 
import pandas as pd
from pandas_datareader import data, wb
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import warnings
warnings.filterwarnings('ignore')

btc = pd.read_csv('/Users/davidtello/Downloads/BTC-USD.csv')
btc.head()
# Shape of the data set
btc.shape
btc.isnull().sum()
# Drop the null entries from the dataset —
btc.dropna(inplace = True, axis = 0)
# Now, let’s check the data type of each column —
btc.dtypes
btc['Date'] = pd.to_datetime(btc['Date'])
btc.head(2)
btc.dtypes
# To get total time duration for which we’re carrying out this analysis —
btc['Date'].max()- btc['Date'].min()
btc.iloc[-90:].describe().astype(int)
# 3. General variation in the stock price
# Before we move on towards further investigation, we’ll set the ‘Date’ column as the index of the dataframe. It makes plotting easy.
btc.index = btc['Date']
#Now plot the closing price (adjusted) of the stock over the period of 2 years to get a general idea of how the stock performed in the given period.
btc['Adj Close'].plot(figsize = (15,8))
#plt.show()
# 4. Day-to-day percentage change(Daily returns)
# Daily percentage change in the price of the stock is calculated on the basis of percentage change between 2 consecutive days’ closing prices. 
# Let’s say if the closing price of the stock yesterday was ₹500 and today the stock closed as ₹550. So, the percentage change is 10%. i.e. ((550–500)500)*100. 
# No mystery here!
# Accordingly, we’ll introduce a new column ‘Day_Perc_Change’ denoting the daily returns in the price of the stock. 
# This can be done using in-built pct_change() function in python.
btc['Day_Perc_Change'] = btc['Adj Close'].pct_change()*100
btc.head()
# You’ll notice that the first value in the ‘Day_Perc_Change’ column is NaN. We’ll drop this row.
btc.dropna(axis = 0, inplace = True)
# Representing daily returns in form of a plot —
btc['Day_Perc_Change'].plot(figsize = (12, 6), fontsize = 12)
# It can be observed that for most of the days, the returns are between -2% to 2% with few spikes in between crossing 6% mark on both the sides.
btc['Day_Perc_Change'].hist(bins = 50, figsize = (10,5)) 
plt.xlabel('Daily returns')
plt.ylabel('Frequency')
#plt.show()
#satistics
btc.Day_Perc_Change.describe()
# 5. Trend Analysis
# Next we add a new column ‘Trend’ whose values are based on the day-to-day percentage change we calculated above. 
# Trend is determined from below relationship —
def trend(x):
  if x > -0.5 and x <= 0.5:
    return 'Slight or No change'
  elif x > 0.5 and x <= 1:
    return 'Slight Positive'
  elif x > -1 and x <= -0.5:
    return 'Slight Negative'
  elif x > 1 and x <= 3:
    return 'Positive'
  elif x > -3 and x <= -1:
    return 'Negative'
  elif x > 3 and x <= 7:
    return 'Among top gainers'
  elif x > -7 and x <= -3:
    return 'Among top losers'
  elif x > 7:
    return 'Bull run'
  elif x <= -7:
    return 'Bear drop'
btc['Trend']= np.zeros(btc['Day_Perc_Change'].count())
btc['Trend']= btc['Day_Perc_Change'].apply(lambda x:trend(x))
btc.head()
# We wish to see how the stock was trending in past 2 years. 
# This can be visualized as a pie chart, with each sector representing the percentage of days each trend occurred. 
# We’ll plot a pie chart for the ‘Trend’ column to visualize the relative frequency of each trend category.
# For this, we’ll use the groupby() function with the trend column to aggregate all days with the same trend into a single group before plotting 
# the pie chart.
# Visualizing Trend Frequency with Pie-Chart —
btc_pie_data = btc.groupby('Trend')
pie_label = sorted([i for i in btc.loc[:, 'Trend'].unique()])
#plt.pie(btc_pie_data['Trend'].count(), labels = pie_label, 
#        autopct = '%1.1f%%', radius = 2)

#plt.show()
# For the period under consideration from mid-Feb 2018 to Feb 2020, the Bitcoin stock was among the top gainers for about 12% of the time, 
# and among the top losers for 10 %. For about 18.9% of the time period, the stock has performed positively on a given day. 
# Likewise, for most period of time (about 29.6%) the stock showed a very slight change in the price.
# These observations are consistent with the daily return histogram we saw in above section.
# 6. Daily Returns and Volume
#plt.stem(btc['Date'], btc['Day_Perc_Change'])
#(btc['Volume']/1000000).plot(figsize = (15, 7.5), 
#                                 color = 'green', 
#                                 alpha = 0.5, title = "Daily volume of trade has been reduced in scale to match with the daily return scale")
# 7. Correlation Analysis Of Stocks with Pair plot and Joint plots
# “Never put all your eggs in a single basket”
# Whenever we go for the diversification of the portfolio, we would NOT want the stocks to be related to each other. Mathematically, 
# Pearson’s correlation coefficient (also called Pearson’s R value) between any pair of stocks should be close to 0. 
# The idea behind is simple — suppose your portfolio comprises of the stocks that are highly correlated, then if one stock tumbles, 
# the others might fall too and you’re at the risk of losing all your investment!
# I selected the aforementioned stocks to perform the correlation analysis. All these stocks are from different segments of Industry and Market cap.
# You are free to choose the stocks of your interest. the procedure remains the same.
# In previous section we’ve used the pre-downloaded csv file for analysis. In this section, we’ll take the help of Pandas web data reader package 
# to extract the prices of stocks.
# import package
# set start and end dates 
# set start and end dates 
# set start and end dates 
start = datetime.datetime(2017, 2, 15)
end = datetime.datetime(2021, 11, 27) 
# extract the closing price data
combined_df = data.DataReader(['BTC-USD', 'ETH-USD','XRP-USD','SOL1-USD', 'MANA-USD', 'ADA-USD'],
'yahoo', start = start, end = end)['Adj Close']
# drop null values
combined_df.dropna(inplace = True, axis = 0)
# display first few rows
combined_df.head(3)
# store daily returns of all above stocks in a new dataframe 
pct_chg_df = combined_df.pct_change()*100
pct_chg_df.dropna(inplace = True, how = 'any', axis = 0)
# plotting pairplot  
import seaborn as sns
sns.set(style = 'ticks', font_scale = 1.25)
sns.pairplot(pct_chg_df)
from scipy.stats import stats
g1 = sns.jointplot('BTC-USD', 'ETH-USD', pct_chg_df, kind = 'scatter')#.annotate(stats.pearsonr)
g2 = sns.jointplot('BTC-USD', 'XRP-USD', pct_chg_df, kind = 'scatter')#.annotate(stats.pearsonr)

plt.show()