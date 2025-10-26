# Variables in DevOps context
# Use snake_case for variable names
# Choose descriptive names

server_name = "web-server-01"
ip_address = "192.168.1.100"
port = 8080
is_running = True
cpu_usage = 67.5

print(f"Server: {server_name}")
print(f"IP: {ip_address}")
print(f"Port: {port}")
print(f"Running: {is_running}")
print(f"CPU: {cpu_usage}%")

# Data Types
# Four fundamental types

hostname = "web-01"
port = 8080
cpu_percent = 67.5
is_active = True

# Check types
print(type(hostname))
print(type(port))
print(type(cpu_percent))
print(type(is_active))

# String Operations

server = "web-server-01"

# Essential string methods
print(server.upper())
print(server.lower())
print(server.replace("01", "02"))
print(server.split("-"))
print(server.startswith("web"))
print(server.endswith("01"))

# String formatting (f-string - USE THIS!)
name = "ngix"
version = "1.21.0"
print(f"Service {name} version {version}")

# Multi-line string (for configs)
config = """
server {
    listen 80;
    server_name example.com;
}
"""

# Practical String Examples

# Example 1: Parse server name
server_name = "web-server-prod-01"
parts = server_name.split("-")
server_type = parts[0]
enviroment = parts[2]
number = parts[3]
print(f"Type: {server_type}, Env: {enviroment}, #: {number}")

# Example 2: CLean user input
user_input = "  Production  "
env = user_input.strip().lower()

# Example 3: Check logs
log = "[ERROR] Database connection failed"
if "ERROR" in log:
    print("⚠️  Error detected in logs!")

# Example 4: Build URLs
host = "api-server"
port = 8080
url = f"http://{host}:{port}/health"
print(url)

# User Input
# Getting and validating input
enviroment = input("Enter enviroment (dev/staging/prod): ")
enviroment = enviroment.strip().lower()

if enviroment in ["dev", "staging", "prog"]:
    print(f" Deploying to {enviroment}")
else:
    print(f" Invalid enviroment: {enviroment}")

# Converting input types
port_str = input("Enter port number: ")
port = int(port_str)
print(f"Using port {port}")

