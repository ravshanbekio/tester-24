import requests

def test_get_endpoint(url: str):
    send_request = requests.get(url)
    endpoint_options = requests.options(url)
    if send_request.status_code == 200:
        print({"message":send_request.json(), "options":endpoint_options.headers.get("Allow")})
    else:
        print(send_request.text)