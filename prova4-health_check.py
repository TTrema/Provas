#!/usr/bin/env python3

import shutil
import psutil
import socket
import time
import emails

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage

def check_ram_usage():
    usage = psutil.virtual_memory()
    return usage

def hostname_resolves(hostname):
    try:
        socket.gethostbyname(hostname)
        return True
    except socket.error:
        return False

disk = check_disk_usage("/")
cpu = check_cpu_usage()
ram = check_ram_usage()[4]
host = hostname_resolves("127.0.0.1") 

print("Pc is stable \nfree space: {:.2f}% \nCPU usage: {:.2f}% \nfree memory: {} \nhost connection: {}".format(disk,cpu,ram,host))


with open('error.txt', 'w') as f:
    f.write("Please check your system and resolve the issue as soon as possible.")
if cpu > 80:
    emails.send(emails.generate("automation@example.com", "student-01@example.com", "CPU usage is over 80%", "Please check your system and resolve the issue as soon as possible.", "error.txt"))
    time.sleep(60)
elif disk < 20:
    emails.send(emails.generate("automation@example.com", "student-01@example.com", "Error - Available disk space is less than 20%", "Please check your system and resolve the issue as soon as possible.", "error.txt"))
    time.sleep(60)
elif ram < 80:
    emails.send(emails.generate("automation@example.com", "student-01@example.com", "Error - Available memory is less than 500MB", "Please check your system and resolve the issue as soon as possible.", "error.txt"))
    time.sleep(60)
elif host != True:
    emails.send(emails.generate("automation@example.com", "student-01@example.com", "Error - localhost cannot be resolved to 127.0.0.1", "Please check your system and resolve the issue as soon as possible.", "error.txt"))
    time.sleep(60)
else:
    time.sleep(60)