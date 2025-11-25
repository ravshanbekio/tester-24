import requests
import json
from typing import Any
from datetime import datetime

from app.requests.get import test_get_endpoint
#from app.requests.create import test_post_endpoint

test_results = []

def redirect2method(url: str):
    """
        Redirecting a given URL to files by specifying a method
    """
    try:
        response = requests.get(f"{url}/openapi.json")
        schema = response.json()
        data = {}

        for path, methods in schema["paths"].items():
            #print(f"Endpoint: {path}") Displays endpoint path only
            for method, details in methods.items():
                #print(f"Method: {method.upper()}") Displays the method of the endpoint
                if method.upper() == "GET":
                    #print("Details",details) Displays details of the path
                    params = details.get("parameters", [])
                    if params:
                        for param in details.get("parameters", []):
                            print(f"[{datetime.now().replace(microsecond=0)}]: Testing the `{path}`")
                            test_result = test_get_endpoint(url=f"{url}{path}", query_param=param['name'], query_type=param['schema']['type'], 
                                            query_default_value=param['schema'].get('default', None), \
                                            required=param['required'])
                            #print(test_result) Displays the details of the request
                            data[path] = {
                                "method": method.upper(),
                                "status_code": test_result['status_code'],
                                "result": test_result['result']
                            }
                            test_results.append(test_result)
                            print(f"[{datetime.now().replace(microsecond=0)}]: Test completed for `{path}`")
                            print("\n" * 1)
                # elif method == "POST":
                #     test_post_endpoint(url)
                else:
                    print(f"{method.upper()} method is not allowed")
                    print("\n" * 1)
                    
        with open("results.json",'w') as file:
            json.dump(data, file, indent=4)

    except Exception as e:
        print(f"Error while fetching openapi.json: {e.args}")