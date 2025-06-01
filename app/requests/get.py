import requests

from app.generate import generate_random_value


def test_get_endpoint(url: str, query_param, query_type, query_default_value, required: bool = False):
    params = {}
    if required == True:
        params[query_param] = generate_random_value(query_type=query_type)
    send_request = requests.get(url, params=params)
    log_info_text = f"ENDPOINT FOR: {url} "\
                    f"Query parameter: {query_param} = {params[query_param]} " \
                    f"Result: {send_request.json()}"
    return log_info_text