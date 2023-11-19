#
#  mini_term_simple_version.py
#
#

import serial
import serial.tools.list_ports
import msvcrt

try:
    ser = serial.Serial('COM6', 115200)
except:
    print('serial port open error. exit program')
    exit(1)

run_flag = True

print('Terminal program started. Press Ctrl-B to exit.')

while run_flag:
    if ser.in_waiting > 0:
        rcv = ser.read(1)
        if (rcv >= b'\x0a') and (rcv < b'\x80'):
            rcv_char = chr(rcv[0])    
            print(rcv_char, sep="", end="", flush=True)

    if (msvcrt.kbhit()):
        kbd = msvcrt.getch()
        ser.write(kbd)
        ser.flush()
        if kbd == b'\x02':     # Ctrl-B
            run_flag = False

ser.close()
