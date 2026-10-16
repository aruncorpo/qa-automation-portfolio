import pytest
from requests.exceptions import Timeout

@pytest.mark.parametrize(
    "userid",
    (1, 2, 3),
    ids=["expecting_userId 1", "expecting_userId 2", "expecting_userId 3"]
)

def test_get_posts_by_user(api_client, userid):
    parameters = {"userId": str(userid)}
    endpoint = "/posts"
    timeout = 10
    apiclient = api_client

    response_get = apiclient.get(endpoint, parameters, timeout)
    data = response_get.json()
    get_headers = response_get.headers

    assert response_get.status_code == 200, f"Failed to create, Status Code :{response_get.status_code}"
    assert "json" in get_headers["Content-Type"], f"Content Type not Json,{get_headers["Content-Type"]}"
    assert len(data) > 1, f"Data is empty - size {len(data)}"

    for element in range(len(data)):
        assert int(data[element]['userId']) == userid, f"list index {element} expected userId {userid} received {data[element]["userId"]}"

def test_get_posts_for_unknown_user(api_client):
    parameters = {"userId": "9999"}
    endpoint = "/posts"
    timeout = 10
    apiclient = api_client

    response_get = apiclient.get(endpoint, parameters, timeout=10)
    data = response_get.json()
    get_headers = response_get.headers

    assert response_get.status_code == 200, f"Failed to create, Status Code :{response_get.status_code}"
    assert "json" in get_headers["Content-Type"], f"Content Type not Json,{get_headers["Content-Type"]}"
    assert isinstance(data, list), f"data is not a list {type(data)}"
    assert len(data) == 0, f"is not empty, size: {len(data)}"


def test_post(api_client):

    payload = {
        "title": "who is butters?",
        "body": "I am butters",
        "userId": "1"
    }
    timeout = 10
    endpoint = "/posts"

    responses = api_client.post(endpoint, payload, timeout=10)
    assert responses.status_code == 201, f"Status Code: {responses.status_code}"

    data = responses.json()
    assert data["title"] == "who is butters?", f"data mismatch {data["title"]}"
    assert data["body"] == "I am butters", f"data mismatch {data["body"]}"
    assert int(data["userId"]) == 1, f"data mismatch {data["userId"]}"
    assert data["id"], f"Failed to create ID"

def test_request_timeout(api_client):
    endpoint = "/posts"
    with pytest.raises(Timeout):
        api_client.get(endpoint, timeout=0.000001)

def test_get_unknown_resource(api_client):
    endpoint = "/posts/999999"
    responses = api_client.get(endpoint)
    assert responses.status_code == 404, f"Failed to get, Status Code :{responses.status_code}"
    response_headers = responses.headers
    assert "application/json" in response_headers['Content-Type'], f"Content Type not Json,{response_headers["Content-Type"]}"
    data = responses.json()
    print(data)

def test_put_post(api_client):
    endpoint = "/posts/1"
    payload = {
        "id": 1,
        "title":"Updated by API test",
        "body":"Testing PUT with pytest",
        "userId": 1
    }

    responses = api_client.put(endpoint, payload)
    assert responses.status_code == 200, f"Failed to put, Status Code :{responses.status_code}"
    data = responses.json()
    assert int(data["id"]) == payload["id"], f"id mismatch {data["id"]}"
    assert payload["title"] == data["title"], f"title mismatch {data["title"]}"
    assert payload["body"] == data["body"], f"body mismatch {data["body"]}"
    assert int(data["userId"]) == payload["userId"], f"userId mismatch {data["userId"]}"

def test_patch_post(api_client):
    endpoint = "/posts/1"
    payload = {
        "title": "Patched title by pytest"
    }

    responses = api_client.patch(endpoint, payload)
    assert responses.status_code == 200, f"Failed to put, Status Code :{responses.status_code}"
    data = responses.json()
    assert data["id"] == 1, f"No ID found"
    assert payload["title"] == data["title"], f"title mismatch {data["title"]}"
    assert "quia et" in data["body"], f"No body found"
    assert data["userId"] == 1, f"No userId found"

def test_delete_post(api_client):
    endpoint = "/posts/1"
    responses = api_client.delete(endpoint)
    assert responses.status_code == 200, f"Failed to delete, Status Code :{responses.status_code}"
    data = responses.json()
    print(data)