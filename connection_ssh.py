import paramiko

def ssh_authentication_attempt():
    # Create an SSH client
    client = paramiko.SSHClient()
    # Ignore the known_hosts file for simplicity in the demonstration
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # Connect to the SSH server with the fake credentials
        client.connect('98.66.139.28', username='backend_admin', password='HiddenAccess!')
        print("Authentication successful")  # This will be printed if authentication succeeds
    except paramiko.AuthenticationException:
        print("Authentication failed")  # This will be printed if authentication fails
    finally:
        # Close the SSH connection
        client.close()

if __name__ == "__main__":
    ssh_authentication_attempt()
