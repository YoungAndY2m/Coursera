import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1])
data = response.json()

import json
print(json.dumps(data, indent=2))
print(type(data)) # dict
for result in data["results"]:
    for key, value in result.items():
        print(key, value)
