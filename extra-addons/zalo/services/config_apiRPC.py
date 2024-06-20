import requests
import xmlrpc.client
import logging

_logger = logging.getLogger(__name__)


class ConfigAPI:

    def __init__(self, app_id, secret_key, code, zaloURL):
        self.app_id = app_id
        self.secret_key = secret_key
        self.code = code
        self.zaloURL = zaloURL
        self.client = xmlrpc.client.ServerProxy(zaloURL)

    def get_access_token(self):
        # url = os.getenv("URL_API_ZALO") + "/oauth/access_token"
        url = self.zaloURL + "/oauth/access_token"
        data = {
            "grant_type": "authorization_code",
            "client_id": self.app_id,
            "client_secret": self.app_secret,
            "code": self.code,
        }
        response = requests.post(url, data=data)
        return response.json()["access_token"]
