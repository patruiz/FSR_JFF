# from pyfirmata import Arduino, util, INPUT
import matplotlib.pyplot as plt 
from datetime import datetime 
import keyboard 
import pandas as pd
import numpy as np 
import time 
import os 
import keyboard 
import serial

def read_values(port, time_lim, time_step):
    t1, t2 = time.time(), time.time() 
    values = []
    
    while(t2 - t1) <= time_lim:
        time.sleep(time_step)
        t2 = time.time()
        values.append(float(port.read()))
    
    return np.array(values, dtype = int)

def readserial(comport, baudrate, time_lim, time_step):
        ser = serial.Serial(comport, baudrate, timeout = time_step)
        data = []
        while len(data) < time_lim:
            try:
                val = int(ser.readline().decode().strip())
                data.append(val)
            except:
                pass
        return data

def readserial1(comport, baudrate):
    ser = serial.Serial(comport, baudrate)
    data = []
    while len(data) < 69:
        try:
            data.append(int(ser.readline().decode().strip()))
        except:
            pass

    return data

def csv_export(data):
    save_path = os.getcwd() + "\\BetaBoard"
    file_name = "ForceData_" + str(datetime.now().strftime("%Y-%m-%d %H-%M-%S")) + ".csv"
    file_path = save_path + "\\" + file_name
    data.to_csv(file_path, index = False)

def serialport(comport, baudrate):
    ser = serial.Serial(comport, baudrate)
    try:
        while True:
            print(ser.readline().decode().strip())
    except KeyboardInterrupt:
        False
    
def calcResistance(*resistors):
    Rs, R_total = [], 0
    for R in resistors:
        R_total = R_total + R**(-1)
    
    print(R_total**(-1))
    


def main(comport, time_lim, time_step, savefile):
    os.system('cls')
    
    # board = Arduino(comport)
    # iterator = util.Iterator(board)
    # iterator.start()

    # swag_board = board.analog[2]
    # swag_board.enable_reporting()

    data_df = pd.DataFrame()  

    print("\n**************************************\n\n ----- BetaBoard FSR Testing ----- \n\n**************************************\n")
    print("Press ENTER to continue . . . \n")
    keyboard.wait("enter")

    os.system('cls')
    print(f"Connected to: {comport}\n")
    print("----- Test Parameters ----- ")
    print(f"Time per Sample: {str(float(time_lim*time_step))} (sec)")
    # print(f"Readings per Sample: {str(int(time_lim/time_step))}")
    print("----------------------------\n")

    test_num, data = 1, {}

    print("Press SPACE to begin test . . .\n")

    while True:
        try:
            keyboard.wait("space")
            os.system("cls")
            print(f"-------- Test Num: {str(int(test_num))} --------\n")
            print(f"Test Num {str(int(test_num))} . . . In Progress\n")
            # result = readserial(comport, 9600, time_lim, time_step)
            result = readserial1(comport, 9600)
            new_data = {str(test_num): result}
            data.update(new_data)
            print(f"Test Num {str(int(test_num))} . . . Complete\n")
            print("-----------------------------\n") 
            test_num = test_num + 1
            print(" ")
            print(result)
            print(" ")
            print("Press SPACE to begin next test . . .")
            print("Press CTRL+C to end testing . . .")
        
        except KeyboardInterrupt:
            data_df = pd.DataFrame.from_dict(data)
            print(data_df)

            if savefile == True:
                csv_export(data_df)
            
            print(f"\nDisconnected from {comport}\n")
            break

if __name__ == "__main__":
    # main("COM4", 10, .5, True)
    serialport("COM4", 9600)
    # calcResistance(500, 500, 700, 1500)

