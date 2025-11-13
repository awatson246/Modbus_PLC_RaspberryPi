# Inputs connected to addresses 000001 and 000002
# Outputs connected to addresses 000011, 000012, and 000013

from pymodbus.client import ModbusTcpClient
import time

# Create the Modbus TCP client, put your own IP here
client = ModbusTcpClient('192.169.___.___')

# Connect to the Modbus TCP server
client.connect()

while True: 
	# Read switches of address, number of bits
	response = client.read_coils(address=0,count2)
	if not response.isError():
		switch1 = response.bits[0]
		switch2 = response.bits[1]
	else:
		print("Error reading registers:", response)
		continue
	
	# Write switch states into corresponding lights
	response = client.write_coil(11, switch1)
	response2 = client.write_coil(10, switch2)
	
	print("Writing complete")
	
	if not response.isError():
		print("Write succesful", response)
	else: 
		print("Error writing registers:", response)
	
	if not response2.isError():
		print("Write succesful", response2)
	else: 
		print("Error writing registers:", response2)
		
# Close the connection
client.close
