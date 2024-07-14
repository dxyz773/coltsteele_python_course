import requests

res = requests.get("https://news.ycombinator.com/", headers={})

print(res.text)
