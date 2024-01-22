# Reduces the sample size of each raw data file and compares it to the original file

import os
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

FILENUM = 19

root_dir = os.getcwd()

savefile_dir = root_dir + r"\\StabilityData\\RawData"
os.chdir(savefile_dir)

file_names = os.listdir(savefile_dir)
file_path = savefile_dir + "\\" + file_names[FILENUM]

df = pd.read_csv(file_path, index_col = False)
data = df.to_numpy()
data = data.transpose()

print(f"File Name: {file_names[FILENUM]}")

print(f"Raw Data Set STD: {str(round(data.std(), 4))}")
print(f"Raw Data Set Length: {str(data.size)}\n")

newdata_69 = np.array([], dtype = int)

count = 0
for i in range(data.size):
    if count == 19:
        newdata_69 = np.append(data[0, i], newdata_69)
        count = 0
    else: 
        count = count + 1

print(f"Reduced Data Set STD: {str(round(newdata_69.std(), 4))}")
print(f"Reduced Data Set Length: {str(newdata_69.size)}")

diff = ((abs(newdata_69.std() - data.std()))/(data.std()))*100
print(f"Raw vs Reduced STD Diff: {str(round(diff, 2))}%")

# print(f"File Path: {file_path}")

df = pd.DataFrame(newdata_69)

x = np.array(range(newdata_69.size))

# plt.plot(x, newdata_69)
# plt.show()

os.chdir(root_dir + "\\StabilityData\\ReducedData")

new_df = pd.DataFrame(newdata_69)
new_df.to_csv(file_names[FILENUM], index = False)