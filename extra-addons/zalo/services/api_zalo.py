import request
import os

class ZaloAPI:
    def __init__(self, app_id, secret_key,code):
        self.app_id = app_id
        self.secret_key = secret_key
        self.code = code

    def get_access_token(self):
        url = os.getenv("URL_API_ZALO") + "/oauth/access_token"
        data = {
            "grant_type": "authorization_code",
            "client_id": self.app_id,
            "client_secret": self.app_secret,
            "code": self.code,
        }
        response = request.post(url, data=data)
        return response.json()["access_token"]
