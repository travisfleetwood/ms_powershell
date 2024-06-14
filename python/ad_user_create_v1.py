import subprocess

# Prompt user for user details
first_name = input("First name: ")
last_name = input("Last name: ")
username = input("Username: ")
password = input("Password: ")

# Check if the user already exists in Active Directory
cmd_check_user = f"Get-ADUser -Filter {{SamAccountName -eq '{username}'}}"
result = subprocess.run(["powershell", "-Command", cmd_check_user], capture_output=True, text=True)
if result.stdout:
    overwrite = input(f"A user with the username '{username}' already exists. Do you want to overwrite it? (y/n) ")
    if overwrite.lower() != 'y':
        print("User creation canceled.")
        exit()

# Create the user in Active Directory
cmd_create_user = f"New-ADUser -Name '{first_name} {last_name}' -SamAccountName '{username}' -AccountPassword (ConvertTo-SecureString '{password}' -AsPlainText -Force)"
subprocess.run(["powershell", "-Command", cmd_create_user])

# Set user properties
cmd_set_user = f"Set-ADUser -Identity '{username}' -GivenName '{first_name}' -Surname '{last_name}' -UserPrincipalName '{username}@example.com' -Description 'Created by Python script'"
subprocess.run(["powershell", "-Command", cmd_set_user])

# Add user to a group
cmd_add_group = f"Add-ADGroupMember -Identity 'Employees' -Members '{username}'"
subprocess.run(["powershell", "-Command", cmd_add_group])

print(f"User account for {first_name} {last_name} created successfully.")
