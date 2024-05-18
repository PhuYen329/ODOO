import zalo.services.access_token as accessToken
import zalo.services.api_zalo as api


class Adapter(accessToken.AccessToken):
    def __init__(self, adaptee: api.ZaloAPI) :
        self.adaptee = adaptee


def get_access_token(self):
    data = self.adaptee.get_access_token()
    return accessToken.AccessToken(data)
