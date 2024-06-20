from ..util.access_token import AccessToken
from ..services.api_zalo import ZaloAPI
import json
from ..define.initialize_default_data import initialize_default_data

class Adapter(AccessToken):
    def __init__(self, adaptee: ZaloAPI):
        self.adaptee = adaptee

    def to_json(self) -> None:
        try:
            # Call the method
            return initialize_default_data(status="success", error=None, data=[self.adaptee.get_access_token()])
        except Exception as e:
            return initialize_default_data(error=str(e))
