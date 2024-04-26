from big_thing_py.utils.log_util import *
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from enum import Enum
from typing import Optional, Dict, Any

from dataclasses import dataclass

# Suppress only the single InsecureRequestWarning from urllib3 needed
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class RequestMethod(Enum):
    GET = 'GET'
    OPTIONS = 'OPTIONS'
    HEAD = 'HEAD'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'


@dataclass
class RequestResponse:
    ok: bool
    reason: str
    status_code: int
    json: dict = None
    text: str = None


def api_request(
    method: RequestMethod,
    url: str,
    query: Dict[str, Any] = None,
    data: Dict[str, Any] = None,
    headers: Dict[str, Any] = None,
    body: Dict[str, Any] = None,
    auth: Tuple[str, str] = None,
    verify: bool = False,
    timeout: float = None,
    retries: int = 3,
) -> Optional[RequestResponse]:
    headers = headers or {}
    for attempt in range(retries):
        try:
            response = requests.request(
                method=method.value,
                url=url,
                params=query,
                data=data,
                headers=headers,
                json=body,
                auth=auth,
                verify=verify,
                timeout=(1, timeout) if timeout else None,
            )
            try:
                request_response = RequestResponse(ok=response.ok, reason=response.reason, status_code=response.status_code, json=response.json())
            except Exception as e:
                request_response = RequestResponse(ok=response.ok, reason=response.reason, status_code=response.status_code, text=response.text)

            if request_response.ok:
                return request_response
            else:
                MXLOG_ERROR(f'Response validation failed, Status Code: {response.status_code}. Attempt: {attempt + 1}')
        except requests.exceptions.RequestException as e:
            MXLOG_WARN(f'Failed to request API: {e}. Attempt: {attempt + 1}')
    else:
        MXLOG_ERROR('All API requests failed after retries.')
        return RequestResponse(ok=False, reason='', status_code=None, json={})


if __name__ == '__main__':
    response = api_request('https://www.google.com')
    print(response)
