import pandas as pd
import matplotlib.pyplot as plt

dataFrame = pd.read_csv('Kumpula-June-2016-w-metadata.txt', skiprows=8)
print(dataFrame.columns)

x = dataFrame['YEARMODA']
y = dataFrame['TEMP']

plt.bar(x, y)
plt.title('Kumpula temperatures in June 2016')
plt.xlabel('Date')
plt.ylabel('Temperature [F]')
# plt.text(20160604.0, 68.0, 'High temperature in early June')
plt.axis([20160615, 20160630, 55.0, 70.0])

plt.show()
