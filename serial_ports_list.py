#
# serial_ports_list.py
#
# 
#  needed to executed 'pip install serial' befor using.
#

#from serial.tools import list_ports

import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
#print("ports=", ports)

for item in ports:
  print('name=', item.name)
  print('desc=', item.description)

# ser = serial.Serial(ports[0].device,9600,timeout=0.1)
