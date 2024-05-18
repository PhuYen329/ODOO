import json
class AccessToken:
    def __init__(self, access_token):
        self.access_token = access_token

    def get_access_token(self):
        return self.access_token