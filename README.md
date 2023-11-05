# simple_serial
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
