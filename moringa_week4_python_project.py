Original file is located at
    https://colab.research.google.com/drive/1r9w95y520qtwgCSB40d_fjcdL8-4Tik4
"""

import pandas as pd
#loading the dateset and library
dataset = pd.read_csv('Autolib_dataset (2).csv')
df = pd.DataFrame(dataset)
df.head()

df.info()

df.shape

df.describe

df = df.drop(['Address','Cars','Displayed comment','Geo point','Rental status','Scheduled at','Subscription status','Slots'],axis = 1)

df.drop_duplicates()

#Identifying the most popular hour of the day for picking up a shared electric car (Bluecar) in the city of Paris over the month of April 2018
df1 = df.loc[(df['month'] == 4 ) & (df['City'] == 'Paris') & (df['year'] == 2018)]
diff_values = df1['Bluecar counter'].diff(periods = 1)
df1['diff_values'] = diff_values
df1.groupby(['diff_values']).min().head(1)

diff_values = df['Bluecar counter'].diff(periods = 1)
df['diff_values'] = diff_values
df.groupby(['hour'])['diff_values'].count().sort_values(ascending =False ).head(1)# most popular hour for returning cars

df.groupby(['ID'])['Public name'].count().sort_values(ascending = False).head(1)#most popular station

df1.groupby(['ID'])['Public name'].count().sort_values(ascending = False).head(1)#most popular station at the most popular picking hour

df.groupby(['Postal code'])['diff_values'].count().sort_values(ascending = False).head(1)##finding the most popular postal code

df1.groupby(['Postal code'])['diff_values'].count().sort_values(ascending = False).head(1)#finding the most popular postal code at the most popular picking hour

df.loc[(df['Postal code'] == 75015)].head(1)#checking whether the most popular station belongs to that postal code
