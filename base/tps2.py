import requests

def fetch_json_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()
        return json_data
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

if __name__ == "__main__":
    url = "https://kawalpemilu.org/assets/tps2.json"
    json_data = fetch_json_data(url)
    if json_data:
        print("JSON Data fetched successfully!")
        # print(json_data)
    else:
        print("Failed to fetch JSON data.")
