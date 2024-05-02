import time
import serial

# Configure the serial connection (parameters may differ based on your device)
ser = serial.Serial(
    port='/dev/ttyS0',  # Specify the serial port (e.g., '/dev/ttyUSB1')
    baudrate=115200,        # Set the baud rate
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

ser.isOpen()
print("|>> " + ser.port + " port opened successfully ..")
print("|>> Application started ..")

while True:
   
    user_input = "Aloo" + '\r\n'
    ser.write(user_input.encode())

    # Wait for the device to respond
    time.sleep(1)

    # Read the output
    out = ''
    while ser.inWaiting() > 0:
        out += ser.read(1).decode()

    if out:
        print(">> " + out)
