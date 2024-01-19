import os 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from ControlChartFunctions import individuals_chart

data_dir = os.getcwd() + "\\StabilityData\\ReducedData"
# data_dir = "C:\\Users\\pr19556\\OneDrive - Applied Medical\\Documents\\Force Sensing Resistor\\Test Data"
data_list = os.listdir(data_dir)

data_file = data_list[7]
# data_file = "ForceData_2024-01-08 13-26-42.csv"
datafile_dir = data_dir + "\\" + data_file

data_df = pd.read_csv(datafile_dir)
print(data_df)



# df_columns = data_df.columns
# test_data = np.array([], dtype = float)
# for i in range(len(df_columns)):
#     entry = min(data_df[df_columns[i]])
#     test_data = np.append(entry, test_data)

test_data = data_df.to_numpy()
# test_data = test_data.T
print(test_data)

print("\n\n---------- TEST RESULTS ----------")
print(f"Sample Size: {len(test_data)}")
print(f"Average: {round(np.average(test_data), 4)}")
print(f"Standard Deviation: {round(np.std(test_data), 4)}\n")

individuals_chart(test_data)

# plt.plot(np.abs(test_data), 'o--')
# plt.
# plt.show()


