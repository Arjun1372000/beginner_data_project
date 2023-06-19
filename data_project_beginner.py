import pandas as pd
# pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
from loguru import logger
import numpy as np

df = pd.read_csv('C:/Users/Arjun V P/Desktop/Pandas/data/survey_results_public.csv')
print(df.shape)
print("\n\tWhat is the average age at which 1st code was written?")

pd.set_option('display.max_columns', 85)
pd.set_option('display.max_rows', 85)

# print(df['Age1stCode'].value_counts())
# As the column contains strings and NaN values we replace them with appropriate values of
# our choice

df['Age1stCode'] = df["Age1stCode"].replace(['Younger than 5 years', 'Older than 85', np.nan], ['4', '86', '0'])

# without astype(), giving inf error as there are string values in the Series

print('\tAns. {}'.format(df['Age1stCode'].astype(float).mean()))


def split_column_values(d):
    d = d.dropna().values.tolist()
    lst1 = []
    for _ in d:
        lst1 += _
    lst = []
    for _ in lst1:
        lst += _.split(';')
    return pd.Series(lst)


def most_common(series_passed):
    count_series = split_column_values(series_passed).value_counts().index[0]
    print("\t{}  :  {}".format(df.columns[_], count_series))


print("\n\tWhat are the most common values in columns 45:54?\n\tAns.")
for _ in range(45, 54):
    most_common(df.iloc[:, [_]])

print("\n\tConstruct a graph; no:of people who have a SOAccount at that age vs Age.\n\tAns. fig1(var)")
data = df['Age'].loc[df['SOAccount'] == 'Yes'].value_counts()
plt.title('No:of people who have an SOAccount vs Age')
plt.ylabel('No: of people')
plt.xlabel('Age')
fig1 = sns.lineplot(data=data)

print("\n\tWhat are the most common values in columns 45:54 w.r.t the OS used?\n\tAns.")
lst = ['Windows', 'Linux-based', 'MacOS', 'BSD']
for i in lst:
    print("\n\t{}\n".format(i))
    for _ in range(45, 54):
        most_common(df.iloc[:, [_]].loc[df['OpSys'] == i])
