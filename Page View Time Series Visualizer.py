import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data and set index to date column
data = pd.read_csv("fcc-forum-pageviews.csv", index_col="date")

# Clean data by filtering out extreme values
data = data[(data > data.quantile(.025)) & (data < data.quantile(.975))]

def draw_line_plot(data):
    plt.figure()
    # Plot line chart using data and set labels and title
    plt.plot(data)
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.show()

def draw_bar_plot(data):
    # Group data by year and month, calculate average page views per month
    data = data.groupby([data.index.year, data.index.month]).mean()
    # Plot bar chart using data and set labels and title
    data.plot(kind="bar")
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.title("Average daily page views for each month grouped by year")
    plt.show()

def draw_box_plot(data):
    # Create year and month columns in data
    data["year"] = data.index.year
    data["month"] = data.index.month
    plt.figure()
    # Create box plot of data by year
    sns.boxplot(x="year", y="page_views", data=data)
    plt.title("Year-wise Box Plot (Trend)")
    plt.xlabel("Year")
    plt.ylabel("Page Views")
    plt.show()
    plt.figure()
    # Create box plot of data by month
    sns.boxplot(x="month", y="page_views", data=data)
    plt.title("Month-wise Box Plot (Seasonality)")
    plt.xlabel("Month")
    plt.ylabel("Page Views")
    plt.show()

