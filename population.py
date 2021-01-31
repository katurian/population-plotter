import os
import csv
import pandas as pd
import matplotlib.pyplot as plt

countries_index = []
regions_index = []
years_column_str = []
years_column_int = []

with open("countries.csv") as csv_file:
   for row in csv.reader(csv_file, delimiter=','):
       countries_index.append(row[0])
       regions_index.append(row[2])

with open("years.csv") as csv_file:
   for row in csv.reader(csv_file, delimiter=','):
       for col in row:
           years_column_str.append(str(col))
           years_column_int.append(int(col))

countries_data = pd.read_csv('population.csv', header=None)
countries_data.columns = years_column_str
countries_data.index = countries_index

top_countries_data = countries_data.sort_values(by=['2019'], ascending=False)
top_countries_data.columns = years_column_int
top_countries_data = top_countries_data.head(10)
top_countries = list(top_countries_data.index)

countries_data.columns = years_column_int

regions_data = pd.read_csv('population.csv', header=None)
regions_data.columns = years_column_int
regions_data.index = regions_index

regions_data = regions_data.T
regions_data = regions_data.groupby(level=0, axis=1).sum()

countries_data = countries_data.T
top_countries_data = top_countries_data.T

def plot_top_countries():
    fig, ax = plt.subplots()
    for country in top_countries:
        ax.plot(top_countries_data.index, top_countries_data[country], label=country)
    plt.legend()
    plt.title('Population Growth of the 10 Most Populous Countries in 2019')
    plt.xlabel('Years')
    plt.ylabel('Population')
    plt.show()

def plot_countries(selected_countries):
    fig, ax = plt.subplots()
    for country in selected_countries:
        ax.plot(countries_data.index, countries_data[country], label=country)
    plt.legend()
    plt.title('Population Growth of Selected Countries')
    plt.xlabel('Years')
    plt.ylabel('Population')
    plt.show()

def plot_regions():
    fig, ax = plt.subplots()
    regions = ['East Asia & Pacific', 'Sub-Saharan Africa', 'Latin America & Caribbean', 'South Asia', 'Europe & Central Asia', 'Middle East & North Africa', 'North America']
    for region in regions:
        ax.plot(regions_data.index, regions_data[region], label=region)
    plt.legend()
    plt.title('Population Growth in Different Regions')
    plt.xlabel('Years')
    plt.ylabel('Population')
    plt.show()
