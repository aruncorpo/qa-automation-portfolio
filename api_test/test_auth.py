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


    api_token = os.getenv("API_TOKEN")
    assert api_token, "Token is empty, failed to retrieve token"
    header = {
        "authorization": f"Bearer {api_token}"
    }
    api_client2 = APIClient(url, header)
    responses3 = api_client2.get(endpoint=endpoint)
    data2 = responses3.json()
    assert data2["token"] == api_token,f"Token mismatch"