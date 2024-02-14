import requests
from base.report import url, payload, headers

def fetch_data_from_url(url, payload, headers):
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

if __name__ == "__main__":
    data_from_url = fetch_data_from_url(url, payload, headers)
    if data_from_url:
        print("Data fetched successfully")
        # print("Data fetched successfully:", data_from_url)
    else:
        print("Failed to fetch data from the URL.")
