# -*- coding: utf-8 -*-
'''

Lauren Forti
DSCI 200
Week 3 Assignment
1/24/2022

'''

#%%
# imports
import pandas as pd
import matplotlib.pyplot as plt

#%%
'''

1. Load the data 'Top 100 Retailers 2015.csv' from Canvas Week 3 Module and name it 'Top_100'.
    Name the index of Top_100 as Company (Hint: Top_100.index=Top_100.Company).
    Delete the missing data if possible.

'''

# load data
Top_100 = pd.read_csv('Top 100 Retailers 2015.csv')

# name index
Top_100.index = Top_100.Company

# get dimensions of Top_100
print(Top_100.shape)
# drop missing data
Top_100 = Top_100.dropna()
# check if any missing values dropped
print(Top_100.shape)

#%%
'''
2. Select the companies with 10 < Rank <=20 and name the 10 companies as a new data frame named 'Top_20', and sort 'Top_20' by Rank with ascending =True.
    Save Top_20 to an excel file named 'Top_20.xlsx'
'''

# output column names
print(Top_100.columns)

# select companies with Rank <= 20 and sort ascending
Top_20 = Top_100[(Top_100['Rank'] > 10) & (Top_100['Rank'] <= 20)].sort_values(['Rank'])

# save df as excel file
Top_20.to_excel('Top_20.xlsx') 

#%%
'''
3. For the data frame 'Top_20',

    a) plot the bar chart of 'Worldwide_Retail_Sales_million', with x='Company'
    
    b) plot the horizontal bar chart of both 'USA_Retail_Sales_million' and 'Worldwide_Retail_Sales_million', with x='Company', rot=45 , stacked=True.
    Save the figure as 'bar_chart.png'.
    
    c) plot pie charts for both 'USA_Retail_Sales_million' and 'Worldwide_Retail_Sales_million', with figsize=(16, 8), autopct=%1.1f%%, legend=False, subplots=True.
    Save the figure as 'pie_chart.png'
'''

# plot bar chart of Worldwide_Retail_Sales_million
Top_20['Worldwide_Retail_Sales_million'].plot.bar(x = 'Company')
plt.show()
plt.close()

# plot horizontal bar chart of USA_Retail_Sales_million and Worldwide_Retail_Sales_million
Top_20[['USA_Retail_Sales_million', 'Worldwide_Retail_Sales_million', 'Company']].plot.barh(x = 'Company',
                                                                                           rot = 45,
                                                                                           stacked = True)
# save bar chart
plt.savefig('bar_chart.png')
plt.show()
plt.close()

# plot pie charts of USA_Retail_Sales_million and Worldwide_Retail_Sales_million
Top_20[['USA_Retail_Sales_million', 'Worldwide_Retail_Sales_million']].plot.pie(subplots = True,
                                                                                figsize = (16, 8),
                                                                                autopct = '%1.f%%',
                                                                                legend = False)
# save pie chart
plt.savefig('pie_chart.png')
plt.show()
plt.close()

#%%
'''
4. For the data frame 'Top_100',
    a) plot lines of 'USA_Retail_Sales_million' and 'Worldwide_Retail_Sales_million'
    
    b) plot the histograms of all the numerical columns in Top_100 with bins=10, figsize=(6,8).
     Save the figure as 'histogram.png'
   
    c) plot the histogram of 'USA_percentage_Worldwide_Sales' in Top_100 with bins=20.
    
    d) graph scatter plot of 'USA_percentage_Worldwide_Sales' with x='USA_Retail_Sales_million', alpha=0.4, c='Rank', cmap=plt.get_cmap("jet"), colorbar=True.
      Save the figure as 'scatter.png'
   
    e) graph scatter plots for both 'USA_Retail_Sales_million' and Worldwide_Retail_Sales_million' with x='Rank' in one graph.
    Save the figure as 'scatter2.png'
  
    f) plot the scatter matrix for 'Top_100'. Save the figure as 'scatter matrix.png'
   
    g) graph the boxplot of 'USA_percentage_Worldwide_Sales'. Save the figure as 'boxplot.png'
'''

# plot lines of USA_Retail_Sales_million and Worldwide_Retail_Sales_million
Top_100.plot(y = ['USA_Retail_Sales_million', 'Worldwide_Retail_Sales_million'])
plt.show()
plt.close()

# plot histogram of all numerical cols
Top_100.hist(bins = 10,
            figsize = (6, 8))
# save histogram
plt.savefig('histogram.png')
plt.show()
plt.close()

# plot histogram of USA_percentage_Worldwide_Sales
Top_100.hist(column = ['USA_percentage_Worldwide_Sales'],
            bins = 20)
plt.show()
plt.close()

# plot scatter plot of USA_percentage_Worldwide_Sales
Top_100.plot.scatter(x = 'USA_Retail_Sales_million',
                    y = 'USA_percentage_Worldwide_Sales',
                    alpha = 0.4,
                    c = 'Rank',
                    cmap = plt.get_cmap('jet'),
                    colorbar = True)
# save scatter plot
plt.savefig('scatter.png')
plt.show()
plt.close()

# scatter plots of USA_Retail_Sales_million and Worldwide_Retail_Sales_million
# plot for USA_Retail_Sales_million
ax1 = Top_100.plot.scatter(x = 'Rank', 
                          y = 'USA_Retail_Sales_million', 
                          c = 'r')
# plot for Worldwide_Retail_Sales_million
Top_100.plot.scatter(x = 'Rank', 
                    y = 'Worldwide_Retail_Sales_million',
                    c = 'b',
                    # combine scatter plots
                    ax = ax1)
# save scatter plots
plt.savefig('scatter2.png')
plt.show()
plt.close()

# plot scatter matrix
pd.plotting.scatter_matrix(Top_100, 
                           figsize = (15, 15))
# save scatter matrix
plt.savefig('scatter matrix.png')
plt.show()
# close the plot
plt.close('all')

# box plot of USA_percentage_Worldwide_Sales
Top_100.boxplot(column = 'USA_percentage_Worldwide_Sales',
                grid = False)
# save box plot
plt.savefig('boxplot.png')
plt.show()
plt.close()
