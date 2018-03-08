import serial
import os
import argparse
from subprocess import Popen

choice = 0
parser = argparse.ArgumentParser()
parser.add_argument("--port", help="arduino port ttyACM#")
args = parser.parse_args()

# You need to specify the USB port used by the Arduino
if args.port:
    choice = args.port

p = 'COM' + str(choice)

# Connects to serial port of Arduino
ser = serial.Serial(
    port=p, \
    baudrate=9600, \
    parity=serial.PARITY_NONE, \
    stopbits=serial.STOPBITS_ONE, \
    bytesize=serial.EIGHTBITS, \
    timeout=0
)

print("connected to:" + ser.portstr)

# Counter
count = 1

# Current device
device = 0

# Change this to true if you want to control all of your lights at once
every = False

# Enter your deviceIds in the array below
devices = [""]

# Enter you account token below here
token = ""

# Saves the state of the device
switch = []
for i in devices:
    switch.append(0)

# Sends the request to the smart plug
def tlp(choice, device_choice):
    curl = """curl -s --request POST "https://wap.tplinkcloud.com/?token="""
    curl += token
    curl += """ HTTP/1.1" \\\
--data '{"method":"passthrough", "params": {"deviceId": \""""
    curl += devices[int(device_choice)]
    curl += """\", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":"""
    curl += str(choice)
    curl += """}}}" }}' \\\
--header "Content-Type: application/json" \\\
%s > /dev/null """
    print(curl)
    os.system(curl)

while True:

    # Reads from Serial
    line = ser.readline()
    if line != '':
	
	# Outputs commands (what has been received)
        print(str(count) + str(': ') + line)

	# Changes the status of the current device
        if line == "1" and not every:
            switch[device] = 1 - switch[device]
            tlp(str(switch[device]), str(device))

	# Changes the status of every devices
        elif line == "1" and every:
	    for i in range(len(switch)):
		switch[i] = 1 - switch[i]

	    for i in range(len(switch)):
		tlp(switch[i], i) 
        
	# Detects which direction you are going with the joystick, 
	# and changes the device accordingly     
        if line == "2":
	    device = 1 + device
	elif line == "3":
            device = 1 - device
            
	count += 1

ser.close()
