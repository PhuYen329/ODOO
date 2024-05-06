# -*- coding: utf-8 -*-
# from odoo import http
class ZaloOaController(http.Controller):
    @http.route('/zalo_oa/callback', auth='public', methods=['POST'], csrf=False)
    def zalo_oa_callback(self, **kwargs):
        # Xử lý yêu cầu callback từ Zalo OA
        zalo_oa_adapter = request.env['zalo_oa_adapter'].sudo().create({
            'app_id': 'your_app_id',
            'secret_key': 'your_secret_key',
            'redirect_uri': 'your_redirect_uri'
        })
        access_token = zalo_oa_adapter.get_access_token()
        user_info = zalo_oa_adapter.get_user_info('user_id')
        message = zalo_oa_adapter.send_message('user_id', 'message_text')
        conversation = zalo_oa_adapter.get_conversation('user_id')
        #...