from pyfirmata import Arduino, util, INPUT
import pandas as pd
import numpy as np 
import time 
from datetime import datetime 
import matplotlib.pyplot as plt 
import os 
import keyboard 

def read_voltage(port, time_lim, time_step):
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

def main(time_lim, time_step):
    board = Arduino("COM3")
    iterator = util.Iterator(board)
    iterator.start()

    data_df = pd.DataFrame()

    while True:
        try:
            print("Press SPACE to begin test.")
            print(f"Time Limit: {str(float(time_lim, 2))}")
            print(f"Time Step: {str(float(time_step, 2))}")
            keyboard.wait("space")

            result = read_voltage(board.analog[2], time_lim, time_step)
            print(result)
        
        except KeyboardInterrupt:
            csv_export(data_df)
            print(data_df)
            break
        break

if __name__ == "__main__":
    main(10, 1)

