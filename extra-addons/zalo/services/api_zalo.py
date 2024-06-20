import requests
import os
import logging

_logger = logging.getLogger(__name__)


class ZaloAPI:
    def __init__(self, app_id, secret_key, code):
        self.app_id = app_id
        self.secret_key = secret_key
        self.code = code
        self.base_url = os.getenv("URL_API_ZALO")

    def get_access_token(self):
        url = f"{self.base_url}/oa/access_token"
        try:
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "secret_key": self.secret_key
            }
            data = {
                "app_id": self.app_id,
                "code": self.code, 
                "grant_type": "authorization_code",
                
            }
            _logger.debug(f"Sending request to URL: {url} with data: {data}")
            response = requests.post(url,headers=headers, data=data)
            response.raise_for_status()
            response_data = response.json()
            _logger.debug(f"Response data: {response_data}")
            return response_data.get("access_token")  # Return the actual access token
        except requests.exceptions.RequestException as e:
            _logger.error(f"Error fetching access token from API: {e}")
            return None

    def fetch_data_from_api(self):
        url = "https://api.mocki.io/v1/b043df5a"  # URL của API giả lập
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            # Xử lý dữ liệu và lưu vào Odoo nếu cần
            env = requests.env
            Model = env[
                "your.model.name"
            ]  # Thay your.model.name bằng tên model của bạn
            for item in data:
                Model.sudo().create(
                    {
                        "name": item.get("name"),
                        "value": item.get("value"),
                    }
                )
        except requests.exceptions.RequestException as e:
            _logger.error(f"Error fetching data from API: {e}")
