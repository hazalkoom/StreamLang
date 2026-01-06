import requests

url = "http://127.0.0.1:8000/run"
payload = {"code": "5 |> add(10) |> print;"}

try:
    print(f"👉 Sending request to {url}...")
    response = requests.post(url, json=payload)
    
    print("👉 Status Code:", response.status_code)
    print("👉 Raw Response Text:")
    print(response.text)
    
    print("\n👉 JSON Content:")
    print(response.json())

except Exception as e:
    print(f"❌ Error: {e}")