import pandas as pd
#pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
from loguru import logger
import numpy as np

df = pd.read_csv('C:/Users/Arjun V P/Desktop/Pandas/data/survey_results_public.csv')
print(df.shape)
print("\n\tWhat is the average age at which 1st code was written?")

pd.set_option('display.max_columns',85)
pd.set_option('display.max_rows',85)

#print(df['Age1stCode'].value_counts())
#As the column contains strings and NaN values we replace them with appropriate values of 
#our choice
   
df['Age1stCode']=df["Age1stCode"].replace(['Younger than 5 years','Older than 85',np.nan],['4','86','0'])

#without .astype(), giving inf error as there are string values in the Series

print('\tAns. {}'.format(df['Age1stCode'].astype(float).mean()))
