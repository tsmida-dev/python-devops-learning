"""
Exercise 1: Server Information Display
Display server information in a professional format
"""

# Server details
hostname = "web-server-01"
ip_address = "192.168.1.100"
operating_system = "Ubuntu 22.04 LTS"
uptime_days = 45
cpu_percent = 67.5
memory_percent = 72.3

# TODO: Display this information in a professional format with borders
# Expected output:
# ================================================
# SERVER INFORMATION
# ================================================
# Hostname:       web-server-01
# IP Address:     192.168.1.100
# ...

print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")
print(f"Operation System: {operating_system}")
print(f"Uptime Days: {uptime_days}")
print(f"CPU: {cpu_percent}%")
print(f"Memory: {memory_percent}%")

"""
Exercise 2: Server Name Parser
Parse server name and extract components
"""

server_name = "web-server-prod-05"

# TODO: Extract and display:
# Type: web
# Role: server
# Environment: prod
# Number: 05

extract_name = server_name.split("-")
print(f"Type: {extract_name[0]}")
print(f"Role: {extract_name[1]}")
print(f"Environment: {extract_name[2]}")
print(f"Number: {extract_name[3]}")

"""
Exercise 3: Log Message Generator
Generate properly formatted log messages
"""

timestamp = "2025-10-26 14:30:00"
level = "INFO"
message = "Server started on port 8080"

# TODO: Generate log in format:
# [2025-10-26 14:30:00] INFO: Server started on port 8080

print(f"[{timestamp}] {level}: {message}")

"""
Exercise 4: Configuration Parser
Parse configuration strings
"""

config1 = "server.host=192.168.1.100"
config2 = "server.port=8080"
config3 = "server.timeout=30"

# Extract values by splitting on '=' and taking the second part
host = config1.split('=')[1]
port = config2.split('=')[1]
timeout = config3.split('=')[1]

# Display the values
print(f"Host: {host}")
print(f"Port: {port}")
print(f"Timeout: {timeout}")

"""
Exercise 5: Resource Usage Calculator
Calculate and display resource percentages
"""

total_memory = 16.0  # GB
used_memory = 12.5   # GB

total_disk = 500.0   # GB
used_disk = 387.3    # GB

# TODO: Calculate percentages and display:
# Memory: 12.5 GB / 16.0 GB (78.1%)
# Disk: 387.3 GB / 500.0 GB (77.5%)

memory = (used_memory / total_memory) * 100
disk = (used_disk / total_disk) * 100
print(f"Memory: {used_memory} GB/ {total_memory} GB ({memory:.1f}%)")
print(f"Disk: {used_disk} GB/ {total_disk} GB ({disk:.1f}%)")

"""
Day 1 Mini Project: Server Information Card
Interactive script that collects and displays server info
"""

print("=" * 50)
print("SERVER INFORMATION COLLECTOR")
print("=" * 50)

# TODO: Get user input for:
# - Server name
# - IP address
# - Environment
# - CPU, Memory, Disk usage percentages

# TODO: Display in a professional card format

server_name = input("Enter the server name: ")
ip_address = input("Enter the IP address: ")
environment = input("Enter the environment (e.g., Production, Staging): ")
cpu_usage = input("Enter CPU usage percentage: ")
memory_usage = input("Enter Memory usage percentage: ")
disk_usage = input("Enter Disk usage percentage: ")

print("\n" + "=" * 50)
print("SERVER INFORMATION CARD")
print("=" * 50)

print(f"Server Name   : {server_name}")
print(f"IP Address    : {ip_address}")
print(f"Environment   : {environment}")
print(f"CPU Usage     : {cpu_usage}%")
print(f"Memory Usage  : {memory_usage}%")
print(f"Disk Usage    : {disk_usage}%")