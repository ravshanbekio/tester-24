import requests

from app.requests.get import test_get_endpoint

def redirect2method(url: str):
    """
        Redirecting a given URL to files by specifying a method
    """
    response = requests.options(url).headers.get("Allow")
    if response == "GET":
        test_get_endpoint(url)
    else:
        print("This type of method is not allowed")