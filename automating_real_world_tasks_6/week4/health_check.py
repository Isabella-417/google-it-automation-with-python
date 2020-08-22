#!/usr/bin/env python3
import shutil
import psutil
import socket
import sched, time


"""
Report an error if CPU usage is over 80%
Report an error if available disk space is lower than 20%
Report an error if available memory is less than 500MB
Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
"""
def check_cpu_usage():
    return psutil.cpu_percent() > 80

def check_disk_space():
    return psutil.disk_usage('/').percent < 20

def check_available_memory():
    mb = 500 * 1024 * 1024  # 500MB
    return psutil.virtual_memory().available < mb

def check_hostname():
    socket.gethostbyname(socket.gethostname())

def check(sc):
    print("doing...")
    s.enter(60,1, check(sc,))

def main():
    s = sched.scheduler(time.time, time.sleep)
    s.run()


if __name__ == "__main__":
    main()
