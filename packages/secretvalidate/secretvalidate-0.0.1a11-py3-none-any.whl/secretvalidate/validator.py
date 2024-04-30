import json
import requests
import os

# Reuse session for multiple requests
session = requests.Session()

def get_headers(service, secret):
    headers_map = {
        'snyk': {'Authorization': f'token {secret}'},
        'sonarcloud': {'Authorization': f'Bearer {secret}'}
        # Add more services here as needed
    }
    return headers_map.get(service, {})

def load_settings():
    with open("urls.json", "r") as f:
        return json.load(f)

def get_service_url(service):
    current_dir = os.path.dirname(os.path.dirname(__file__))
    urls_path = os.path.join(current_dir, 'urls.json')

    with open(urls_path, 'r') as f:
        urls = json.load(f)

    service_url = urls.get(service)

    if not service_url:
        raise ValueError(f"Error: URL for service {service} not found.")

    return service_url

def validate(service, secret, response):
    headers = get_headers(service, secret)
    url = get_service_url(service)

    try:
        with session.get(url, headers=headers, verify=True) as response_data:
            response_data.raise_for_status()  # Raise an HTTPError for bad responses

            if response_data.status_code == 200:
                if response:
                    return "Active"
                else:
                    try:
                        json_response = response_data.json()
                        return json.dumps(json_response, indent=4)
                    except json.JSONDecodeError:
                        return "Response is not a valid JSON."
            else:
                if response:
                    return "InActive"
                else:
                    return response_data.text
    except requests.HTTPError as e:
        if response:
            return "InActive"
        else:
            return e.response.text
    except requests.RequestException as e:
        return None

# def main(service, secret, response):  
#     try:
#         # Call the validate function with provided arguments
#         result = validate(service, secret, response)
#         print(result)
#     except Exception as e:
#         print(f"Error: {e}")
