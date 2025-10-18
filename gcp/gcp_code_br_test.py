import requests, json

url = "https://total-billirubin-776757242044.us-east1.run.app"

# POST example
r = requests.post(url, json={"total_bilirubin": 0.8, "direct_bilirubin": 0.1})
print(r.status_code, r.json())  # expect: "status": "normal"

r = requests.post(url, json={"total_bilirubin": 2.5, "direct_bilirubin": 0.1})
print(r.status_code, r.json())  # expect: "status": "abnormal", jaundice risk

# GET example (optional)
r = requests.get(url, params={"total_bilirubin": 0.8, "direct_bilirubin": 0.1})
print(r.status_code, r.json())
