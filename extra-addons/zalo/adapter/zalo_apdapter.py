import request
import json

class ZaloOaAdapter:
    def __init__(self, app_id, secret_key, redirect_uri,code):
        self.app_id = app_id
        self.secret_key = secret_key
        self.redirect_uri = redirect_uri
        self.code = code

    def get_access_token(self):
        # Thực hiện yêu cầu truy cập token
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'app_id': self.app_id,
            'secret_key': self.secret_key,
            'redirect_uri': self.redirect_uri,
            'grant_type': 'authorization_code',
            'code':self.code
        }
        response = request.post('https://openapi.zalo.me/v4/oauth/access_token', headers=headers, data=data)
        access_token = json.loads(response.content)['access_token']
        return access_token

    def make_api_call(self, endpoint, method='GET', data=None):
        # Thực hiện các yêu cầu API đối với Zalo OA
        headers = {
            'Authorization': f'Bearer {self.get_access_token()}'
        }
        if method == 'POST':
            response = requests.post(f'https://openapi.zalo.me/v4/{endpoint}', headers=headers, json=data)
        else:
            response = requests.get(f'https://openapi.zalo.me/v4/{endpoint}', headers=headers)
        return json.loads(response.content)

    def get_user_info(self, user_id):
        # Lấy thông tin người dùng từ Zalo OA
        endpoint = f'users/{user_id}'
        response = self.make_api_call(endpoint)
        return response

    def send_message(self, user_id, message):
        # Gửi tin nhắn đến người dùng qua Zalo OA
        endpoint = f'messages'
        data = {
            'receiver_id': user_id,
            'text': message
        }
        response = self.make_api_call(endpoint, method='POST', data=data)
        return response

    def get_conversation(self, user_id):
        # Lấy lịch sử trò chuyện với người dùng từ Zalo OA
        endpoint = f'conversations/{user_id}'
        response = self.make_api_call(endpoint)
        return response