# %%
import requests
import pprint
import os
import IPython

# %%
ctf_url = os.environ["CTF_URL"]
ctf_token = os.environ["CTF_TOKEN"]
ctf_sitepwd = os.environ["CTF_SITEPWD"]
#ctf_sitepwd = ""

# %%
s = requests.Session()
s.headers.update({"Authorization": f"Token {ctf_token}"})
cookies={"site_password": f"{ctf_sitepwd}"}
r = s.get(
    f"{ctf_url}/api/v1/configs", cookies=cookies,
    headers={"Content-Type": "application/json"}
)
pprint.pprint(r)
if r.status_code == 200:
    pprint.pprint(r.json())
else:
    print("Received error: switching to interactive")
    IPython.embed()

# %%sudo 
print("Retrieving challenges")
r = s.get(
    f"{ctf_url}/api/v1/challenges", cookies=cookies,
    headers={"Content-Type": "application/json"}
)
pprint.pprint(r)
if r.status_code == 200:
    pprint.pprint(r.json())
else:
    print("Received error: switching to interactive")
    IPython.embed()

print("Retrieving services")
r = s.get(
    f"{ctf_url}/api/v1/services", cookies=cookies,
    headers={"Content-Type": "application/json"}
)
pprint.pprint(r)
if r.status_code == 200:
    pprint.pprint(r.json())
else:
    print("Received error: switching to interactive")
    IPython.embed()