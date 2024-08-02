#!/bin/python3

import sys
import socket
from datetime import datetime

#define target ip
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
else:
    print("Invalid input")
    print("Syntax: python3 scanner.py <ip>")

#banner
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

#trying to connect to target
try:
    for port in range(1,500):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) #socket timeout after 1 second to avoid infinite waiting time
        result = s.connect_ex((target, port)) #returns error indicator
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

#exceptions in case of errors
except KeyboardInterrupt: #Ctrl+C, Ctrl+Z
    print("\nExiting program.")
    sys.exit() #exits program

except socket.gaierror:
    print("\nHostname could not be resolved.")                                                                                                                                               
    sys.exit()                                                                                                                                                                               
                                                                                                                                                                                             
except socket.error:                                                                                                                                                                         
    print("\nCould not connect to server.")                                                                                                                                                  
    sys.exit()
