import pandas as pd


dataFrame = pd.read_csv('Kumpula-June-2016-w-metadata.txt', skiprows=8)
# print(dataFrame.columns)
# print(dataFrame.index)
# print(len(dataFrame.index))
# print(dataFrame.shape)
# type(dataFrame)
# print(dataFrame.dtypes)
# print(dataFrame['TEMP'])
# type(dataFrame['TEMP'])
# myList = [1, 2, 3, 4, 5, 6, 7.0]
# mySeries = pd.Series(myList)
# print(mySeries)
# dataFrame['TEMP'].mean()
# dataFrame.describe()
# print(dataFrame['TEMP'].astype(int))
dataFrame['DIFF'] = 0.0
print(dataFrame)
dataFrame['DIFF'].dtypes
dataFrame['DIFF'] = dataFrame['MAX'] - dataFrame['MIN']
print(dataFrame)
dataFrame['DIFF_Min'] = dataFrame['TEMP'] - dataFrame['MIN']
print(dataFrame)
dataFrame['TEMP_Celsius'] = (dataFrame['TEMP'] - 32) / (9/5)
print(dataFrame)
row5 = dataFrame[0:5]
print(row5)
row8 = dataFrame.loc[8]
print(row8)
print(dataFrame.loc[8])
print(row8.TEMP)
print(row8['TEMP'])
temps_5to10 = dataFrame[['TEMP', 'TEMP_Celsius']]
print(temps_5to10)
w_temps = dataFrame.loc[(dataFrame['TEMP_Celsius'] > 15) & (dataFrame['YEARMODA'] > 20160615)]
print(w_temps)
w_temps = w_temps.reset_index(drop=True)
print(w_temps)
w_temps.loc[:4, 'TEMP_Celsius'] = None
print(w_temps)
w_temps_clean = w_temps.dropna(subset=['TEMP_Celsius'])
print(w_temps_clean)
w_temps_filled = w_temps.fillna(0)
print(w_temps_filled)
sorted_temp_a = dataFrame.sort_values(by='TEMP')
print(sorted_temp_a)
sorted_temp_d = dataFrame.sort_values(by='TEMP', ascending=False)
print(sorted_temp_d)
dataFrame['Celsius_rounded'] = dataFrame['TEMP_Celsius'].round(0)
print(dataFrame)
unique = dataFrame['Celsius_rounded'].unique()
unique
uniq_temp_days = len(unique)
print('There were', uniq_temp_days, 'days with unique mean temperatures in June 2016 in Helsinki.')
output_fp = 'Kumpula_temps_June_2016.csv'
dataFrame.to_csv(output_fp, sep=",")
output2 = "Kumpula_temps_aobve15_June_2016.csv"
dataFrame.to_csv(output2, index=False, float_format="%.1f")
