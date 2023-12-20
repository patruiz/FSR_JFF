import os
import keyboard
import numpy as np
import pandas as pd
from datetime import datetime
import serial, serial.tools.list_ports

save_path = os.getcwd()

def get_vals(test_num):
    force_data, data_values = np.array([], dtype = float), 0
    print(f"\n----- TEST {test_num} START -----")
    print(f"\nTest Num: {test_num}")
         
    while data_values <= 69:
        try: 
            data_raw = ser.readline().decode('ascii', errors = 'replace').strip()
        except UnicodeDecodeError as e:
            print(f"UnicodeDecodeError: {e}")
            continue
        
        print(data_raw)
        force_data = np.append(force_data, data_raw)
        data_values = len(force_data)
        
    print(f"\n----- TEST {test_num} END -----\n")

    # print(force_data)
    return force_data 


for port in serial.tools.list_ports.comports():
    info = dict({"Name": port.name, "Description": port.description, "Manufacturer": port.manufacturer, "Hwid": port.hwid})
    if port.manufacturer == "FTDI":
        ser_info = dict({"Name": port.name, "Description": port.description, "Manufacturer": port.manufacturer, "Hwid": port.hwid})

try:
    ser = serial.Serial(port = "COM6", baudrate = 9600, timeout = None)
    print(f"\n----- Connected to {ser_info['Name']} -----\n")

    print("Press Space to Begin Test. . .\n")
  
    test_num, flag = 1, True
    keyboard.wait("space")
    print("\n----- Start Test-----\n")

    final_data = []

    try:
        while True:
            try:
                ser.open()
            except:
                pass
            final_data.append(get_vals(test_num))
            test_num = test_num + 1
            ser.close()

    except KeyboardInterrupt:
        print("\n----- End Test -----\n")
        
        df = pd.DataFrame(final_data, columns = ["Force (lbf)"])
        
        file_name = "Force Data " + str(datetime.now()) + ".csv"
        print(f"File Name: {file_name}")
        print(f"File Directory: {save_path}")

        print("\nForce Value Results\n")
        print(df)
 
        os.chdir(save_path) 
        df.to_csv(file_name, index = True)

        ser.close()
        print(f"\n----- Disconnected from {ser_info['Name']} -----\n")
    
except serial.SerialException:
    print("\n----- Serial Connection Failed -----\n")