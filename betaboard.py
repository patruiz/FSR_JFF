# from pyfirmata import Arduino, util, INPUT
import matplotlib.pyplot as plt 
from datetime import datetime 
import keyboard 
import pandas as pd
import numpy as np 
import time 
import os 

def read_value(port, time_lim = 5, time_step = 1):
    t1, t2 = time.time(), time.time() 
    voltage = []
    
    while(t2 - t1) <= time_lim:
        time.sleep(time_step)
        t2 = time.time()
        voltage.append([t2-t1, port.read()])
    
    return np.array(voltage)

def csv_export(data):
    data_df = pd.DataFrame(data)
    save_path = os.getcwd() + "\\BetaBoard"
    file_name = "ForceData_" + str(datetime.now().strftime("%Y-%m-%d %H-%M-%S")) + ".csv"
    file_path = save_path + "\\" + file_name
    data_df.to_csv(file_path, index = False)
    print(data_df)

def main():
    board = Arduino("COM3")
    iterator = util.Iterator(board)
    iterator.start()
    print("\n----- Connected to Arduio -----\n")

    print("Press Space to Begin Test . . . \n")
    print("Press Ctrl + C to End Test . . . \n")
    keyboard.wait("space")

    test_num = 1
    test_data = {}
    while True:
        values = []
        try:
            while len(values) < 690:
                values.append(board.analog[2].read())

            print(f"\n--- START: Test Number {str(test_num)} ---\n")
            new_data = {str(test_num): values}
            test_data.update(new_data)
            print(f"\n--- END: Test Number {str(test_num)} ---\n")
            test_num = test_num + 1


        except KeyboardInterrupt:
            csv_export(test_data)
            print("\n----- Disconnected from Arduio -----\n")
        
        keyboard.wait("space")

if __name__ == "__main__":
    main()




