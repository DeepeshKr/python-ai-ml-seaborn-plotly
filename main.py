#!/usr/bin/env python
# coding: utf-8

import matplotlib
matplotlib.use('Agg')  # Use the Agg backend to avoid interactive mode warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px

# Explicitly close all figures before changing the backend
plt.close('all')

# Change the backend
matplotlib.use('TkAgg')  # Use the TkAgg backend for interactive display

# Read the dataset
df = pd.read_csv('Automobile (1).csv')

def data_summary():
    df.head()
    df.shape

    df.info()
    df.describe(include='all').T
    
def seab_born_graphs():
    # Set Matplotlib style
    sns.set(style="whitegrid")

    # Increase the limit for open figures
    import matplotlib as mpl
    mpl.rcParams['figure.max_open_warning'] = 50

    # Plot a histogram with customizations
    plt.figure(figsize=(10, 6))
    plt.title('Histogram: Price')
    plt.xlim(3000, 50000)
    plt.ylim(0, 70)
    plt.xlabel('Price of cars')
    plt.ylabel('Frequency')
    sns.histplot(data=df, x='price', color='orange')
    plt.savefig('histogram_price.png')  # Save the figure

    # Create a boxplot
    plt.figure(figsize=(10, 6))
    plt.title('Boxplot: Horsepower')
    plt.xlim(30, 300)
    plt.xlabel('Horsepower')
    sns.boxplot(data=df, x='horsepower', color='green')
    plt.savefig('boxplot_horsepower.png')  # Save the figure

    # Create a count plot
    plt.figure(figsize=(20, 7))
    plt.title('Countplot: Car Make')
    plt.xticks(rotation=90)
    sns.countplot(data=df, x='make')
    plt.savefig('countplot_make.png')  # Save the figure

    # Create a scatter plot with customization
    plt.figure(figsize=(10, 6))
    plt.title('Scatterplot: Engine Size vs Horsepower')
    plt.xlabel('Engine Size')
    plt.ylabel('Horsepower')
    sns.scatterplot(data=df, x='engine_size', y='horsepower', hue='fuel_type')
    plt.savefig('scatterplot_engine_size_horsepower.png')  # Save the figure

    # Create a pair plot
    pairplot = sns.pairplot(data=df[['normalized_losses', 'wheel_base', 'curb_weight', 'engine_size', 'price', 'peak_rpm']])
    pairplot.fig.suptitle("Pair Plot", y=1.02)
    plt.savefig('pairplot.png')  # Save the figure

    # Create a heatmap
    plt.figure(figsize=(8, 6))
    plt.title('Heatmap: Correlation')
    sns.heatmap(data=df[['wheel_base', 'curb_weight', 'engine_size', 'price']].corr(), annot=True, cmap='YlGnBu')
    plt.savefig('heatmap_correlation.png')  # Save the figure

    # Show all saved figures
    plt.show()

# ###  Plotly
# ## Plotly
# - **Plotly** is an open-source Python graphing library for building beautiful and interactive visualizations.
def plotly_graphs():
    # let's start by installing plotly
    #!pip install plotly

    # ### Histogram
    his = px.histogram(df, x="price")
    his.show()
    # Save the figure as an HTML file
    his.write_html("histogram.html")

    # ### Bar Plot
    bar = px.bar(df, x='peak_rpm', y='horsepower')
    bar.show()

    # ### Scatter Plot
    scat = px.scatter(df, x='price', y='engine_size')
    scat.show()

    # ### Boxplot with underlying data
    fig = px.box(df, x="fuel_type", y="horsepower", points="all")
    fig.show()


    # ### 3D Scatter Plot
    fig_3d = px.scatter_3d(df, x='fuel_type', y='horsepower', z='price', color='horsepower')
    fig_3d.show()

    # to save the output to an HTML file
    fig_3d.write_html("scatter_3da.html")

plotly_graphs()


