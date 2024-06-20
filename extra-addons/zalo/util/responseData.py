# file: util/access_token.py

from .access_token import AccessToken
def responseData(access_token: AccessToken) -> None:
    return access_token.to_json()
