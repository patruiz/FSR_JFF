import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 

def individuals_chart(data, title):
    try:
        data = np.abs(data)
        mu = np.average(data)
        sigma = np.std(data)
        # k = len(data)
        k = 3
        LCL = mu - k*sigma
        UCL = mu + k*sigma 

        plt.title(title)
        plt.plot(data, 'o-')
        plt.xlabel("Observation")
        plt.ylabel("Analog Value")
        plt.ylim((200, 700))
        plt.axhline(y = mu, linestyle = "--", color = 'black', label = f"X_Bar = {round(mu, 4)}")
        plt.axhline(y = LCL, linestyle = "--", color = 'red', label = f"LCL = {round(LCL, 4)}")
        plt.axhline(y = UCL, linestyle = "--", color = 'blue', label = f"UCL = {round(UCL, 4)}")
        plt.legend(loc = 0)
        plt.show()

    except:
        print("Invalid Entry")
