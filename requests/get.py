import requests

url = 'https://edition.cnn.com'
res = requests.get(url)

print("Status code: {}".format(res.status_code))
print("Encoding: {}".format(res.encoding))
print("=== Headers ===")
for key in res.headers:
    print("{} --- {}".format(key, res.headers[key]))
