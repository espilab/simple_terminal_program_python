#
#
#  mini_term.py
#
#
#   ('pip install pyserial' required)

import serial
import serial.tools.list_ports
import msvcrt
import sys


# check received data and display the data if exist it
def disp_rcv_data():
  rx_len = ser.in_waiting
  if rx_len > 0:
    rcv_byte = ser.read(1)
    print(chr(rcv_byte[0]), sep="", end="", flush=True)

# check kbhit, and send the data
def send_kd_data():
  if msvcrt.kbhit():
    kbd = msvcrt.getch()
    #print('(kbd=',kbd,')', sep="", end="", flush=True)     #DEBUG

    # Ctrl-B to exit program
    if kbd == b'\x02':  
      return False 
    else:
      ser.write(kbd)
      ser.flush()
  return True



#-------- main --------
if __name__ == '__main__':

  if len(sys.argv) < 3:
    print('usage  : mini_term.py <com_port> <speed>')
    print('example: mini_term.py COM3 115200')
    exit(1)

  com_port_str = sys.argv[1]
  com_speed = sys.argv[2]

  try:
    ser = serial.Serial(com_port_str, int(com_speed))
  except:
    print('serial port open error. exit program')
    exit(1)

  print('Terminal program started. Press Ctrl-B to exit.')

  # loop: [ check receive data and print, read keyboard -> send ]
  run_flag = True
  while run_flag:
    disp_rcv_data()
    run_flag = send_kd_data()


  ser.close()
