import os 
import statistics
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from ControlChartFunctions import individuals_chart

os.system("cls")

# data_dir = os.getcwd() + r"\\CapabilityData"
data_dir = os.getcwd() + "\\BetaBoard"
data_list = os.listdir(data_dir)

# data_file = data_list[1]
# data_file = str(input("Enter Filename: "))
data_file = r"ForceData_2024-03-01 14-40-19"
# data_file = r"ForceData_2024-03-01 14-29-00"
datafile_dir = data_dir + "\\" + data_file + ".csv"

data_df = pd.read_csv(datafile_dir)
print(data_df)

df_columns = data_df.columns
test_data = np.array([], dtype = float)
for i in range(len(df_columns)):
    # entry = min(data_df[df_columns[i]])
    entry = statistics.mode(data_df[df_columns[i]])
    # print(statistics.mode(data_df[df_columns[i]]))
    test_data = np.append(entry, test_data)

# test_data = data_df.to_numpy()
# test_data = test_data.T
print(test_data)

print("\n\n---------- TEST RESULTS ----------")
print(f"Sample Size: {len(test_data)}")
print(f"Average: {round(np.average(test_data), 4)}")
print(f"Standard Deviation: {round(np.std(test_data), 4)}\n")

individuals_chart(test_data, "Open Fixture")

# plt.plot(np.abs(test_data), 'o--')
# plt.
# plt.show()


