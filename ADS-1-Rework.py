# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 03:41:34 2023

@author: Ismail Sarigat
"""

# Importing libraries
import pandas as pd
import matplotlib.pyplot as plt


# Read csv file
agriculture = pd.read_csv('agri_land.csv')
print(agriculture)

plt.figure(figsize=(8,8))
plt.hist(agriculture["2000"], label="2000", alpha=0.8, bins=4)
plt.hist(agriculture["2010"], label="2010", alpha=0.5, bins=4)
plt.legend()
plt.xlabel("Agricultural Land (%)")
plt.ylabel("Frequency")
plt.show()


# Read csv file 
forest = pd.read_csv('forest_area.csv')
print(forest)

plt.figure(figsize=(12,9))
plt.plot(forest["1990"], color="Brown", label="1990")
plt.plot(forest["2000"], color="Blue", label="2000")
plt.plot(forest["2010"], color="Orange", label="2010")
plt.legend()
plt.xlabel("N")
plt.ylabel("Forest Area (%)")
plt.show()


# Read csv file
region = pd.read_csv('revenue.csv')
print(region)

name = ["North", "East", "South", "West"]

plt.figure()
plt.pie(region["TOTAL REVENUE"], labels=name, autopct='%1.1f%%') 
plt.title("Total Revenue in Every Region")
plt.show()