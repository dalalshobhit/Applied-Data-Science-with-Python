import pandas as pd
import numpy as np

# Reading and cleaning Energy file

# Read Excel file
energy = pd.read_excel("Energy Indicators.xls", skiprows = 17, skip_footer = 38)

# Drop first 2 columns and rename other columns
# Replace missing data with NaN values
# Convert petjoules to gigajoules (petajoules * 1,000,000)
energy = energy.drop(['Unnamed: 0', 'Unnamed: 2'], axis=1).rename({'Unnamed: 1':'Country','Petajoules':'Energy Supply','Gigajoules':'Energy Supply per Capita','%':'% Renewable'}, axis=1)
energy.replace('...',np.nan, inplace=True)
energy['Energy Supply'] = energy['Energy Supply']*1000000

# Replace the list of countries mentioned in problem with new names
energy.replace(['Republic of Korea','United States of America','United Kingdom of Great Britain and Northern Ireland','China, Hong Kong Special Administrative Region'], ['South Korea','United States','United Kingdom','Hong Kong'], inplace=True)

# Remove numbers and/or parenthesis from countries' names
energy['Country'] = energy['Country'].str.replace(r" \(.*\)","")
energy['Country'] = energy['Country'].str.replace('\d+','')

#print(energy)

# --------------------------------------------------------------------------------------------------------------

# Reading and cleaning World Bank csv File

# Read csv file
GDP = pd.read_csv("world_bank.csv", skiprows = 4)
GDP = GDP.drop(['2016', '2017', 'Unnamed: 62'], axis=1)

# Rename list of countries as mentioned in the problem
GDP.replace(['Korea, Rep.','Iran, Islamic Rep.','Hong Kong SAR, China'],['South Korea','Iran','Hong Kong'], inplace=True)

#print(GDP.head(3))

# --------------------------------------------------------------------------------------------------------------

# Reading and cleaning Sciamgo xlsx file
ScimEn = pd.read_excel("scimagojr.xlsx")

#print(ScimEn)

# --------------------------------------------------------------------------------------------------------------

# Filter 2006 - 2015 data for GDP dataframe
GDP = GDP.drop(GDP.ix[:,'1960':'2005'], axis=1)
#print(GDP.head(2))

# Filter top 15 rows from ScimEn
ScimEn_filtered = ScimEn.drop(ScimEn.index[16:])
#print(ScimEn)

# --------------------------------------------------------------------------------------------------------------

# QUESTION 1
# Merging all Energy and ScimEn dataframe
energy_ScimEn = pd.merge(energy, ScimEn_filtered, left_on = 'Country', right_on = 'Country')
#print(energy_ScimEn)

# Merging energy_ScimEn and GDP dataframe
energy_ScimEn_GDP = pd.merge(energy_ScimEn, GDP, left_on = 'Country', right_on = 'Country Name')

# Reset index and drop other unwanted columns
energy_ScimEn_GDP = energy_ScimEn_GDP.set_index('Country')
energy_ScimEn_GDP = energy_ScimEn_GDP.drop(['Country Name','Country Code','Indicator Name', 'Indicator Code'], axis=1)

print('------------------------------  Question 1  ------------------------------')
print(energy_ScimEn_GDP)


# --------------------------------------------------------------------------------------------------------------

# QUESTION 2

# Merge all 3 dataframes and print the difference of len of currently merged dataframe and length of dataframe in
# question 1 which is 15
first_merge = pd.merge(energy, GDP, left_on = 'Country', right_on = 'Country Name')
second_merge = pd.merge(first_merge, ScimEn, left_on = 'Country', right_on = 'Country')

print('------------------------------  Question 2  ------------------------------')
print(len(second_merge)-len(energy_ScimEn_GDP))


# --------------------------------------------------------------------------------------------------------------

# QUESTION 3

Top15 = energy_ScimEn_GDP
Top15_GDP = Top15.drop(['Energy Supply', 'Energy Supply per Capita', '% Renewable', 'Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index'],axis=1)
avgGDP = Top15_GDP.mean(axis=1, skipna=True)
avgGDP = avgGDP.sort_values(ascending=False)

print('------------------------------  Question 3  ------------------------------')
print(avgGDP)


# --------------------------------------------------------------------------------------------------------------

# QUESTION 4

Top15 = energy_ScimEn_GDP
Top15_GDP = Top15.drop(['Energy Supply', 'Energy Supply per Capita', '% Renewable', 'Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index'],axis=1)
# Calculate mean, sort values and get the diff between years 2015 and 2006
Top15_GDP['avgGDP'] = Top15_GDP.mean(axis=1, skipna=True)
Top15_GDP_sorted = Top15_GDP.sort_values(['avgGDP'], axis=0, ascending=False)
diff = (Top15_GDP_sorted.iloc[[5]]['2015']-Top15_GDP_sorted.iloc[[5]]['2006']).values

print('------------------------------  Question 4  ------------------------------')
print(diff[0])


# --------------------------------------------------------------------------------------------------------------

# QUESTION 5

Top15 = energy_ScimEn_GDP
Top15_GDP = Top15.drop(['Energy Supply', 'Energy Supply per Capita', '% Renewable', 'Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index'],axis=1)
# Calculate mean for each column
mean_ener_sply_per_cap = Top15.mean(axis=0, numeric_only=True)

print('------------------------------  Question 5  ------------------------------')
print(float(mean_ener_sply_per_cap['Energy Supply per Capita']))


# --------------------------------------------------------------------------------------------------------------

# QUESTION 6

Top15 = energy_ScimEn_GDP

print('------------------------------  Question 6  ------------------------------')
print(tuple([Top15['% Renewable'].idxmax(), Top15['% Renewable'].max()]))


# --------------------------------------------------------------------------------------------------------------

# QUESTION 7

Top15 = energy_ScimEn_GDP

# Calculate the ratio between self-citations and total citations and create a new column for this ratios
Top15['ratio'] = Top15['Self-citations']/Top15['Citations']

print('------------------------------  Question 7  ------------------------------')
print(tuple([Top15['ratio'].idxmax(),Top15['ratio'].max()]))


# --------------------------------------------------------------------------------------------------------------

# QUESTION 8

Top15 = energy_ScimEn_GDP

# Calculate the ratio of Energy Supply and Energy Supply per Capita to find the total population
Top15['tot_pop'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
countries_pop = Top15['tot_pop']
# Sort population series in descending order
sorted_series = countries_pop.sort_values(ascending=False)

print('------------------------------  Question 8  ------------------------------')
print(sorted_series.index[2])


# --------------------------------------------------------------------------------------------------------------

# QUESTION 9

Top15 = energy_ScimEn_GDP

# Calculate total populations
Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
ener_sup_per_cap = Top15['Energy Supply per Capita']
citable_per_cap = Top15['Citable documents']/Top15['PopEst']

print('------------------------------  Question 9  ------------------------------')
print(ener_sup_per_cap.corr(citable_per_cap, method='pearson'))


# --------------------------------------------------------------------------------------------------------------

# QUESTION 10

Top15 = energy_ScimEn_GDP

# Create a new column with '1' or '0' based on % Renewable value higher or lower then median value
Top15['HighRenew'] = np.where((Top15['% Renewable'] >= Top15['% Renewable'].median()), 1, 0)
Top15 = Top15.sort_values('Rank')

print('------------------------------  Question 10  ------------------------------')
print(Top15['HighRenew'])


# --------------------------------------------------------------------------------------------------------------

# QUESTION 11

Top15 = energy_ScimEn_GDP

# Create an estimated population column
Top15['Est_Pop'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
Top15.reset_index()
# Define a continent dictionary
ContinentDict  = {'China':'Asia',
                  'United States':'North America',
                  'Japan':'Asia',
                  'United Kingdom':'Europe',
                  'Russian Federation':'Europe',
                  'Canada':'North America',
                  'Germany':'Europe',
                  'India':'Asia',
                  'France':'Europe',
                  'South Korea':'Asia',
                  'Italy':'Europe',
                  'Spain':'Europe',
                  'Iran':'Asia',
                  'Australia':'Australia',
                  'Brazil':'South America'}
# Create a new Continent column and map the dictionary to the dataframe
Top15['Continent'] = Top15.index.map(lambda x: ContinentDict[x])
# Create a new dataframe with aggregate values and grouped by 'Continent'
newTop15 = Top15.groupby('Continent')['Est_Pop'].agg(['size', 'sum', 'mean', 'std'])

print('------------------------------  Question 11  ------------------------------')
print(newTop15)


# --------------------------------------------------------------------------------------------------------------

# QUESTION 12

Top15 = energy_ScimEn_GDP

ContinentDict  = {'China':'Asia',
                  'United States':'North America',
                  'Japan':'Asia',
                  'United Kingdom':'Europe',
                  'Russian Federation':'Europe',
                  'Canada':'North America',
                  'Germany':'Europe',
                  'India':'Asia',
                  'France':'Europe',
                  'South Korea':'Asia',
                  'Italy':'Europe',
                  'Spain':'Europe',
                  'Iran':'Asia',
                  'Australia':'Australia',
                  'Brazil':'South America'}

Top15['Continent'] = Top15.index.map(lambda x: ContinentDict[x])
Top15 = Top15.reset_index()

Top15['bins'] = pd.cut(Top15['% Renewable'], 5, include_lowest=True)
newTop15 = Top15.groupby(by=['Continent', 'bins'])['Country'].agg('size')

print('------------------------------  Question 12  ------------------------------')
print(newTop15)


# --------------------------------------------------------------------------------------------------------------

# QUESTION 13

Top15 = energy_ScimEn_GDP
Top15['PopEst'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
Top15['PopEst'] = Top15['PopEst'].map('{:,f}'.format)

print('------------------------------  Question 13  ------------------------------')
print(Top15['PopEst'])
