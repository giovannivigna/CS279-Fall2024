#!/usr/bin/env python3
import sys
import requests
from csv import DictReader


def main(argv):
    if len(argv) != 3:
        print(f"Usage: {argv[0]} <URL> <ADMIN_TOKEN>")
        return 1
    url = sys.argv[1]
    token = sys.argv[2]

    # Create API Session
    url = url.strip("/")
    s = requests.Session()
    s.headers.update({"Authorization": f"Token {token}"})

    # See users.csv example template at https://docs.ctfd.io/docs/imports/csv#users
    users = DictReader(open("users.csv"))

    for user in users:
        # Note that the notify parameter is being passed here so CTFd will send the 
        # user an email with their credentials after the account is created
        r = s.post(
            f"{url}/api/v1/users?notify=true",
            json={
                "name": user["name"],
                "email": user["email"],
                "password": user["password"],
                "type": "user",
                "verified": True,
                "hidden": False,
                "banned": False,
                "fields": [],
            },
            headers={"Content-Type": "application/json"},
        )
        print(r.json())


if __name__ == "__main__":
    sys.exit(main(sys.argv))
