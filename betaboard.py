from pyfirmata import Arduino, util , INPUT
import pandas as pd, numpy as np
import time 
from datetime import datetime
import matplotlib.pyplot as px


board = Arduino('COM3')
iterator = util.Iterator(board)
iterator.start()

def store_voltage(port, time_lim = 10, time_step=1):
    t1 = time.time() 
    t2 = time.time() 
    voltages = []
    while (t2 - t1) <= time_lim:
        time.sleep(time_step)
        t2 = time.time()
        voltages.append(
            [t2 - t1, port.read()]
        )
    return np.array(voltages)

def get_fsr(volt, res):
    # Vo = Vcc ( R / (R + FSR) )
    # vo/vcc = volt
    # volt = r/(r + fsr) => r+fsr = r/volt => fsr = r/volt - r =>  fsr = r(1/volt - 1)
    if np.isclose(volt, 0):
        return np.inf
    return res * (1/volt - 1)

def run_experiment(port, time_lim, time_step, resistor_val, force, filename):
    result = store_voltage(port, time_lim, time_step)

    result_df = pd.DataFrame(result, columns = ["time", "voltage"])
    print(result_df)
    
    # result_df = pd.DataFrame(result, columns=['time', 'voltage'])
    # print(result_df)
    # result_df['date'] = str(datetime.today()).split(' ')[0]
    # result_df['resistance'] = float(resistor_val)
    # result_df['force'] = float(force)
    # result_df['name'] = fsr_name
    # result_df['FSR'] = result_df['voltage'].apply(lambda x: get_fsr(x, resistor_val))
    # result_df.to_csv('track_force_{0}.txt'.format(str(datetime.now()).replace(' ', '').replace(':', '') ))
    # ax = result_df.plot.scatter(x = result_df["time"], y = result_df["voltage"])

    # fig = px.scatter(result_df, x='time', y='voltage', title='Force_{0}:Resist_{1}_FSR_{2}'.format(force, resistor_val, fsr_name))

    # return result_df , fig

    result_df.to_csv(filename)

    return result_df

swag_board = board.analog[2]
swag_board.enable_reporting()
swag_board.read()

time.sleep(1)



# this will run the experiment and measure voltage over time
# g1 = run_experiment(
  #  board.analog[2], 30, 1, 1500, 10, 'circle', 
# )
# g1[1]

def main():

    try:        
        filename = str(input("enter filename: ")) + ".csv"
        time_lim = int(input("enter time limit (seconds): "))
        time_step = int(input("enter time step (seconds): "))
        force = int(input("enter force (lb): "))
            
    except:
        print("try again")


    run_experiment(board.analog[2], time_lim, time_step, 1500, force, filename)

if __name__ == "__main__":
    main()
    
