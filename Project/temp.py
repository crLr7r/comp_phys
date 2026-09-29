import requests

url = "https://api.openalex.org/fields"

params = {
    "search": "physics",
    "per-page": 10
}

response = requests.get(url, params=params)
data = response.json()

for field in data["results"]:
    print(field["id"], field["display_name"])

import requests

url = "https://api.openalex.org/subfields"

params = {
    "filter": "field.id:31",
    "per-page": 100
}

response = requests.get(url, params=params)
data = response.json()

print("status:", response.status_code)
print("개수:", len(data["results"]))

for subfield in data["results"]:
    print(
        subfield["id"],
        "→",
        subfield["display_name"]
    )