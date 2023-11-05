#!/usr/bin/env python3
'''
This program is a simple gui for serial port selection.
Used as script returns port,baud,parity,stop,handshake
separated by spaces. Closing the windows or pressing
Cancel the returm value is None,115200,....
From python scripts call the function simple_serial_get()
which returns the tuple (port,baud,...)
Uses python3, pyserial and PySimpleGui

(c) Fabio Sturman fabio.sturman@gmail.com - 2023
This program is covered by
GNU General Public License, version 3
'''
import serial.tools.list_ports
import PySimpleGUI as sg

def simple_serial_get(default_data=[115200,8,'N',1,'None']):
    '''Returns tuple (port,baud,parity,stop,handshake)'''
    sg.theme('SystemDefault')
    ports = serial.tools.list_ports.comports()
    if len(ports)==0:
        sg.Popup('No com port!',font=('Ubuntu',10))
        return 'None',115200,8,'N',1,'None'
    ports.reverse()
    layout = [[sg.T('Port:',size=(8,1)),sg.Combo(ports,ports[0])],
              [sg.T('Baud:',size=(8,1)),sg.Combo([1200,2400,4800,9600,19200,38400,57600,115200],default_value=default_data[0])],
              [sg.T('NBits:',size=(8,1)),sg.Combo([7,8],default_value=default_data[1])],
              [sg.T('Parity:',size=(8,1)),sg.Combo(['N','O','E'],default_value=default_data[2])],
              [sg.T('Stop:',size=(8,1)),sg.Combo([1,2],default_value=default_data[3])],
              [sg.T('Handshake:',size=(8,1)),sg.Combo(['None','CTS/RTS','XON/XOFF'],default_value=default_data[4])],
              [sg.B('Ok'), sg.B('Cancel')]
             ]
    window = sg.Window("Port Configuration", layout, modal=True,font=('Ubuntu',10))
    while True:
        event, values = window.read()
        if event == "Ok": 
            port= values[0][0] 
        else:
            port= 'None'
        window.close()
        return port,values[1],values[2],values[3],values[4],values[5]
    
if __name__ == "__main__":
    '''Prints selected values for port,baud,parity,stop,handshake
    on stdout separated by spaces'''
    t=simple_serial_get()
    print(t[0],t[1],t[2],t[3],t[4],t[5])
