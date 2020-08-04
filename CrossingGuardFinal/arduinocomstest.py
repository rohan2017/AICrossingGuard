import serial
import time

# Define the serial port and baud rate.
# Ensure the 'COM#' corresponds to what was seen in the Windows Device Manager
ser = serial.Serial('COM3', 9600)
time.sleep(2)  # wait for the serial connection to initialize

while True:
    user_input = input("\n Type go or stop: ")
    time.sleep(0.1)

    if user_input == "stop":
        ser.write(b'S')
    elif user_input == "go":
        ser.write(b'G')
