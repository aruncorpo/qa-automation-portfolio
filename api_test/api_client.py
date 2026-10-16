import requests

class APIClient:
    def __init__(self, base_url, headers=None):
        self.session = requests.Session()
        self.base_url = base_url
        self.headers = headers
        if headers:
            self.session.headers.update(self.headers)

    def get(self, endpoint, parameters=None, timeout=10):
        endpoint = endpoint.lstrip("/")
        return self.session.get(url= self.base_url +"/"+ endpoint, params= parameters, timeout=timeout)

    def post(self, endpoint, payload, parameters=None, timeout=10):
        endpoint = endpoint.lstrip("/")
        return self.session.post(url= self.base_url +"/"+ endpoint,json= payload, params= parameters, timeout=timeout)

    def put(self, endpoint, payload, parameters=None, timeout=10):
        endpoint = endpoint.lstrip("/")
        return self.session.put(url=self.base_url +"/"+ endpoint, json=payload, params=parameters, timeout=timeout)

    def patch(self, endpoint, payload=None, parameters=None, timeout=10):
        endpoint = endpoint.lstrip("/")
        return self.session.patch(url=self.base_url +"/"+ endpoint, json=payload, params=parameters, timeout=timeout)

    def delete(self, endpoint, parameters=None, timeout=10):
        endpoint = endpoint.lstrip("/")
        return self.session.delete(url=self.base_url +"/"+ endpoint, params=parameters, timeout=timeout)

    def close(self):
        self.session.close()