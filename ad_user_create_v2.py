import subprocess

# Get user input
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
username = input("Enter username: ")
password = input("Enter password: ")

# Construct PowerShell command to check if user exists
ps_command = f"Get-ADUser -Filter {{ SamAccountName -eq '{username}' }}"

# Execute PowerShell command to check if user exists
result = subprocess.run(["powershell", "-Command", ps_command], capture_output=True, text=True)

# Check if user exists
if "DistinguishedName" in result.stdout:
    # User already exists, prompt user to confirm overwrite
    overwrite = input("User already exists. Do you want to overwrite? (y/n) ")
    if overwrite.lower() != "y":
        print("User creation cancelled.")
        exit()

# Construct PowerShell command to create user account
ps_command = f"New-ADUser -GivenName '{first_name}' -Surname '{last_name}' -SamAccountName '{username}' -AccountPassword (ConvertTo-SecureString '{password}' -AsPlainText -Force) -Enabled $true"

# Execute PowerShell command to create user account
result = subprocess.run(["powershell", "-Command", ps_command], capture_output=True, text=True)

# Check if user account was created successfully
if "DistinguishedName" in result.stdout:
    print("User account created successfully.")
else:
    print("Error creating user account.")
    print(result.stderr)
