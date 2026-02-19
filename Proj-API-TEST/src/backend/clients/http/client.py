import requests
from http import HTTPMethod
from urllib.parse import urljoin
import time
from typing import Optional

from src.backend.clients.http.utils import attach_request_data


class HTTPClient:

    def __init__(self, host: str, default_headers: Optional[dict] = None):
        self._host = host
        self._default_headers = default_headers


    def get(self, route: str, headers: Optional[dict] = None, params: Optional[dict] = None) -> requests.Response:
        return self._request(method=HTTPMethod.GET, route=route, headers=headers, params=params)



    def post(self, route: str, headers: Optional[dict] = None, json: Optional[dict] = None, data: Optional[str] = None) -> requests.Response:
        return self._request(method=HTTPMethod.POST, route=route, headers=headers, json=json, data=data)
    

    def delete(self, route: str, headers: Optional[dict] = None, json: Optional[dict] = None, data: Optional[dict] = None, params: Optional[dict] = None):
        return self._request(method=HTTPMethod.DELETE, route=route, headers=headers, json=json, data=data, params=params)



    def _request(self, method: HTTPMethod, route: str,headers: Optional[dict] = None, **kwargs) -> requests.Response:
        with requests.Session() as session:
            url = urljoin(base=self._host, url=route)

            req_headers = {}
            if self._default_headers:
                req_headers.update(self._default_headers)               
            if headers:
                req_headers.update(headers)
            request_time = time.time()
            response = session.request(method=method, url=url, headers=req_headers, **kwargs)
            response_time = time.time()
            attach_request_data(response=response, request_time=request_time, response_time=response_time)

            return response