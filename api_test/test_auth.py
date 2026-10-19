from api_test.api_client import APIClient
import os

def test_auth():

    url = "https://httpbin.org"
    headers = {
        "authorization": "Bearer practice-token"
    }
    endpoint = "/bearer"


    api_client = APIClient(url, headers)
    responses = api_client.get(endpoint=endpoint)
    assert responses.status_code == 200, f"Failed to create, Status Code :{responses.status_code}"
    data = responses.json()
    assert data["authenticated"] == True, f"Failed, authentication"
    assert data["token"] == "practice-token", f"Token mismatch {data["token"]}"


    api_client2 = APIClient(url)
    responses2 = api_client2.get(endpoint=endpoint)
    assert responses2.status_code == 401, f"Failed, Status Code :{responses2.status_code}"
