#! python
import requests
import sys


def main(argv):
    try:
        url = argv[1]
        token = argv[2]
        user = argv[3]
        email = argv[4]
        password = argv[5]
    except IndexError:
        print(f"Usage: python3 {argv[0]} <url> <admin_token> <user> <email> <password>")
        sys.exit(1)

    # Create API Session
    url = url.strip("/")
    s = requests.Session()
    s.headers.update({"Authorization": f"Token {token}"})

    # NOTE: If you wish for the user's credentials to be emailed to them, pass the
    # notify=true parameter in the URL. For example: /api/v1/users?notify=true
    r = s.post(
        f"{url}/api/v1/users?notify=true",
        json={"name": user, "email": email, "password": password, "type":"user", "verified": True, "hidden":False, "banned":False, "fields":[]},
        headers={"Content-Type": "application/json"},
    )
    print(r.json())


if __name__ == "__main__":
    sys.exit(main(sys.argv))
