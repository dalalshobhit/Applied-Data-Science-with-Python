import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read Toronto, Ontario weather data
# Drop unwanted columns and rows
df1 = pd.read_excel('Toronto_Ontario_Historical_Weather_Data.xlsx', skiprows=18, index_col=0)
df1.drop(columns=['Mean Max Temp Flag','Mean Min Temp Flag', 'Mean Temp Flag'], axis=1, inplace=True)
df1.drop(df1.columns[5:], axis=1, inplace=True)
#print(df1.head(5))
# Drop weather data until 1957 to make it time-consistent with Hall Beach weather data
df1.drop(df1.index[0:1404], inplace=True)
# Rename column names
df1.rename(columns={'Mean Max Temp (°C)':'Mean_Max_Toronto_(°C)',
    'Mean Min Temp (°C)':'Mean_Min_Toronto_(°C)','Mean Temp (°C)':'Mean_Mean_Toronto_(°C)'}, inplace=True)
#print(df1.head(5))

# Read Hall Beach, Nunavut weather data
# Drop unwanted columns and rows
df2 = pd.read_excel('Hall_Beach_Nunavut_Historical_Weather_Data.xlsx', skiprows=18, index_col=0)
df2.drop(columns=['Mean Max Temp Flag','Mean Min Temp Flag', 'Mean Temp Flag'], axis=1, inplace=True)
df2.drop(df2.columns[5:], axis=1, inplace=True)
# Drop weather data for the year 2007 to make it time-consistent with Toronto weather data
df2.drop(df2.index[-11:], inplace=True)
# Rename column names
df2.rename(columns={'Mean Max Temp (°C)':'Mean_Max_HallBeach_(°C)',
    'Mean Min Temp (°C)':'Mean_Min_HallBeach_(°C)','Mean Temp (°C)':'Mean_Mean_HallBeach_(°C)'}, inplace=True)
#print(df2.head(5))


# Final data filtering and cleaning for plotting

# Create a jan_temp dataframe with weather data only for month of January for both Toronto and Hall Beach
toronto_jan_temp = df1[df1['Month']==1].copy()    ############ .copy() is used to avoid the SettingWithCopyWarning due to chained indexing
hallbeach_jan_temp = df2[df2['Month']==1].copy()
#print(toronto_jan_temp.head(10))

# Final data cleaning
# Replace NaN values with average values of all records for that column
toronto_jan_temp['Mean_Max_Toronto_(°C)'].fillna(toronto_jan_temp['Mean_Max_Toronto_(°C)'].mean(), inplace=True)
hallbeach_jan_temp['Mean_Max_HallBeach_(°C)'].fillna(hallbeach_jan_temp['Mean_Max_HallBeach_(°C)'].mean(), inplace=True)
toronto_jan_temp['Mean_Mean_Toronto_(°C)'].fillna(toronto_jan_temp['Mean_Mean_Toronto_(°C)'].mean(), inplace=True)
hallbeach_jan_temp['Mean_Mean_HallBeach_(°C)'].fillna(hallbeach_jan_temp['Mean_Mean_HallBeach_(°C)'].mean(), inplace=True)
toronto_jan_temp['Mean_Min_Toronto_(°C)'].fillna((toronto_jan_temp['Mean_Min_Toronto_(°C)'].mean()), inplace=True)
hallbeach_jan_temp['Mean_Min_HallBeach_(°C)'].fillna((hallbeach_jan_temp['Mean_Min_HallBeach_(°C)'].mean()), inplace=True)
#print(hallbeach_jan_temp.head(10))


# Plot 2x1 matrix of line charts to compare the weather trend accross the timeline month wise
# First row will plot maximum, mean and minimum temperature for Toronto in Januray
# Second row will plot maximum, mean and minimum temperature for Hall Beach in January

# Create a figure canvas to plot subplots
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

# Plot 1st subplot to compare average monthly maximum temperature
p11 = ax1.plot(toronto_jan_temp['Year'], toronto_jan_temp['Mean_Max_Toronto_(°C)'], '-', color='coral')
p12 = ax1.plot(toronto_jan_temp['Year'], toronto_jan_temp['Mean_Mean_Toronto_(°C)'], '-', color='goldenrod')
p13 = ax1.plot(toronto_jan_temp['Year'], toronto_jan_temp['Mean_Min_Toronto_(°C)'], '-', color='blue')
#ax1 = sns.lineplot(x='Year', y='Mean_Max_Toronto_(°C)', data=toronto_jan_temp, color='coral')
#ax1 = sns.lineplot(x='Year', y='Mean_Mean_Toronto_(°C)', data=toronto_jan_temp, color='goldenrod')
#ax1 = sns.lineplot(x='Year', y='Mean_Min_Toronto_(°C)', data=toronto_jan_temp, color='blue')
ax1.set_title('Mean monthly Temp. of Toronto in January')
ax1.set_ylabel('Temp. (°C)')
# Hide the spines from the plot
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

# Plot 2nd subplot to compare average monthly mean temperature
p21 = ax2.plot(hallbeach_jan_temp['Year'], hallbeach_jan_temp['Mean_Max_HallBeach_(°C)'], '-', color='crimson')
p22 = ax2.plot(hallbeach_jan_temp['Year'], hallbeach_jan_temp['Mean_Mean_HallBeach_(°C)'], '-', color='gold')
p23 = ax2.plot(hallbeach_jan_temp['Year'], hallbeach_jan_temp['Mean_Min_HallBeach_(°C)'], '-', color='aqua')
ax2.set_title('Mean monthly Temp. of Hall Beach in January')
ax2.set_ylabel('Temp. (°C)')
# Hide the spines from the plot
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

# Add grid lines to plots
ax1.grid(color='grey', linestyle='-', linewidth=0.3, alpha=0.5)
ax2.grid(color='grey', linestyle='-', linewidth=0.3, alpha=0.5)
# Darken the threshold temperature value
ax1.axhline(0, color='black')
ax2.axhline(-25, color='black')

fig.tight_layout()

# Save the plot as a png file
fig.savefig('outputFigure.png')
