import requests

from app.requests.get import test_get_endpoint
#from app.requests.create import test_post_endpoint

test_results = []

def redirect2method(url: str):
    """
        Redirecting a given URL to files by specifying a method
    """
    try:
        response = requests.get("http://127.0.0.1:8000/openapi.json")
        schema = response.json()

        for path, methods in schema["paths"].items():
            print(f"Endpoint: {path}")
            for method, details in methods.items():
                print(f"Method: {method.upper()}")
                if method.upper() == "GET":
                    print("Redirecting endpoint to the GET method")
                    #print("Details",details)
                    for param in details.get("parameters", []):
                        print(f"Testing the {path}")
                        test_results.append(test_get_endpoint(url=f"{url}{path}", query_param=param['name'], query_type=param['schema']['type'], 
                                          query_default_value=param['schema'].get('default', None), \
                                          required=param['required']))
                        print(test_results)
                        print(f"Test completed for {path}")
                # elif method == "POST":
                #     test_post_endpoint(url)
                else:
                    print("This type of method is not allowed")
                    
    except Exception as e:
        print(f"Error while fetching openapi.json: {e.args}")