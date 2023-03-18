import subprocess

# Define the PowerShell command to get a list of running processes
ps_command = "Get-Process"

# Use subprocess to run the PowerShell command and capture the output
output = subprocess.check_output(["powershell", ps_command])

# Print the output
print(output.decode())
