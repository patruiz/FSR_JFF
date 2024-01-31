from pyfirmata import Arduino, util, INPUT
import pandas as pd
import numpy as np 
import time 
from datetime import datetime 
import matplotlib.pyplot as plt 
import os 

def store_voltage(port, time_lim = 10, time_step = 1):
    t1, t2 = time.time(), time.time() 
    voltage = []
    
    while(t2 - t1) <= time_lim:
        time.sleep(time_step)
        t2 = time.time()
        voltage.append([t2-t1, port.read()])
    
    return np.array(voltage)

def csv_export(data):
    data_df = pd.DataFrame(data, columns = ["Time", "Voltage"])
    save_path = os.getcwd() + "\\BetaBoard"
    file_name = "ForceData_" + str(datetime.now().strftime("%Y-%m-%d %H-%M-%S")) + ".csv"
    file_path = save_path + "\\" + file_name
    data_df.to_csv(file_path, index = False)
    print(data_df)

def main():
    board = Arduino("COM3")
    iterator = util.Iterator(board)
    iterator.start()

    result = store_voltage(board.analog[2])
    csv_export(result)

if __name__ == "__main__":
    main()




