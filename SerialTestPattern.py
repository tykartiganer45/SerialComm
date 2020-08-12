import time
import serial
import os
from SerialCommWrite import callpreset, sclose, sopen

#ser = serial.Serial(
#    port='/dev/ttyUSB0',
#    baudrate=19200,
#    parity=serial.PARITY_NONE,
#    stopbits=serial.STOPBITS_ONE,
#    bytesize=serial.EIGHTBITS
#)
#os.system("ffmpeg -i rtsp://admin:laddyp4d@192.168.1.114/live -acodec copy -vcodec copy -t 90 TestImages/FullRecord.ts &")
#sleep(5.0)
i = 1
while i <= 3:
      if i == 1:
	  callpreset(52)
	  sclose()
          time.sleep(5.0)
 	  #os.system("ffmpeg -i rtsp://admin:laddyp4d@192.168.1.114/live -acodec copy -vcodec copy -t 90 TestImages/FullRecord.mp4 &")
          sopen()
	  callpreset(70)
          time.sleep(5.0)
          callpreset(70)
          sclose()
	  time.sleep(2.0)
          #ser.open()
	  os.system("ffmpeg -y -i rtsp://admin:laddyp4d@192.168.1.114/live -vframes 1 TestImages/P1/Position1_Pattern" + str(i) + ".jpg &")
	  time.sleep(4.0)


	  sopen()
	  callpreset(71)
          time.sleep(1.0)
          callpreset(71)
	  sclose()
	  time.sleep(2.0)
          #ser.open()
	  os.system("ffmpeg -y -i rtsp://admin:laddyp4d@192.168.1.114/live -vframes 1 TestImages/P2/Position2_Pattern" + str(i) + ".jpg &")
	  time.sleep(4.0)


	  sopen()
	  callpreset(72)
          time.sleep(1.0)
          callpreset(72)
	  sclose()
 	  time.sleep(2.0)
          #ser.open()
	  os.system("ffmpeg -y -i rtsp://admin:laddyp4d@192.168.1.114/live -vframes 1 TestImages/P3/Position3_Pattern" + str(i) + ".jpg &")
	  time.sleep(4.0)

	  sopen()
	  callpreset(73)
          time.sleep(1.0)
          callpreset(73)
	  sclose()
	  time.sleep(2.0)
          #ser.open()
	  os.system("ffmpeg -y -i rtsp://admin:laddyp4d@192.168.1.114/live -vframes 1 TestImages/P4/Position4_Pattern" + str(i) + ".jpg &")
	  time.sleep(4.0)
	  print("PASS: " + str(i))
	  i = i + 1

      elif i == 3:
	  sopen()
	  callpreset(70)
          time.sleep(1.0)
          callpreset(70)
          sclose()
	  time.sleep(2.0)
          #ser.open()
	  os.system("ffmpeg -y -i rtsp://admin:laddyp4d@192.168.1.114/live -vframes 1 TestImages/P1/Position1_Pattern" + str(i) + ".jpg &")
	  time.sleep(4.0)
	  

	  sopen()
	  callpreset(71)
          time.sleep(1.0)
          callpreset(71)
	  sclose()
	  time.sleep(2.0)
          #ser.open()
	  os.system("ffmpeg -y -i rtsp://admin:laddyp4d@192.168.1.114/live -vframes 1 TestImages/P2/Position2_Pattern" + str(i) + ".jpg &")
	  time.sleep(4.0)

	  sopen()
	  callpreset(72)
          time.sleep(1.0)
          callpreset(72)
	  sclose()
 	  time.sleep(2.0)
          #ser.open()
	  os.system("ffmpeg -y -i rtsp://admin:laddyp4d@192.168.1.114/live -vframes 1 TestImages/P3/Position3_Pattern" + str(i) + ".jpg &")
	  time.sleep(4.0)

	  sopen()
	  callpreset(73)
          time.sleep(1.0)
          callpreset(73)
	  sclose()
	  time.sleep(2.0)
          #ser.open()
	  os.system("ffmpeg -y -i rtsp://admin:laddyp4d@192.168.1.114/live -vframes 1 TestImages/P4/Position4_Pattern" + str(i) + ".jpg &")
	  time.sleep(4.0)
	  print("PASS: " + str(i))
	  i = i + 1

	  sopen()
          time.sleep(1.0)
	  callpreset(52)
	  time.sleep
	  sclose()
	  print("PASS: " + str(i))
	  sclose()
	  x = 1
	  while x <= 3:
              os.system("ffmpeg -i TestImages/P1/Position1_Pattern" + str(x) + '.jpg -vf "crop=370:225:1233:855" TestImages/P1/Cropped/Colors_Pattern' + str(x) + ".jpg &")
              os.system("ffmpeg -i TestImages/P2/Position2_Pattern" + str(x) + '.jpg -vf "crop=370:225:850:555" TestImages/P2/Cropped/Colors_Pattern' + str(x) + ".jpg &")
    	      os.system("ffmpeg -i TestImages/P3/Position3_Pattern" + str(x) + '.jpg -vf "crop=370:225:1578:1252" TestImages/P3/Cropped/Colors_Pattern' + str(x) + ".jpg &")
              os.system("ffmpeg -i TestImages/P4/Position4_Pattern" + str(x) + '.jpg -vf "crop=370:225:1070:1059" TestImages/P4/Cropped/Colors_Pattern' + str(x) + ".jpg &")
              x = x + 1
          i = i + 1
          break    
      else:
	  time.sleep(1.0)
	  sopen()
	  callpreset(70)
          time.sleep(1.0)
          callpreset(70)
          sclose()
	  time.sleep(2.0)
          #ser.open()
	  os.system("ffmpeg -y -i rtsp://admin:laddyp4d@192.168.1.114/live -vframes 1 TestImages/P1/Position1_Pattern" + str(i) + ".jpg &")
	  time.sleep(4.0)


	  sopen()
	  callpreset(71)
          time.sleep(1.0)
          callpreset(71)
	  sclose()
	  time.sleep(2.0)
          #ser.open()
	  os.system("ffmpeg -y -i rtsp://admin:laddyp4d@192.168.1.114/live -vframes 1 TestImages/P2/Position2_Pattern" + str(i) + ".jpg &")
	  time.sleep(4.0)

          
	  sopen()
	  callpreset(72)
          time.sleep(1.0)
          callpreset(72)
	  sclose()
 	  time.sleep(2.0)
          #ser.open()
	  os.system("ffmpeg -y -i rtsp://admin:laddyp4d@192.168.1.114/live -vframes 1 TestImages/P3/Position3_Pattern" + str(i) + ".jpg &")
	  time.sleep(4.0)

	  sopen()
	  callpreset(73)
          time.sleep(1.0)
          callpreset(73)
	  sclose()
	  time.sleep(2.0)
          #ser.open()
	  os.system("ffmpeg -y -i rtsp://admin:laddyp4d@192.168.1.114/live -vframes 1 TestImages/P4/Position4_Pattern" + str(i) + ".jpg &")
	  time.sleep(4.0)
	  print("PASS: " + str(i))
	  i = i + 1

