#!/usr/bin/python3

#!/usr/bin/python3
"""
A script that:
- Takes in a URL and an email,
- Sends a POST request to the URL with the email as a parameter,
- Displays the body of the response (decoded in utf-8).
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    # Get the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    email_bytes = email.encode("utf-8")
    request = urllib.request.Request(url, data=email_bytes, method="POST")

    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
        print(response_body)

