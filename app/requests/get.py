import requests

from app.generate import generate_random_value


def test_get_endpoint(url: str, query_param = None, query_type = None, query_default_value = None, required: bool = False):
    params = {}
    if query_param:
        if required == True:
            params[query_param] = generate_random_value(query_type=query_type)
        else:
            params[query_param] = query_default_value

    send_request = requests.get(url, params=params)
    # log_info_text = f"ENDPOINT FOR: `{url}` \n"\
    #                 f"Query parameter: {query_param} = {params[query_param]} \n" \
    #                 f"Result: {send_request.json()}" 
    return {
        "status_code":send_request.status_code,
        "result": send_request.json()
    }