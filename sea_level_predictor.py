import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data = df, x = 'Year', y = 'CSIRO Adjusted Sea Level')

    # Create first line of best fit
    bestfit1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_lst1 = list(range(1880, 2051))
    y_lst1 = [bestfit1.slope * i + bestfit1.intercept for i in x_lst1]
    plt.plot(x_lst1, y_lst1)

    # Create second line of best fit
    df_alt = df.loc[df['Year'] >= 2000]
    bestfit2 = linregress(df_alt['Year'], df_alt['CSIRO Adjusted Sea Level'])
    x_lst2 = list(range(2000, 2051))
    y_lst2 = [bestfit2.slope * i + bestfit2.intercept for i in x_lst2]
    plt.plot(x_lst2, y_lst2)

    # Add labels and title
    plt.xlim(1850, 2075)
    plt.ylim(0, 16)
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()