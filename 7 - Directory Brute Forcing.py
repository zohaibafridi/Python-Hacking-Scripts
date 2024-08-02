import requests

def dir_bruteforce(url, wordlist):
    with open(wordlist, 'r') as f:
        for line in f:
            directory = line.strip()
            full_url = f"{url}/{directory}"
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f"Found: {full_url}")

url = 'http://example.com'
wordlist = 'wordlist.txt'
dir_bruteforce(url, wordlist)
