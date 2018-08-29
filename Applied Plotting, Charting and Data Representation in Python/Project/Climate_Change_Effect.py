import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read Toronto, Ontario weather data
# Drop unwanted columns and rows
df1 = pd.read_excel('Toronto_Ontario_Historical_Weather_Data.xlsx', skiprows=18, index_col=0)
df1.drop(columns=['Mean Max Temp Flag','Mean Min Temp Flag', 'Mean Temp Flag'], axis=1, inplace=True)
df1.drop(df1.columns[4:], axis=1, inplace=True)
# Drop weather data until 1957 to make it time-consistent with Hall Beach weather data
df1.drop(df1.index[0:1404], inplace=True)
# Rename column names
df1.rename(columns={'Mean Max Temp (°C)':'Mean_Max_Toronto_(°C)',
    'Mean Min Temp (°C)':'Mean_Min_Toronto_(°C)','Mean Temp (°C)':'Mean_Mean_Toronto_(°C)'}, inplace=True)
#print(df1.head(5))
#print(len(df1))

# Read Hall Beach, Nunavut weather data
# Drop unwanted columns and rows
df2 = pd.read_excel('Hall_Beach_Nunavut_Historical_Weather_Data.xlsx', skiprows=18, index_col=0)
df2.drop(columns=['Year','Mean Max Temp Flag','Mean Min Temp Flag', 'Mean Temp Flag'], axis=1, inplace=True)
df2.drop(df2.columns[4:], axis=1, inplace=True)
# Drop weather data for the year 2007 to make it time-consistent with Toronto weather data
df2.drop(df2.index[-11:], inplace=True)
# Rename column names
df2.rename(columns={'Month':'Month_HallBeach','Mean Max Temp (°C)':'Mean_Max_HallBeach_(°C)',
    'Mean Min Temp (°C)':'Mean_Min_HallBeach_(°C)','Mean Temp (°C)':'Mean_Mean_HallBeach_(°C)'}, inplace=True)
#print(df2.head(5))
#print(len(df2))


# Merge (Union all) two dataframes df1 & df2
df = pd.concat([df1,df2], axis=1)
df.drop(df.columns[[4]], axis=1, inplace=True)
#print(df.head(5))

#############################################################################################################

# Plot 3x1 matrix of line charts to compare the weather trend accross the timeline month wise
# First row will plot maximum temperature for both region (Januray)
# Second row will plot mean temperature for both region (January)
# Third row will plot minimum temperature for both region (January)

jan_temp = df[df['Month']==1]
print(jan_temp.head(5))

fig = plt.figure()

plt.subplot(3, 1, 1)
plt.plot(jan_temp['Year'], jan_temp['Mean_Max_Toronto_(°C)'], '-')
plt.title('Comparison of mean maximum temperatures of Toronto, Ontario and Hall Beach, Nunavut')
plt.ylabel('Temperatue (°C)')


fig.savefig('outputFigure.png')
