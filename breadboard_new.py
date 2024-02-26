import serial 

def readserial(comport, baudrate):
        ser = serial.Serial(comport, baudrate, timeout = 0.1)

        while True:
                data = ser.readline().decode().strip()
                if data:
                        print(data)

if __name__ == '__main__':
    readserial('COM4', 9600)