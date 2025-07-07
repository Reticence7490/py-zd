class RequestUtils:
    def send_request(self, method, url, json=None, headers=None):
        response = requests.request(method=method, url=url, json=json, headers=headers)
        return response.json()