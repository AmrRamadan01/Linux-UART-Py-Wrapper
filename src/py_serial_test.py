import time
import serial

# Configure the serial connection (parameters may differ based on your device)
ser = serial.Serial(
    port='/dev/ttyS0',  # Specify the serial port (e.g., '/dev/ttyUSB1')
    baudrate=15200,        # Set the baud rate
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

ser.isOpen()
print("Enter your commands below.")
print("Insert \"exit\" to leave the application.")

while True:
    # Get keyboard input
    # user_input = input(">> ")

    # if user_input == 'exit':
    #     ser.close()
    #     break
    # else:
        # Send the character to the device
        # (Note: I've added a carriage return and line feed to the characters as requested by my device)
    
    user_input = 'Aloo'
    ser.write(user_input + '\r\n')

    # Wait for the device to respond
    time.sleep(1)

    # Read the output
    out = ''
    while ser.inWaiting() > 0:
        out += ser.read(1)

    if out:
        print(">> " + out)
