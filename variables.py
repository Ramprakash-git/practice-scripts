#!/usr/bin/env python3

name = 'Ram'
hostname = 'mail.lab.local'
ssh_port = 2222
disk_usage = 79.5
service_running = True
port_str = '8080'

print(f"Admin   : {name}")
print(f"SSHPort : {ssh_port}")
print(f"Server  : {hostname}")
print(f"Disk    : {disk_usage}%")
print(f"Service : {service_running}")
port_int = int(port_str)
result = port_int + 1
print(result)

print(type(name))
print(type(hostname))
print(type(ssh_port))
print(type(disk_usage))
print(type(service_running))
print(type(port_int))
