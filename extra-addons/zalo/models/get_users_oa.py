from odoo import models, fields,api

class ZaloOaUser(models.Model):
    _name = 'zalo_oa_user'
    _description = 'Zalo OA User'

    user_id = fields.Char(string='User ID', required=True)
    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    avatar = fields.Binary(string='Avatar')



    def set_user_id(self, value):
        self.name = value

    def set_name(self, value):
        self.name = value

    def set_avatar(self, value):
        self.avatar = value

    def set_email(self, value):
        self.email = value

    def set_phone(self, value):
        self.phone = value

    def get_user_íd(self):
        # Lấy avatar của người dùng
        return self.avatar
    def get_avatar(self):
        # Lấy avatar của người dùng
        return self.avatar

    def get_name(self):
        # Lấy tên của người dùng
        return self.name

    def get_email(self):
        # Lấy email của người dùng
        return self.email

    def get_phone(self):
        # Lấy số điện thoại của người dùng
        return self.phone
