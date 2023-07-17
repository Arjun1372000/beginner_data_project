import pandas as pd
# pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
from loguru import logger
import numpy as np

df = pd.read_csv('C:/Users/Arjun V P/Desktop/Pandas/data/survey_results_public.csv')
print(df.shape)

# Q1
print("\n\tWhat is the average age at which 1st code was written?")

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

# print(df['Age1stCode'].value_counts())
# As the column contains strings and NaN values we replace them with appropriate values of
# our choice

df['Age1stCode'] = df["Age1stCode"].replace(['Younger than 5 years', 'Older than 85', np.nan], ['4', '86', '0'])

# without astype(), giving inf error as there are string values in the Series

print('\tAns. {}'.format(df['Age1stCode'].astype(float).mean()))


# input: Series
def split_column_values(series_data):
    series_data = series_data.fillna('None')
    return series_data.str.split(';').explode()
# Output: Series


# function to print the most common value in a series passed
def most_common(series_passed):
    # value_counts() returns in descending order hence index[0] will be the most common
    count_series = split_column_values(series_passed).value_counts().index[0]
    print("\t{}  :  {}".format(df.columns[_], count_series))


# Q2
print("\n\tWhat are the most common values in columns 45:54?\n\tAns.")
for _ in range(45, 54):
    most_common(df.iloc[:, _])

# Q3
print("\n\tConstruct a graph; no:of people who have a SOAccount at that age vs Age.\n\tAns. fig1(var)")
data = df['Age'].loc[df['SOAccount'] == 'Yes'].value_counts()
plt.title('No:of people who have an SOAccount vs Age')
plt.ylabel('No: of people')
plt.xlabel('Age')
fig1 = sns.lineplot(data=data)

# Q4
print("\n\tWhat are the most common values in columns 45:54 w.r.t the OS used?\n\tAns.")
lst = ['Windows', 'Linux-based', 'MacOS', 'BSD']
for i in lst:
    print("\n\t{}\n".format(i))
    for _ in range(45, 54):
        most_common(df.iloc[:, _].loc[df['OpSys'] == i])

# Q5
print("\n\tWhat is the most used SocialMedia in each Country?\n\tAns. co_df")
countries = df['Country'].dropna().unique()
co_so = []
for country in countries:
    temp = df.loc[df['Country'] == country, 'SocialMedia'].value_counts().index[0]
    co_so += [[country, temp]]
    # print("\t{} : {}".format(country, temp))
c_df = pd.DataFrame(co_so, columns=['Country', 'SocialMedia'])

# Q6
print("\n\tWhat is the average, max and min WorkWeekHrs w.r.t Country?\n\tAns. co_hrs_df")
co_hrs = []
for country in countries:
    # nan values means that all the values of WorkWeekHrs that corresponds to that country are nan
    temp = df.loc[df['Country'] == country, 'WorkWeekHrs'].dropna().mean()
    temp1 = df.loc[df['Country'] == country, 'WorkWeekHrs'].dropna().max()
    temp2 = df.loc[df['Country'] == country, 'WorkWeekHrs'].dropna().min()
    co_hrs += [[country, temp, temp1, temp2]]
    # print("\t{} : {} {} {}".format(country, temp, temp1, temp2))
c_hrs_df = pd.DataFrame(co_hrs, columns=['Country', 'MeanWorkWeekHrs', 'MaxWorkWeekHrs', 'MinWorkWeekHrs'])

print("\n\tWhat is the maximum salary(ConvertedComp) w.r.t the Country?\n\tAns. c_comp_df")
co_comp = []
for country in countries:
    temp = df.loc[df['Country'] == country, 'ConvertedComp'].dropna().max()
    co_comp += [[country, temp]]
    # print("\t{} : {}".format(country, temp))
c_comp_df = pd.DataFrame(co_comp, columns=['Country', 'MaxSalaryYearly'])

# Editing of a Column according to a condition
# df.loc[df['CompFreq'] == 'Monthly', 'ConvertedComp'] *= 12
# df.loc[df['CompFreq'] == 'Weekly', 'ConvertedComp'] *= 50
# print(df.loc[df['CompFreq'] == 'Monthly', 'ConvertedComp'])
# print(df.loc[df['CompFreq'] == 'Weekly', 'ConvertedComp'])
