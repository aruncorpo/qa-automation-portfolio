import pytest
from api_test.api_client import APIClient

@pytest.fixture
def api_client():
    base_url = "https://jsonplaceholder.typicode.com"
    apiclient = APIClient(base_url)
    yield apiclient
    apiclient.close()