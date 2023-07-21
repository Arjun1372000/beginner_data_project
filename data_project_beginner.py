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
print("\n\tWhat are the most common values in columns 43:54?\n\tAns.")
for _ in range(43, 54):
    most_common(df.iloc[:, _])

# Q3
print("\n\tConstruct a graph; no:of people who have a SOAccount at that age vs Age.\n\tAns. fig1(var)")
data = df['Age'].loc[df['SOAccount'] == 'Yes'].value_counts()
plt.title('No:of people who have an SOAccount vs Age')
plt.ylabel('No: of people')
plt.xlabel('Age')
fig1 = sns.lineplot(data=data)

# Q4
print("\n\tWhat are the most common values in columns 43:54 w.r.t the OS used?\n\tAns.")
lst = ['Windows', 'Linux-based', 'MacOS', 'BSD']
for i in lst:
    print("\n\t{}\n".format(i))
    for _ in range(43, 54):
        most_common(df.iloc[:, _].loc[df['OpSys'] == i])

# Q5
print("\n\tWhat is the most used SocialMedia in each Country?\n\tAns. co_df")
# c_df is a Series with Country as index
c_df = df.groupby('Country')['SocialMedia'].apply(lambda x: x.value_counts().index[0])

# Q6
print("\n\tWhat is the average, max and min WorkWeekHrs w.r.t Country?\n\tAns. co_hrs_df")
# c_hrs_df is a Dataframe with Country as index
c_hrs_df = df.groupby('Country')['WorkWeekHrs'].agg(['min', 'max', 'mean'])

print("\n\tWhat is the maximum salary(ConvertedComp) w.r.t the Country?\n\tAns. c_comp_df")
# c_comp_df is a Series with Country as index
c_comp_df = df.groupby('Country')['ConvertedComp'].max()

# Editing of a Column according to a condition
# df.loc[df['CompFreq'] == 'Monthly', 'ConvertedComp'] *= 12
# df.loc[df['CompFreq'] == 'Weekly', 'ConvertedComp'] *= 50
# print(df.loc[df['CompFreq'] == 'Monthly', 'ConvertedComp'])
# print(df.loc[df['CompFreq'] == 'Weekly', 'ConvertedComp'])

# This function returns a series of what % from each country uses Python. First we group the dataframe by Country,
# then we access the 'LanguageHaveWorkedWith' column, then use the apply function to apply the desired function to each
# group(Series object), at last accessing the desired value from multi-indexing(Country,'LanguageHaveWorkedWith')

# Q.What is the % of people using Python in each country?
python_pct_byCountry = df.groupby('Country')['LanguageWorkedWith'].apply(lambda x: x.str.split(';').explode().value_counts(normalize=True).mul(100)).loc[:, 'Python']
