import serial
import matplotlib.pyplot as plt
from datetime import datetime
import time

# Configure the serial port
ser = serial.Serial('/dev/ttyACM0', 115200)  # Change '/dev/ttyUSB0' to your Arduino's serial port
time.sleep(3)
ser.reset_input_buffer()
print("connected successfully")

plt.ion()  # Turn on interactive mode for Matplotlib
fig, ax = plt.subplots()  # Create figure and axis objects
line, = ax.plot([], [])  # Create empty line object for plotting

x_data = []
y_data = []

try:
    while True:
        if ser.in_waiting > 0:
            data_str = ser.readline().decode('utf-8').rstrip()
            print(data_str)
            timestamp = datetime.now()
            x_data.append(timestamp)
            y_data.append(float(data_str))
            
            # Update the line plot
            line.set_xdata(x_data)
            line.set_ydata(y_data)
            ax.relim()  # Recalculate axis limits
            ax.autoscale_view()  # Autoscale the view
            fig.canvas.draw()  # Redraw the figure
            
except KeyboardInterrupt:
    print('Closed muscle data \nSwitch off and on for receiving data again')
    ser.close()

plt.ioff()  # Turn off interactive mode
plt.show()
