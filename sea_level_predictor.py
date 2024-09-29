import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")
    
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])
    
    slope, intercept, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred = pd.Series(range(1880, 2051))
    y_pred = intercept + slope * x_pred
    plt.plot(x_pred, y_pred, color='red', label='Best fit line (1880-2050)')
    
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    x_pred_recent = pd.Series(range(2000, 2051))
    y_pred_recent = intercept_recent + slope_recent * x_pred_recent
    plt.plot(x_pred_recent, y_pred_recent, color='green', label='Best fit line (2000-2050)')
    
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    plt.legend()

    plt.xticks([1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075])
    
    plt.savefig('sea_level_plot.png')
    return plt.gca()
