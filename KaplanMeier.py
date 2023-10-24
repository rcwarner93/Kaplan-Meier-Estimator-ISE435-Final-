"""
The Kaplan Meier Plot Program for ISE 435 Project
12/6/2022
Author: Robert Warner

Given data as a .csv file with columns named:
elementID | time | event_type

This program uses the following libraries:

pandas to read a .csv file and modify data frames (tables)
numpy to perform mathematical operations on the data
seaborn to plot the resulting Kaplan Meier Estimate to a graph

In order to output a plotted survival estimate line using the 
Kaplan Meier Estimate formula
"""
#%%
# Importing the required libraries
import pandas as pd
import numpy as np
import seaborn as sns

#%%
# Read in the .csv data file 
df_data = pd.read_csv('kaplan-meier_sample_data_set.csv')

# %%
# Sorting the read in data by its 'time' column row value
df_data.sort_values('time')['time'].unique

#%%
# Initializing a Kaplan Meier Estimate Table (as data frame) to be plotted
columns = ['time', 'elementID', 'event_type', 'Survival Probability']
kaplanMeier = pd.DataFrame(columns = columns, dtype = np.number)
kaplanMeier = kaplanMeier.append(pd.DataFrame([[0, df_data.shape[0], 0, 1]], columns = columns))
#%%
# Calculating and appending the Kaplan Meier Estimate to the data frame to be plotted
for i, t in enumerate(df_data['time']):
    # n(i) is the number of elements known to have survived
    # (i.e., elements that have not failed or been censored) up to time t
    n = np.sum(df_data['time'] >= t)
    # d(i) is the number of events that happened at time t(i) 
    d = np.sum((df_data['time'] == t) & (df_data['event_type'] == 1))
    # s is the kaplan meiers esimate
    kapMeirEstimate = (1 - d / n ) * kaplanMeier.loc[i, 'Survival Probability']
    # Add the Kaplan Meier Estimate row to the new data frame
    kaplanMeier = kaplanMeier.append(pd.DataFrame([[t, n, d, kapMeirEstimate]], index = [i + 1], columns = columns))

# %%
# Plotting the survival estimate line plot using seaborn and a steps-post style
graph = sns.lineplot(data=kaplanMeier, x="time", y="Survival Probability", drawstyle='steps-post')

