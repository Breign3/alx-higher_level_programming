#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status."""

from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    request = Request(url)

    with urlopen(request) as response:
        raw_content = response.read()
        decoded_content = raw_content.decode('utf-8')
        body = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
