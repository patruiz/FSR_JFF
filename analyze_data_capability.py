import os 
import numpy as np
import pandas as pd 
import scipy.stats as sts 
import matplotlib.pyplot as plt 

# dir = r"C:\Users\pr19556\OneDrive - Applied Medical\Documents\Force Sensing Resistor\Program\FSR_JFF\Data"
test_dir = r"C:\Users\pr19556\OneDrive - Applied Medical\Documents\Force Sensing Resistor\Test Data"

# os.chdir(dir)
os.chdir(test_dir)
file_list = os.listdir()

data = pd.read_csv(file_list[1])
print(round(data.iloc[1]))
print(round(np.average(data.iloc[1])))

data_average = []
# print(data)
for col in range(len(data.columns)):
    data_average.append(round(np.average(data.iloc[col]), 2))

print(data_average)

print(np.std(data_average))
print(data_average)

# data = pd.read_csv(file_list[1], index_col=False)
# data_avg = np.array([], dtype = float)
# data_mode = np.array([], dtype = int)
# elements_count, nums = {}, []


# print(data.loc[:, 1])

# for val in range(len(data)):
#     if len(nums) < 667:
#         nums.append(int(val))
#         print(nums)
#     elif len(nums) == 667:
#         print(nums)
#         data_avg = np.append(sum(nums), data_avg)
#         data_mode = np.append(sts.mode(nums), data_mode)

#         for element in nums:
#             if element in elements_count: 
#                 elements_count[element] = elements_count[element] + 1
#             else:
#                 elements_count[element] = 1
        
#         nums = []


# for key, value in elements_count.items():
#     print(f"{key}: {value}")

# print(data_mode)


# print(len(data_10avg))

y = np.array([], dtype = int)
for val in range(len(data)):
    y = np.append(y, val)

# plt.scatter(y, data)
# plt.show()

# plt.plot(data, marker = "x", linestyle = "-")
# plt.ylim(215,255)
# plt.show()