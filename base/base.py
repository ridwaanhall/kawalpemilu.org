import requests

class DataFetcher:
    @staticmethod
    def fetch_data_from_url(url, payload, headers):
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)
            return None

    @staticmethod
    def fetch_json_data(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            json_data = response.json()
            return json_data
        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)
            return None

    @staticmethod
    def perform_option(option):
        if option == "1":
            url1 = "https://us-central1-kp24-fd486.cloudfunctions.net/hierarchy2"
            payload1 = {"data": {"id": ""}}
            headers1 = {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "en-US,en;q=0.9,mt;q=0.8",
                "Cache-Control": "no-cache",
                "Content-Type": "application/json",
                "Dnt": "1",
                "Origin": "https://kawalpemilu.org",
                "Pragma": "no-cache",
                "Referer": "https://kawalpemilu.org/",
                "Sec-Ch-Ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": "\"Windows\"",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "cross-site",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
            }
            json_data = DataFetcher.fetch_data_from_url(url1, payload1, headers1)
            if json_data:
                print("JSON Data fetched successfully from cloudfunctions.net!")
                # print(json_data)
            else:
                print("Failed to fetch JSON data from cloudfunctions.net.")
        elif option == "2":
            url2 = "https://kawalpemilu.org/assets/tps.json"
            json_data = DataFetcher.fetch_json_data(url2)
            if json_data:
                print("JSON Data fetched successfully from kawalpemilu.org!")
                # print(json_data)
            else:
                print("Failed to fetch JSON data from kawalpemilu.org.")
        elif option == "3":
            url2 = "https://kawalpemilu.org/assets/tps2.json"
            json_data = DataFetcher.fetch_json_data(url2)
            if json_data:
                print("JSON Data fetched successfully from kawalpemilu.org!")
                # print(json_data)
            else:
                print("Failed to fetch JSON data from kawalpemilu.org.")
        else:
            print("Invalid option. Please choose 1 or 2 or 3.")
