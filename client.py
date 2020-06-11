import requests

r = requests.get("http://127.0.0.1:5000/info")
answer = r.json()
print(answer["calc_info"])

out_json = {"age": 21, "height_in": 72, "gender": "male"}
r = requests.post("http://127.0.0.1:5000/iwc", json=out_json)
print(r.json())

r = requests.get("http://127.0.0.1:5000/hello/Anne")
print(r.text)