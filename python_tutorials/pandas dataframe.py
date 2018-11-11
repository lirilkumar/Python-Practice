# references
# https://pandas.pydata.org/pandas-docs/stable/api.html#api-dataframe-missing


import pandas as pd
import numpy as np
from datetime import datetime

# --------------------------------------------------

data = [
    ['Amal',    'Liril',    25, 180,    70, 76.4993, 87, 'Gujarat',datetime.strptime('11/10/1992 2:00','%m/%d/%Y %H:%M').replace(second=0,microsecond=0)],
    ['Amal',    'Pankaj',   29, 170,    -65, 44, 0, 'Gujarat',datetime.strptime('3/1/1987 0:11','%m/%d/%Y %H:%M').replace(second=10,microsecond=0)],
    [np.nan,    'Bhavika',  27, 174,    71, -23, 56, 'Maharastra',datetime.strptime('3/11/1990 3:00','%m/%d/%Y %H:%M').replace(second=0,microsecond=0)],
    ['Gori',    'Jigar',    24, 171,    56, 87, 88, 'Maharastra',datetime.strptime('3/1/1993 0:00','%m/%d/%Y %H:%M').replace(second=0,microsecond=0)],
    ['Bhadra',  'Jigar',    25, np.nan,    75, 95, 90, 'Gujarat',datetime.strptime('3/31/1997 11:00','%m/%d/%Y %H:%M').replace(second=0,microsecond=0)],
    ['Gajra',   'Pankaj',    20, 146,    71, np.nan, 55, np.nan,datetime.strptime('3/21/1988 21:00','%m/%d/%Y %H:%M').replace(second=0,microsecond=0)],
    ['Bhadra',  'Ronak',    23, 176,    0, 84, 52, 'Maharastra',datetime.strptime('9/19/1985 17:00','%m/%d/%Y %H:%M').replace(second=0,microsecond=0)],
]

data2 = [
    [np.nan,    'Shivani',  22, 170,    72, -22.0, 91, 'Himachal',datetime.strptime('3/11/1994 3:00','%m/%d/%Y %H:%M').replace(second=0,microsecond=0)],
    ['Katariya','Hina',    23, np.nan,    71, 90, 22, 'Punjab',datetime.strptime('3/31/1994 11:00','%m/%d/%Y %H:%M').replace(second=0,microsecond=0)],
]

# --------------------------------------------------

df = pd.DataFrame(data,columns=['lname','fname','age','height','weight','ssc','hsc','state','DOB'],index=['001','002','003','004','005','006','007'])
df2 = pd.DataFrame(data2,columns=['lname','fname','age','height','weight','ssc','hsc','state','DOB'],index=['008','009'])

# fname lname age, height, weight, 10th marks 12th marks state email
# print(df)
# print(df.shape)
# print(df.columns)
# print(df['fname'])
# print(df[['fname','lname']])
# print(df[1:3])
# print(df.loc['003'])
# print(df.iloc[-1])

# --------------------------------------------------


# print(df['age']>=25)
# print(df[df['age']>=25])

# print(df[['ssc','hsc']]>70)
# print(df[df[['ssc','hsc']]>70])

# print(df.isin(['Amal','Pankaj']))

# print(df[~df.isin(['Amal'])])

# print(df[df['age'].notnull() & df['height'].isnull()])

# print(df[['fname','lname','ssc']].where(df['ssc']>80,np.nan).dropna())

# print(df[['fname','lname','ssc','hsc']].where(np.logical_and(df['ssc']>50,df['hsc']>50),np.nan).dropna())


# --------------------------------------------------

# print(df.head(1))
# print(df.tail(1))

# for r in df.iteritems():
#     print(r)

# --------------------------------------------------

# print(df.index)

# print(df.blocks)
# print(df.transpose)

# types of datatypes in df
# print(df.dtypes)

# Return a Numpy representation of the DataFrame.
# print(df.values)

# DataFrame.axes	Return a list representing the axes of the DataFrame.
# print(df.axes)

# DataFrame.ndim	Return an int representing the number of axes / array dimensions.
# print(df.ndim)

# DataFrame.size	Return an int representing the number of elements in this object. (cells)
# print(df.size)

# DataFrame.shape	Return a tuple representing the dimensionality of the DataFrame.
# print(df.shape)

# DataFrame.memory_usage([index, deep])	Return the memory usage of each column in bytes.
# print(df.memory_usage())

# DataFrame.empty	Indicator whether DataFrame is empty.
# print(df.empty)


# --------------------------------------------------

# df['total']=df['ssc']+df['hsc']
# print(df.head(2))
# df['total']=df['total']+2
# print(df.head(2))

# df['weekday']=df['DOB'].dt.weekday
# print(df)

# del df['total']
# df.pop('total')
# print(df.head(2))

# df=df[:4].append(df[3:])
# print(df)

# df=df.drop(index="004")
# df.drop(index="004",inplace=True)
# print(df)

# unique values
# print(df['lname'].unique())


# --------------------------------------------------

# data manipulation

# print(df.sum())
# print(df['age'].sum())
# print(df[['age','weight']].sum())

# print(df)
# print(df[3:5].sum(axis=0)) #axis 0 - by column
# print(df[['age']].sum(axis=1))

# --------------------------------------------------

# find nulls (np.nan)
# print(df.isna())
# print(df.isnull())

# replace nulls by interpolation (only numbers)
# df.interpolate(inplace=True)
# df.fillna(0,inplace=True)
# print(df)

# replace values by values
# df.replace('Maharastra','MAH',inplace=True)
# df.replace(np.nan,0,inplace=True)
# print(df)

# remove zeros by interpolation
# df.replace(0,np.nan,inplace=True)
# df.interpolate(inplace=True)
# print(df)


# remove -ves using interpolation

# --------------------------------------------------

# https://pandas.pydata.org/pandas-docs/stable/api.html#datetimelike-properties

# date time values
# print(df['DOB'].dt.time)
# print(df['DOB'].dt.date)

# print(df['DOB'].dt.time.max())
# print(df['DOB'].dt.time.min())

# print(df['DOB'].dt.hour)
# print(df['DOB'].dt.minute)
# print(df['DOB'].dt.second)

# print(df['DOB'].dt.month)
# print(df['DOB'].dt.day)
# print(df['DOB'].dt.year)

# --------------------------------------------------
# statistics

# number nulls per column
# print(df.isnull().sum())

# number nulls per row
# print(df.isnull().sum(axis=1))

# number nulls single column
# print(df['ssc'].isnull().sum())

# number nulls row range
# print(df[:4].isnull().sum(axis=1))


# ------------------------------------------------

# Determine pivot table
# impute_grps = df.pivot_table(values=["ssc","hsc"], index=["lname","fname"])
# print(impute_grps)

# ------------------------------------------------

# transpose
# print(df.T)

# ------------------------------------------------

# sorting
# print(df.sort_values(['lname','fname'],ascending=True))

# ------------------------------------------------

# description of dataframe on numeric fields
# print(df.describe())

# ------------------------------------------------
# resetting index
# print(df.reset_index().index)

# ------------------------------------------------

# replacing values in df
# df.replace(['Amal', 'Bhadra', 'Chandra', 'Gori', 'Gajra'], ['amal', 'bhadra', 'chandra', 'gori', 'gajra'],inplace=True)

# using regex
# df.replace({'M.*': 'Maharastra'}, regex=True,inplace=True)
# print(df)

# ------------------------------------------------
# DataFrame.apply(func[, axis, broadcast, …])	Apply a function along an axis of the DataFrame.
# DataFrame.applymap(func)	Apply a function to a Dataframe elementwise.

# applying function to df
# ageNextYear=lambda s:s.upper()
# print(df['fname'].apply(ageNextYear))

# ip=lambda df:df+1
# print(df[['age','ssc','hsc']].applymap(ip))

# ------------------------------------------------
# rounding
# print(df['ssc'].round(1))
# print(df.round(1))

# ------------------------------------------------
# concat / append data frames (rows)
# print(pd.concat([df,df2]))

#  merge dataframes (cols)
# df3=pd.DataFrame()
# df['result']=np.where(np.logical_and(df['ssc']>35,df['hsc']>=35),'PASS','FAIL')
# df3=df[['result']]
# df.pop('result')
# print(df.merge(df3,right_on=df.index,left_on=df3.index))

# ------------------------------------------------
# model matrix
# print(pd.get_dummies(df['DOB'].dt.hour))


# ------------------------------------------------
# rolling values
# print(df['ssc'].rolling(2).apply(np.mean))


# ------------------------------------------------

# print(df[df['ssc'].lt(70)])


# ------------------------------------------------
# GROUP BY
# http://pandas.pydata.org/pandas-docs/stable/groupby.html

# print(df.groupby(by='lname').sum())
# print(df.groupby(by=['state','lname']).sum())
print(df.groupby(by=['state']).mean())

# ------------------------------------------------

# aggregate
# print(df[['ssc','hsc']].agg(['sum','max','min','mean','prod','std','var','median']))

# print(df.agg({'hsc' : ['sum', 'min'], 'ssc' : ['min', 'max']}))

# print(df.agg("mean", axis="columns"))
# print(df.agg("mean", axis=1))

# print(df.agg("mean", axis="rows"))
# print(df.agg("mean", axis=0))

# print(df.groupby(['fname']).agg(['min', 'max', 'sum']))
# print(df.groupby(['fname']).ssc.agg(['min', 'max', 'sum']))
print(df.groupby(['state'])['ssc','hsc','age'].agg(['min', 'max', 'sum']))

# --------------------------------------------------------------
#                           LINKS
# ______________________________________________________________
# Datetime
# https://pandas.pydata.org/pandas-docs/version/0.21/timeseries.html#epoch-timestamps
# https://pandas.pydata.org/pandas-docs/version/0.21/timeseries.html#
# https://pandas.pydata.org/pandas-docs/version/0.21/timeseries.html#generating-ranges-of-timestamps
# https://pandas.pydata.org/pandas-docs/version/0.21/timeseries.html#indexing
# ______________________________________________________________
