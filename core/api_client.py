
import requests

def get(url, headers=None, params=None):
    return requests.get(
        url=url,
        headers=headers,
        params=params
    )

def post(url, headers=None, payload=None):
    if payload is None:
        return requests.post(
            url=url,
            headers=headers
        )
    return requests.post(
        url=url,
        headers=headers,
        json=payload
    )

def delete(url, headers=None, payload=None):
    if payload is None:
        return requests.delete(
            url=url,
            headers=headers
        )
    return requests.delete(
        url=url,
        headers=headers,
        json=payload
    )
