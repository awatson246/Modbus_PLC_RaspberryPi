import time
from pycomm3 import LogixDriver
first_plc = LogixDriver('192.198.___.___') 
first_plc.open()

state = 0

while True: 
	with LogixDriver('192.168.___.___') as micro850:
		print(micro850)
		
		# System off condition
		while state == 0:
			print(state)
			
			taglist = micro850.read('_IO_EM_DI_01')
			green = taglist[1]
			taglist = micro850.read('_IO_EM_DI_00')
			red = taglist[1]
			
			micro850.write('_IO_EM_DO_07', green)
			micro850.write('IO_EM_DO_06', red)
			
			time.sleep(0.1)
			
			if green:
				# Move to system on
				state = 1
				while green:
					taglist = micro850.read('_IO_EM_DI_01')
					freen = taglist[1]
					
		# System on condition
		while state == 1:
			print(state)
			
			taglist = micro850.read('_IO_EM_DI_01')
			green = taglist[1]
			taglist = micro850.read('_IO_EM_DI_00')
			red = taglist[1]
			
			micro850.write('_IO_EM_DO_07', green)
			micro850.write('IO_EM_DO_06', red)
			
			time.sleep(0.1)
			
			
			if green:
				# Move to system off
				state = 0
				while green:
					taglist = micro850.read('_IO_EM_DI_01')
					freen = taglist[1]