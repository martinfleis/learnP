# weather analysis
import pandas as pd


path = '6591337447542dat_August.txt'
data = pd.read_csv(path, sep='\s+', na_values=['*', '**', '***', '****', '*****', '******'])

select_cols = ['YR--MODAHRMN', 'DIR', 'SPD', 'GUS', 'TEMP', 'MAX', 'MIN']
data = data[select_cols]
data.dtypes
name_conversion_dict = {'YR--MODAHRMN': 'TIME', 'SPD': 'SPEED', 'GUS': 'GUST'}
type(name_conversion_dict)
data = data.rename(columns=name_conversion_dict)
data.columns
data.describe()
data.head(30)


def fahrToCelsius(row, src_col, target_col):
    """
    A generic function to convert Fahrenheit temperature into Celsius.

    Parameters
    ----------

    row: pd.Series
        Input row containing the data for specific index in the DataFrame

    src_col : str
        Name of the source column for the calculation. I.e. the name of the column where Fahrenheits are stored.

    target_col : str
        Name of the target column where Celsius will be stored.
    """
    # Convert the Fahrenheit into Celsius and update the target column value
    row[target_col] = (row[src_col] - 32) / 1.8
    return row


# def fahrToCelsius(temp_fahrenheit):
#     """
#     Function to convert Fahrenheit temperature into Celsius.
#
#     Parameters
#     ----------
#
#     temp_fahrenheit: int | float
#         Input temperature in Fahrenheit (should be a number)
#     """
#
#     # Convert the Fahrenheit into Celsius and return it
#     converted_temp = (temp_fahrenheit - 32) / 1.8
#     return converted_temp
#

col_name = 'Celsius'
data[col_name] = None

for idx, row in data.iterrows():
    celsius = fahrToCelsius(row['TEMP'])
    data.loc[idx, col_name] = celsius

data.head()
data['SPEED'] = data['SPEED']*0.44704
data['GUST'] = data['GUST']*0.44704
data.head(30)

data['TIME_str'] = data['TIME'].astype(str)
data.head()
data['TIME_str'].dtypes
type(data.loc[0, 'TIME_str'])

data['TIME_dh'] = data['TIME_str'].str.slice(start=0, stop=10)
data.head()

data['TIME_h'] = data['TIME_str'].str.slice(start=8, stop=10)
data['TIME_h'] = data['TIME_h'].astype(int)
data.head()

aggr_data = pd.DataFrame()
grouped = data.groupby('TIME_dh')

time1 = '2017080400'
group1 = grouped.get_group(time1)
group1

mean_cols = ['DIR', 'SPEED', 'GUST', 'TEMP', 'Celsius', 'TIME_h']
mean_values = group1[mean_cols].mean()
mean_values

mean_values['TIME_dh'] = time1
mean_values

aggr_data = aggr_data.append(mean_values, ignore_index=True)
aggr_data

for key, group in grouped:
    mean_values = group[mean_cols].mean()
    mean_values['TIME_dh'] = key
    aggr_data = aggr_data.append(mean_values, ignore_index=True)

aggr_data = aggr_data.loc[2:]
aggr_data = pd.DataFrame()
aggr_data

std_wind = aggr_data['SPEED'].std()
avg_wind = aggr_data['SPEED'].mean()
print('Std:', std_wind)
print('Mean:', avg_wind)
upper_treshold = avg_wind + (std_wind*2)
print('Upper treshold for outlier:', upper_treshold)
aggr_data['Outlier'] = None

for idx, row in aggr_data.iterrows():
    if row['SPEED'] > upper_treshold:
        aggr_data.loc[idx, 'Outlier'] = True
    else:
        aggr_data.loc[idx, 'Outlier'] = False
print(aggr_data)

storm = aggr_data.loc[aggr_data['Outlier'] == True]
print(storm)

print(storm['TIME_h'].value_counts())

gust_sort = storm.sort_values(by='GUST', ascending=False)
gust_sort


data2 = data.copy()
data2 = data2.apply(fahrToCelsius, src_col='TEMP', target_col='Celsius2', axis=1)
data2.head()
