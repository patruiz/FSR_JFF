from pyfirmata import Arduino, util, INPUT
import pandas as pd
import numpy as np 
import time 
from datetime import datetime 
import matplotlib.pyplot as plt 
import os 
import keyboard 
import os

def read_values(port, time_lim, time_step):
    t1, t2 = time.time(), time.time() 
    values = []
    
    while(t2 - t1) <= time_lim:
        time.sleep(time_step)
        t2 = time.time()
        values.append(port.read())
    
    return np.array(values)

def csv_export(data):
    save_path = os.getcwd() + "\\BetaBoard"
    file_name = "ForceData_" + str(datetime.now().strftime("%Y-%m-%d %H-%M-%S")) + ".csv"
    file_path = save_path + "\\" + file_name
    data.to_csv(file_path, index = False)

def main(comport, time_lim, time_step, savefile):
    os.system('cls')
    
    board = Arduino(comport)
    iterator = util.Iterator(board)
    iterator.start()

    data_df = pd.DataFrame()

    print("\n**************************************\n\n ----- BetaBoard FSR Testing ----- \n\n**************************************\n")
    print("Press ENTER to continue . . . \n")
    keyboard.wait("enter")

    os.system('cls')
    print(f"Connected to: {comport}\n")
    print("----- Test Parameters ----- ")
    print(f"Time per Sample: {str(float(time_lim))} (sec)")
    print(f"Readings per Sample: {str(int(time_lim/time_step))}")
    print("----------------------------\n")

    test_num, data = 1, {}

    print("Press SPACE to begin test . . .")
    keyboard.wait("space")
    while True:
        try:
            os.system("cls")
            print(f"-------- Test Num: {str(int(test_num))} --------\n")
            print(f"Test Num {str(int(test_num))} . . . In Progress\n")
            result = read_values(board.analog[2], time_lim, time_step)
            new_data = {str(test_num): result}
            data.update(new_data)
            print(f"Test Num {str(int(test_num))} . . . Complete\n")
            print("-----------------------------\n")
            test_num = test_num + 1
            print("Press SPACE to begin next test . . .")
            print("Press CTRL+C to end testing . . .")
            keyboard.wait("space")
        
        except KeyboardInterrupt:
            data_df = pd.DataFrame.from_dict(data)
            if savefile == True:
                csv_export(data_df)
            
            print(f"\nDisconnected from {comport}\n")
            break

if __name__ == "__main__":
    main("COM4", 1, .2, False)

