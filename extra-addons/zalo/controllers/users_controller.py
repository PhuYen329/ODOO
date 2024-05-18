# -*- coding: utf-8 -*-
from odoo import http
import logging
import zalo.services.api_zalo as api
import zalo.adapter.adapter as adapter
import request
class users_controller(http.Controller):
    @http.route('/zalo/settings', auth='public', methods=['POST'], csrf=False) 
    def settings(self, app_id, redirect_uri):
        # Xử lý dữ liệu tại đây
        # ...
        return http.redirect(
            f"https://oauth.zaloapp.com/v4/oa/permission?app_id={app_id}&redirect_uri={redirect_uri}"
        )
