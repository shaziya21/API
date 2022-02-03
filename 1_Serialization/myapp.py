import requests
URL = "http://127.0.0.1:8000/stuinfo/1"

r = requests.get(url = URL)

#extract json from r which is response

data = r.json()
print(data)


# this is a separate app , not related to drf, python ,django... Its a thrd party
