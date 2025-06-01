import requests
import json

response = requests.get("http://127.0.0.1:8000/openapi.json")
schema = response.json()

# Getting all endpoint
for path, methods in schema["paths"].items():
    print(f"Endpoint: {path}")
    for method, details in methods.items():
        print(f"  Method: {method.upper()}")
        print("Details",details)
        print("  Parameters:")
        for param in details.get("parameters", []):
            print(f"{param['name']} (required: {param['required']}): {param['schema']['type']} = {param['schema']['default']}")