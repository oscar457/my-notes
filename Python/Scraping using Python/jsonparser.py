import json
import urllib.request, urllib.parse, urllib.error
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
data = urllib.request.urlopen(url, context=ctx).read().decode()

info = json.loads(data)
lst = info["comments"]
total = 0

for item in lst:
    total = total + int(item["count"])

print(total)
