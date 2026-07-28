#!/usr/bin/env python3

services = ["httpd","sshd","exim","dovecot","firewalld"]

def sysinfo(hostname,user):
    print(f"{hostname}")
    print(f"{user}")

def check_disk(disk, threshold=80):
    if disk > 90:
        return "CRITICAL"
    elif disk > threshold:
        return "WARNING"
    else:
        return "OK"

def check_service(service):
    if service in services:
        return "True"
    else:
        return "False"

def print_report(service, isknown, status):
    print("==== Server Report ====")
    print(f" Service : {service}")
    print(f" Known   : {isknown}")
    print(f" Disk    : {status}")

def main():
    hostname = str(input("Enter your hostname: "))
    user = str(input("Enter your username: "))
    disk = float(input("Enter disk usage: "))
    service = str(input("Enter a service name: "))
    sysinfo(hostname,user)
    status = check_disk(disk)
    isknown = check_service(service)
    print_report(service, isknown, status)

main()
