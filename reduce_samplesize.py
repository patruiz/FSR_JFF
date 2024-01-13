import os
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

FILENUM = 2

savefile_dir = os.getcwd() + r"\Data"
os.chdir(savefile_dir)

file_names = os.listdir(savefile_dir)
file_path = savefile_dir + "\\" + file_names[FILENUM]

df = pd.read_csv(file_path, index_col = False)
data = df.to_numpy()
data = data.transpose()

print(f"Original Data Set STD: {str(round(data.std(), 4))}")
print(f"Original Data Set Length: {str(data.size)}")
print(np.max(data))
print(np.min(data))

newdata_69 = np.array([], dtype = int)

count = 0
for i in range(data.size):
    if count == 69:
        newdata_69 = np.append(data[0, i], newdata_69)
        count = 0
    else: 
        count = count + 1

print(f"New Data Set STD: {str(round(newdata_69.std(), 4))}")
print(f"New Data Set Length: {str(newdata_69.size)}")

error = ((abs(newdata_69.std() - data.std()))/(data.std()))*100
print(f"Original vs New Error: {str(round(error, 2))}%")

df = pd.DataFrame(newdata_69)

x = np.array(range(newdata_69.size))

# plt.plot(x, newdata_69)
# plt.show()

new_df = pd.DataFrame(newdata_69)
new_df.to_csv(file_names[FILENUM] + "_NEW", index = False)