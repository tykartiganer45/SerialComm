import time
import serial
import struct
import binascii
import os

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
   port='/dev/ttyUSB0',
   baudrate=19200,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS
)


#print("SERIAL PORT OPEN? " + str(ser.isOpen()))



#-------------------------------------------------------------------
#-------------------------PAN COMMANDS------------------------------
#-------------------------------------------------------------------
#Function to step move pan left at specified speed
def steppanleft(speed):
    if speed > 0 and speed <= 60:
	#Converting Speed to Hex Value
	speed = speed + 2
	hex_speed = hex(speed)
	print("PAN SPEED IN HEX FORMAT: " + hex_speed)
	str_speed = str(hex_speed)
	#Reformatting Hex value to have 2 digits
	if len(str_speed[2:]) == 1:  
	   final = '0' + str_speed[2:]
	elif len(str_speed[2:]) == 2:
	   final = str_speed[2:]
	else:
	   raise Exception('Not valid speed input')
	print("REFORMATTED HEX SPEED: " + final)
	#Combining all pieces to make Pelco D command "04" represents "Pan Left"
	start = "FF"
	data = "010004"+ final + "00"
	print("PELCO-D COMMAND W/O CHECKSUM: " + data)
	data = binascii.unhexlify(data)
	print repr(data)
	#Calculating Checksum value and converting to hex value
	checksum = sum(map(ord, data))
	hex_checksum = hex(checksum)
	str_checksum = str(hex_checksum)
	#Reformatting checksum to have 2 digits
	if len(str_checksum[2:]) == 1:  
	   checksum_final = '0' + str_checksum[2:]
	else:
	   checksum_final = str_checksum[2:]
	print("CHECKSUM HEX VALUE: " + checksum_final)
	#Combining all pieces to create the full Pelco D command and running it
	start_pan_left = start + binascii.hexlify(data) + checksum_final
	print("FULL PELCO-D COMMAND: " + start_pan_left) 
	print repr(binascii.unhexlify(start_pan_left))
	ser.write(start_pan_left.decode("hex"))
	#Stopping the pan action to make it just do a step
	time.sleep(1.5)
	stop()
	stop()
	print("STEP PAN LEFT DONE")
    else:
        raise Exception('Not valid degree input') 

#Function to pan left at specified speed and duration
def continuouspanleft(speed, duration):
    if speed > 0 and speed <= 60 and duration > 0:
	#Converting Speed to Hex Value
	speed = speed + 2
	hex_speed = hex(speed)
	print("PAN SPEED IN HEX FORMAT: " + hex_speed)
	str_speed = str(hex_speed)
	#Reformatting Hex value to have 2 digits
	if len(str_speed[2:]) == 1:  
	   final = '0' + str_speed[2:]
	elif len(str_speed[2:]) == 2:
	   final = str_speed[2:]
	else:
	   raise Exception('Not valid speed input')
	print("REFORMATTED HEX SPEED: " + final)
	#Combining all pieces to make Pelco D command "04" represents "Pan Left"
	start = "FF"
	data = "010004"+ final + "00"
	print("PELCO-D COMMAND W/O CHECKSUM: " + data)
	data = binascii.unhexlify(data)
	print repr(data)
	#Calculating Checksum value and converting to hex value
	checksum = sum(map(ord, data))
	hex_checksum = hex(checksum)
	str_checksum = str(hex_checksum)
	#Reformatting checksum to have 2 digits
	if len(str_checksum[2:]) == 1:  
	   checksum_final = '0' + str_checksum[2:]
	else:
	   checksum_final = str_checksum[2:]
	print("CHECKSUM HEX VALUE: " + checksum_final)
	#Combining all pieces to create the full Pelco D command and running it
	start_pan_left = start + binascii.hexlify(data) + checksum_final
	print("FULL PELCO-D COMMAND: " + start_pan_left) 
	print repr(binascii.unhexlify(start_pan_left))
	ser.write(start_pan_left.decode("hex"))
	print("PANNING LEFT for " + str(duration) + " seconds")
	time.sleep(duration)
	stop()
	stop()
	print("PANNING LEFT DONE")
    else:
        raise Exception('Not valid degree input') 

#Function to pan right at specified speed and duration
def continuouspanright(speed, duration):
    if speed > 0 and speed <= 60 and duration > 0:
	#Converting Speed to Hex Value
	speed = speed + 2
	hex_speed = hex(speed)
	print("PAN SPEED IN HEX FORMAT: " + hex_speed)
	str_speed = str(hex_speed)
	#Reformatting Hex value to have 2 digits
	if len(str_speed[2:]) == 1:  
	   final = '0' + str_speed[2:]
	elif len(str_speed[2:]) == 2:
	   final = str_speed[2:]
	else:
	   raise Exception('Not valid speed input')
	print("REFORMATTED HEX SPEED: " + final)
	#Combining all pieces to make Pelco D command "02" represents "Pan Right"
	start = "FF"
	data = "010002"+ final + "00"
	print("PELCO-D COMMAND W/O CHECKSUM: " + data)
	data = binascii.unhexlify(data)
	print repr(data)
	#Calculating Checksum value and converting to hex value
	checksum = sum(map(ord, data))
	hex_checksum = hex(checksum)
	str_checksum = str(hex_checksum)
	#Reformatting checksum to have 2 digits
	if len(str_checksum[2:]) == 1:  
	   checksum_final = '0' + str_checksum[2:]
	else:
	   checksum_final = str_checksum[2:]
	print("CHECKSUM HEX VALUE: " + checksum_final)
	#Combining all pieces to create the full Pelco D command and running it
	start_pan_right = start + binascii.hexlify(data) + checksum_final
	print("FULL PELCO-D COMMAND:: " + start_pan_right) 
	print repr(binascii.unhexlify(start_pan_right))
	ser.write(start_pan_right.decode("hex"))
	print("PANNING RIGHT for " + str(duration) + " seconds")
	time.sleep(duration)
	stop()
	stop()
	print("PANNING RIGHT DONE")
    else:
        raise Exception('Not valid degree input') 

#Function to step move pan right at specified speed
def steppanright(speed):
    if speed > 0 and speed <= 60:
	#Converting Speed to Hex Value
	speed = speed + 2
	hex_speed = hex(speed)
	print("PAN SPEED IN HEX FORMAT: " + hex_speed)
	str_speed = str(hex_speed)
	#Reformatting Hex value to have 2 digits
	if len(str_speed[2:]) == 1:  
	   final = '0' + str_speed[2:]
	elif len(str_speed[2:]) == 2:
	   final = str_speed[2:]
	else:
	   raise Exception('Not valid speed input')
	print("REFORMATTED HEX SPEED: " + final)
	#Combining all pieces to make Pelco D command "02" represents "Pan Right"
	start = "FF"
	data = "010002"+ final + "00"
	print("PELCO-D COMMAND W/O CHECKSUM: " + data)
	data = binascii.unhexlify(data)
	print repr(data)
	#Calculating Checksum value and converting to hex value
	checksum = sum(map(ord, data))
	hex_checksum = hex(checksum)
	str_checksum = str(hex_checksum)
	#Reformatting checksum to have 2 digits
	if len(str_checksum[2:]) == 1:  
	   checksum_final = '0' + str_checksum[2:]
	else:
	   checksum_final = str_checksum[2:]
	print("CHECKSUM HEX VALUE: " + checksum_final)
	#Combining all pieces to create the full Pelco D command and running it
	start_pan_right = start + binascii.hexlify(data) + checksum_final
	print("FULL PELCO-D COMMAND: " + start_pan_right) 
	print repr(binascii.unhexlify(start_pan_right))
	ser.write(start_pan_right.decode("hex"))
	#Stopping the pan action to make it just do a step
	time.sleep(1.5)
	stop()
	stop()
	print("STEP PAN RIGHT DONE")
    else:
        raise Exception('Not valid degree input') 



#-------------------------------------------------------------------
#-------------------------TILT COMMANDS-----------------------------
#-------------------------------------------------------------------
#Function to step move tilt up at specified speed
def steptiltup(speed):
    if speed > 0 and speed <= 60:
	#Converting Speed to Hex Value
	speed = speed + 2
	hex_speed = hex(speed)
	print("TILT SPEED IN HEX FORMAT: " + hex_speed)
	str_speed = str(hex_speed)
	#Reformatting Hex value to have 2 digits
	if len(str_speed[2:]) == 1:  
	   final = '0' + str_speed[2:]
	elif len(str_speed[2:]) == 2:
	   final = str_speed[2:]
	else:
	   raise Exception('Not valid speed input')
	print("REFORMATTED HEX SPEED: " + final)
	#Combining all pieces to make Pelco D command "08" represents "Tilt Up"
	start = "FF"
	data = "01000800" + final
	print("PELCO-D COMMAND W/O CHECKSUM: " + data)
	data = binascii.unhexlify(data)
	print repr(data)
	#Calculating Checksum value and converting to hex value
	checksum = sum(map(ord, data))
	hex_checksum = hex(checksum)
	str_checksum = str(hex_checksum)
	#Reformatting checksum to have 2 digits
	if len(str_checksum[2:]) == 1:  
	   checksum_final = '0' + str_checksum[2:]
	else:
	   checksum_final = str_checksum[2:]
	print("CHECKSUM HEX VALUE: " + checksum_final)
	#Combining all pieces to create the full Pelco D command and running it
	start_tilt_up = start + binascii.hexlify(data) + checksum_final
	print("FULL PELCO-D COMMAND: " + start_tilt_up) 
	print repr(binascii.unhexlify(start_tilt_up))
	ser.write(start_tilt_up.decode("hex"))
	#Stopping the tilt action to make it just do a step
	time.sleep(1.5)
	stop()
	stop()
	print("STEP TILT UP DONE")
    else:
        raise Exception('Not valid degree input')

#Function to step move tilt up at specified speed
def continuoustiltup(speed, duration):
    if speed > 0 and speed <= 60 and duration > 0:
	#Converting Speed to Hex Value
	speed = speed + 2
	hex_speed = hex(speed)
	print("TILT SPEED IN HEX FORMAT: " + hex_speed)
	str_speed = str(hex_speed)
	#Reformatting Hex value to have 2 digits
	if len(str_speed[2:]) == 1:  
	   final = '0' + str_speed[2:]
	elif len(str_speed[2:]) == 2:
	   final = str_speed[2:]
	else:
	   raise Exception('Not valid speed input')
	print("REFORMATTED HEX SPEED: " + final)
	#Combining all pieces to make Pelco D command "08" represents "Tilt Up"
	start = "FF"
	data = "01000800" + final
	print("PELCO-D COMMAND W/O CHECKSUM: " + data)
	data = binascii.unhexlify(data)
	print repr(data)
	#Calculating Checksum value and converting to hex value
	checksum = sum(map(ord, data))
	hex_checksum = hex(checksum)
	str_checksum = str(hex_checksum)
	#Reformatting checksum to have 2 digits
	if len(str_checksum[2:]) == 1:  
	   checksum_final = '0' + str_checksum[2:]
	else:
	   checksum_final = str_checksum[2:]
	print("CHECKSUM HEX VALUE: " + checksum_final)
	#Combining all pieces to create the full Pelco D command and running it
	start_tilt_up = start + binascii.hexlify(data) + checksum_final
	print("FULL PELCO-D COMMAND: " + start_tilt_up) 
	print repr(binascii.unhexlify(start_tilt_up))
	ser.write(start_tilt_up.decode("hex"))
	print("TILTING UP for " + str(duration) + " seconds")
	time.sleep(duration)
	stop()
	stop()
	print("TILT UP DONE")
    else:
        raise Exception('Not valid degree input')
	

#Function to step move tilt down at specified speed
def steptiltdown(speed):
    if speed > 0 and speed <= 60:
	#Converting Speed to Hex Value
	speed = speed + 2
	hex_speed = hex(speed)
	print("TILT SPEED IN HEX FORMAT: " + hex_speed)
	str_speed = str(hex_speed)
	#Reformatting Hex value to have 2 digits
	if len(str_speed[2:]) == 1:  
	   final = '0' + str_speed[2:]
	elif len(str_speed[2:]) == 2:
	   final = str_speed[2:]
	else:
	   raise Exception('Not valid speed input')
	print("REFORMATTED HEX SPEED: " + final)
	#Combining all pieces to make Pelco D command "10" represents "Tilt Up"
	start = "FF"
	data = "01001000" + final
	print("PELCO-D COMMAND W/O CHECKSUM: " + data)
	data = binascii.unhexlify(data)
	print repr(data)
	#Calculating Checksum value and converting to hex value
	checksum = sum(map(ord, data))
	hex_checksum = hex(checksum)
	str_checksum = str(hex_checksum)
	#Reformatting checksum to have 2 digits
	if len(str_checksum[2:]) == 1:  
	   checksum_final = '0' + str_checksum[2:]
	else:
	   checksum_final = str_checksum[2:]
	print("CHECKSUM HEX VALUE: " + checksum_final)
	#Combining all pieces to create the full Pelco D command and running it
	start_tilt_down = start + binascii.hexlify(data) + checksum_final
	print("FULL PELCO-D COMMAND: " + start_tilt_down) 
	print repr(binascii.unhexlify(start_tilt_down))
	ser.write(start_tilt_down.decode("hex"))
	#Stopping the tilt action to make it just do a step
	time.sleep(1.5)
	stop()
	stop()
	print("STEP TILT DOWN DONE")
    else:
        raise Exception('Not valid degree input')

#Function to tilt down at specified speed for specified duration
def continuoustiltdown(speed, duration):
    if speed > 0 and speed <= 60 and duration > 0:
	#Converting Speed to Hex Value
	speed = speed + 2
	hex_speed = hex(speed)
	print("TILT SPEED IN HEX FORMAT: " + hex_speed)
	str_speed = str(hex_speed)
	#Reformatting Hex value to have 2 digits
	if len(str_speed[2:]) == 1:  
	   final = '0' + str_speed[2:]
	elif len(str_speed[2:]) == 2:
	   final = str_speed[2:]
	else:
	   raise Exception('Not valid speed input')
	print("REFORMATTED HEX SPEED: " + final)
	#Combining all pieces to make Pelco D command "10" represents "Tilt Up"
	start = "FF"
	data = "01001000" + final
	print("PELCO-D COMMAND W/O CHECKSUM: " + data)
	data = binascii.unhexlify(data)
	print repr(data)
	#Calculating Checksum value and converting to hex value
	checksum = sum(map(ord, data))


	hex_checksum = hex(checksum)
	str_checksum = str(hex_checksum)
	#Reformatting checksum to have 2 digits
	if len(str_checksum[2:]) == 1:  
	   checksum_final = '0' + str_checksum[2:]
	else:
	   checksum_final = str_checksum[2:]
	print("CHECKSUM HEX VALUE: " + checksum_final)
	#Combining all pieces to create the full Pelco D command and running it
	start_tilt_down = start + binascii.hexlify(data) + checksum_final
	print("FULL PELCO-D COMMAND: " + start_tilt_down) 
	print repr(binascii.unhexlify(start_tilt_down))
	ser.write(start_tilt_down.decode("hex"))
	print("TILTING DOWN for " + str(duration) + " seconds")
	time.sleep(duration)
	stop()
	stop()
	print("TILTING DOWN DONE")
    else:
        raise Exception('Not valid degree input')



#-------------------------------------------------------------------
#-------------------------PAN & TILT COMMANDS-----------------------
#-------------------------------------------------------------------
#Function to pan left & tilt up at specified speed for specified duration
def continuousupleft(pan_speed,tilt_speed, duration):
    if pan_speed > 0 and pan_speed <= 60 and tilt_speed > 0 and tilt_speed <=60 and duration > 0:
	#Converting Speed to Hex Value
	pan_speed = pan_speed + 2
	tilt_speed = tilt_speed + 2
	hex_pan_speed = hex(pan_speed)
	hex_tilt_speed = hex(tilt_speed)
	print("PAN SPEED IN HEX FORMAT: " + hex_pan_speed)
	print("TILT SPEED IN HEX FORMAT: " + hex_tilt_speed)
	str_pan_speed = str(hex_pan_speed)
	str_tilt_speed = str(hex_tilt_speed)
	#Reformatting Hex value to have 2 digits
	if len(str_pan_speed[2:]) == 1:  
	   final_pan = '0' + str_pan_speed[2:]
	elif len(str_pan_speed[2:]) == 2:
	   final_pan = str_pan_speed[2:]
	else:
	   raise Exception('Not valid speed input')
	if len(str_tilt_speed[2:]) == 1:  
	   final_tilt = '0' + str_tilt_speed[2:]
	elif len(str_pan_speed[2:]) == 2:
	   final_tilt = str_tilt_speed[2:]
	else:
	   raise Exception('Not valid speed input')
	print("REFORMATTED HEX PAN SPEED: " + final_pan)
	print("REFORMATTED HEX TILT SPEED: " + final_tilt)
	#Combining all pieces to make Pelco D command "0C" represents "Pan Left & Tilt Up"
	start = "FF"
	data = "01000C" + final_pan + final_tilt
	print("PELCO-D COMMAND W/O CHECKSUM: " + data)
	data = binascii.unhexlify(data)
	print repr(data)
	#Calculating Checksum value and converting to hex value
	checksum = sum(map(ord, data))
	hex_checksum = hex(checksum)
	str_checksum = str(hex_checksum)
	#Reformatting checksum to have 2 digits
	if len(str_checksum[2:]) == 1:  
	   checksum_final = '0' + str_checksum[2:]
	else:
	   checksum_final = str_checksum[2:]
	print("CHECKSUM HEX VALUE: " + checksum_final)
	#Combining all pieces to create the full Pelco D command and running it
	start_upleft = start + binascii.hexlify(data) + checksum_final
	print("FULL PELCO-D COMMAND: " + start_upleft) 
	print repr(binascii.unhexlify(start_upleft))
	ser.write(start_upleft.decode("hex"))
	print("PANNING LEFT & TILTING UP for " + str(duration) + " seconds")
	time.sleep(duration)
	stop()
	stop()
	print("PANNING LEFT & TILTING UP DONE")
    else:
        raise Exception('Not valid degree input')

#Function to pan right & tilt up at specified speed for specified duration
def continuousupright(pan_speed,tilt_speed, duration):
    if pan_speed > 0 and pan_speed <= 60 and tilt_speed > 0 and tilt_speed <=60 and duration > 0:
	#Converting Speed to Hex Value
	pan_speed = pan_speed + 2
	tilt_speed = tilt_speed + 2
	hex_pan_speed = hex(pan_speed)
	hex_tilt_speed = hex(tilt_speed)
	print("PAN SPEED IN HEX FORMAT: " + hex_pan_speed)
	print("TILT SPEED IN HEX FORMAT: " + hex_tilt_speed)
	str_pan_speed = str(hex_pan_speed)
	str_tilt_speed = str(hex_tilt_speed)
	#Reformatting Hex value to have 2 digits
	if len(str_pan_speed[2:]) == 1:  
	   final_pan = '0' + str_pan_speed[2:]
	elif len(str_pan_speed[2:]) == 2:
	   final_pan = str_pan_speed[2:]
	else:
	   raise Exception('Not valid speed input')
	if len(str_tilt_speed[2:]) == 1:  
	   final_tilt = '0' + str_tilt_speed[2:]
	elif len(str_pan_speed[2:]) == 2:
	   final_tilt = str_tilt_speed[2:]
	else:
	   raise Exception('Not valid speed input')
	print("REFORMATTED HEX PAN SPEED: " + final_pan)
	print("REFORMATTED HEX TILT SPEED: " + final_tilt)
	#Combining all pieces to make Pelco D command "0A" represents "Pan Right & Tilt Up"
	start = "FF"
	data = "01000A" + final_pan + final_tilt
	print("PELCO-D COMMAND W/O CHECKSUM: " + data)
	data = binascii.unhexlify(data)
	print repr(data)
	#Calculating Checksum value and converting to hex value
	checksum = sum(map(ord, data))
	hex_checksum = hex(checksum)
	str_checksum = str(hex_checksum)
	#Reformatting checksum to have 2 digits
	if len(str_checksum[2:]) == 1:  
	   checksum_final = '0' + str_checksum[2:]
	else:
	   checksum_final = str_checksum[2:]
	print("CHECKSUM HEX VALUE: " + checksum_final)
	#Combining all pieces to create the full Pelco D command and running it
	start_upright = start + binascii.hexlify(data) + checksum_final
	print("FULL PELCO-D COMMAND: " + start_upright) 
	print repr(binascii.unhexlify(start_upright))
	ser.write(start_upright.decode("hex"))
	print("PANNING RIGHT & TILTING UP for " + str(duration) + " seconds")
	time.sleep(duration)
	stop()
	stop()
	print("PANNING RIGHT & TILTING UP DONE")
    else:
        raise Exception('Not valid degree input')

#Function to pan left & tilt down at specified speed for specified duration
def continuousdownleft(pan_speed,tilt_speed, duration):
    if pan_speed > 0 and pan_speed <= 60 and tilt_speed > 0 and tilt_speed <=60 and duration > 0:
	#Converting Speed to Hex Value
	pan_speed = pan_speed + 2
	tilt_speed = tilt_speed + 2
	hex_pan_speed = hex(pan_speed)
	hex_tilt_speed = hex(tilt_speed)
	print("PAN SPEED IN HEX FORMAT: " + hex_pan_speed)
	print("TILT SPEED IN HEX FORMAT: " + hex_tilt_speed)
	str_pan_speed = str(hex_pan_speed)
	str_tilt_speed = str(hex_tilt_speed)
	#Reformatting Hex value to have 2 digits
	if len(str_pan_speed[2:]) == 1:  
	   final_pan = '0' + str_pan_speed[2:]
	elif len(str_pan_speed[2:]) == 2:
	   final_pan = str_pan_speed[2:]
	else:
	   raise Exception('Not valid speed input')
	if len(str_tilt_speed[2:]) == 1:  
	   final_tilt = '0' + str_tilt_speed[2:]
	elif len(str_pan_speed[2:]) == 2:
	   final_tilt = str_tilt_speed[2:]
	else:
	   raise Exception('Not valid speed input')
	print("REFORMATTED HEX PAN SPEED: " + final_pan)
	print("REFORMATTED HEX TILT SPEED: " + final_tilt)
	#Combining all pieces to make Pelco D command "14" represents "Pan Left & Tilt Down"
	start = "FF"
	data = "010014" + final_pan + final_tilt
	print("PELCO-D COMMAND W/O CHECKSUM: " + data)
	data = binascii.unhexlify(data)
	print repr(data)
	#Calculating Checksum value and converting to hex value
	checksum = sum(map(ord, data))
	hex_checksum = hex(checksum)
	str_checksum = str(hex_checksum)
	#Reformatting checksum to have 2 digits
	if len(str_checksum[2:]) == 1:  
	   checksum_final = '0' + str_checksum[2:]
	else:
	   checksum_final = str_checksum[2:]
	print("CHECKSUM HEX VALUE: " + checksum_final)
	#Combining all pieces to create the full Pelco D command and running it
	start_downleft = start + binascii.hexlify(data) + checksum_final
	print("FULL PELCO-D COMMAND: " + start_downleft) 
	print repr(binascii.unhexlify(start_downleft))
	ser.write(start_downleft.decode("hex"))
	print("PANNING LEFT & TILTING DOWN for " + str(duration) + " seconds")
	time.sleep(duration)
	stop()
	stop()
	print("PANNING LEFT & TILTING DOWN DONE")
    else:
        raise Exception('Not valid degree input')

#Function to pan right & tilt down at specified speed for specified duration
def continuousdownright(pan_speed,tilt_speed, duration):
    if pan_speed > 0 and pan_speed <= 60 and tilt_speed > 0 and tilt_speed <=60 and duration > 0:
	#Converting Speed to Hex Value
	pan_speed = pan_speed + 2
	tilt_speed = tilt_speed + 2
	hex_pan_speed = hex(pan_speed)
	hex_tilt_speed = hex(tilt_speed)
	print("PAN SPEED IN HEX FORMAT: " + hex_pan_speed)
	print("TILT SPEED IN HEX FORMAT: " + hex_tilt_speed)
	str_pan_speed = str(hex_pan_speed)
	str_tilt_speed = str(hex_tilt_speed)
	#Reformatting Hex value to have 2 digits
	if len(str_pan_speed[2:]) == 1:  
	   final_pan = '0' + str_pan_speed[2:]
	elif len(str_pan_speed[2:]) == 2:
	   final_pan = str_pan_speed[2:]
	else:
	   raise Exception('Not valid speed input')
	if len(str_tilt_speed[2:]) == 1:  
	   final_tilt = '0' + str_tilt_speed[2:]
	elif len(str_pan_speed[2:]) == 2:
	   final_tilt = str_tilt_speed[2:]
	else:
	   raise Exception('Not valid speed input')
	print("REFORMATTED HEX PAN SPEED: " + final_pan)
	print("REFORMATTED HEX TILT SPEED: " + final_tilt)
	#Combining all pieces to make Pelco D command "12" represents "Pan Right & Tilt Down"
	start = "FF"
	data = "010012" + final_pan + final_tilt
	print("PELCO-D COMMAND W/O CHECKSUM: " + data)
	data = binascii.unhexlify(data)
	print repr(data)
	#Calculating Checksum value and converting to hex value
	checksum = sum(map(ord, data))
	hex_checksum = hex(checksum)
	str_checksum = str(hex_checksum)
	#Reformatting checksum to have 2 digits
	if len(str_checksum[2:]) == 1:  
	   checksum_final = '0' + str_checksum[2:]
	else:
	   checksum_final = str_checksum[2:]
	print("CHECKSUM HEX VALUE: " + checksum_final)
	#Combining all pieces to create the full Pelco D command and running it
	start_downright = start + binascii.hexlify(data) + checksum_final
	print("FULL PELCO-D COMMAND: " + start_downright) 
	print repr(binascii.unhexlify(start_downright))
	ser.write(start_downright.decode("hex"))
	print("PANNING RIGHT & TILTING DOWN for " + str(duration) + " seconds")
	time.sleep(duration)
	stop()
	stop()
	print("PANNING RIGHT & TILTING DOWN DONE")
    else:
        raise Exception('Not valid degree input')

#-------------------------------------------------------------------
#-------------------------PRESET COMMANDS---------------------------
#-------------------------------------------------------------------
#Setting Preset Postion
def setpreset(preset):
    if preset >= 0 and preset <= 255:
	#Converting Speed to Hex Value
	hex_preset = hex(preset)
	print("PRESET IN HEX FORMAT: " + hex_preset)
	str_preset = str(hex_preset)
	#Reformatting Hex value to have 2 digits
	if len(str_preset[2:]) == 1:  
	   final = '0' + str_preset[2:]
	elif len(str_preset[2:]) == 2:
	   final = str_preset[2:]
	else:
	   raise Exception('Not valid preset input')
	print("REFORMATTED HEX PRESET: " + final)
        #Combining all pieces to make Pelco D command "03" represents "Set Preset"
	start = "FF"
	data = "01000300" + final
	print("PELCO-D COMMAND W/O CHECKSUM: " + data)
	data = binascii.unhexlify(data)
	print repr(data)
	#Calculating Checksum value and converting to hex value
	checksum = sum(map(ord, data))
	hex_checksum = hex(checksum)
	str_checksum = str(hex_checksum)
	#Reformatting checksum to have 2 digits
	if len(str_checksum[2:]) == 1:  
	   checksum_final = '0' + str_checksum[2:]
	else:
	   checksum_final = str_checksum[2:]
	print("CHECKSUM HEX VALUE: " + checksum_final)
	#Combining all pieces to create the full Pelco D command and running it
	start_setpreset = start + binascii.hexlify(data) + checksum_final
	print("FULL PELCO-D COMMAND: " + start_setpreset) 
	print repr(binascii.unhexlify(start_setpreset))
	ser.write(start_setpreset.decode("hex"))
    else:
        raise Exception('Not valid preset input')

#Call Preset Position	
def callpreset(preset):
    if preset >= 0 and preset <= 255:
	#Converting Speed to Hex Value
	hex_preset = hex(preset)
	print("PRESET IN HEX FORMAT: " + hex_preset)
	str_preset = str(hex_preset)
	#Reformatting Hex value to have 2 digits
	if len(str_preset[2:]) == 1:  
	   final = '0' + str_preset[2:]
	elif len(str_preset[2:]) == 2:
	   final = str_preset[2:]
	else:
	   raise Exception('Not valid preset input')
	print("REFORMATTED HEX PRESET: " + final)
        #Combining all pieces to make Pelco D command "07" represents "Call Preset"
	start = "FF"
	data = "01000700" + final
	print("PELCO-D COMMAND W/O CHECKSUM: " + data)
	data = binascii.unhexlify(data)
	print repr(data)
	#Calculating Checksum value and converting to hex value
	checksum = sum(map(ord, data))
	hex_checksum = hex(checksum)
	str_checksum = str(hex_checksum)
	#Reformatting checksum to have 2 digits
	if len(str_checksum[2:]) == 1:  
	   checksum_final = '0' + str_checksum[2:]
	else:
	   checksum_final = str_checksum[2:]
	print("CHECKSUM HEX VALUE: " + checksum_final)
	#Combining all pieces to create the full Pelco D command and running it
	start_callpreset = start + binascii.hexlify(data) + checksum_final
	print("FULL PELCO-D COMMAND: " + start_callpreset) 
	print repr(binascii.unhexlify(start_callpreset))
	ser.write(start_callpreset.decode("hex"))
	pre = str(preset)
	print("PRESET #: " + pre)
    else:
        raise Exception('Not valid preset input')

#Clear Preset Position	
def clearpreset(preset):
    if preset >= 0 and preset <= 255:
	#Converting Speed to Hex Value
	hex_preset = hex(preset)
	print("PRESET IN HEX FORMAT: " + hex_preset)
	str_preset = str(hex_preset)
	#Reformatting Hex value to have 2 digits
	if len(str_preset[2:]) == 1:  
	   final = '0' + str_preset[2:]
	elif len(str_preset[2:]) == 2:
	   final = str_preset[2:]
	else:
	   raise Exception('Not valid preset input')
	print("REFORMATTED HEX PRESET: " + final)
        #Combining all pieces to make Pelco D command "05" represents "Clear Preset"
	start = "FF"
	data = "01000500" + final
	print("PELCO-D COMMAND W/O CHECKSUM: " + data)
	data = binascii.unhexlify(data)
	print repr(data)
	#Calculating Checksum value and converting to hex value
	checksum = sum(map(ord, data))
	hex_checksum = hex(checksum)
	str_checksum = str(hex_checksum)
	#Reformatting checksum to have 2 digits
	if len(str_checksum[2:]) == 1:  
	   checksum_final = '0' + str_checksum[2:]
	else:
	   checksum_final = str_checksum[2:]
	print("CHECKSUM HEX VALUE: " + checksum_final)
	#Combining all pieces to create the full Pelco D command and running it
	start_clearpreset = start + binascii.hexlify(data) + checksum_final
	print("FULL PELCO-D COMMAND: " + start_clearpreset) 
	print repr(binascii.unhexlify(start_clearpreset))
	ser.write(start_clearpreset.decode("hex"))
    else:
        raise Exception('Not valid preset input')

#TestCommands
def test():
    stop = "FF01000700333b"
    print repr(binascii.unhexlify(stop))
    ser.write(stop.decode("hex"))
#Stop Movement Function
def stop():
    stop = "FF010000000001"
    print repr(binascii.unhexlify(stop))
    ser.write(stop.decode("hex"))
def sclose():
    ser.close()
def sopen():
    ser.open()


#clearpreset(73)
#time.sleep(4.0)
#setpreset(73)
#time.sleep(4.0)
#steppanright(7)
#callpreset(72)
#time.sleep(4.0)
#callpreset(70)
#steptiltdown(5)
#time.sleep(10.0)
#callpreset(63)
#ser.close()
#time.sleep(5.0)
#ser.open()
#callpreset(63)
#ser.close()
#time.sleep(5.0)
#ser.open()
#callpreset(61)
#ser.close()
#time.sleep(5.0)
#callpreset(60)
#ser.close()
#time.sleep(5.0)
#ser.open()
#os.system("ffmpeg -y -i rtsp://admin:laddyp4d@192.168.1.110/live -vframes 1 TestImages/P4/Position4_Pattern1.jpg &")
#time.sleep(2.0)
#os.system('ffmpeg -i TestImages/P4/Position4_Pattern1.jpg -vf "crop=1080:770:1785:795" TestImages/P4/Cropped/Zep_Pattern1.jpg &')
#time.sleep(1.0)
#steppanright(15)
#callpreset(63)
#continuouspanright(30,2)
#time.sleep(4.0)
#continuouspanleft(15,10)
#time.sleep(4)
#continuoustiltup(15,5)
#time.sleep(4.0)
#test()
#continuoustiltdown(30,10)
#time.sleep(4)
#continuousupright(15,15,3)
#time.sleep(4)
#continuousdownleft(30,30,7)
#time.sleep(4)
#continuousupleft(15,15,6)
#time.sleep(4)
#continuousdownright(15,15,3)
#test()
#time.sleep(4.0)
#stop()

#ser.close()

	
