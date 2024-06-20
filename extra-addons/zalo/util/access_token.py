# file: util/access_token.py

class AccessToken:
    def __init__(self, access_token):
        self._access_token = access_token

    def to_json(self):
        return self._access_token
