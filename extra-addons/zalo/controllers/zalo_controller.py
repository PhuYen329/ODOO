# -*- coding: utf-8 -*-
from odoo import http
import logging
import zalo.services.api_zalo as api
import zalo.adapter.adapter as adapter
import request

class ZaloController(http.Controller):
    @http.route('/', auth='public', methods=['GET'], csrf=False)
    def index(self, **kwargs):
        oaid = kwargs.get('oaid')
        code = kwargs.get('code')
        # Do something with the oaid and code
        return 'Data received'
    @http.route('/settings/<string:app_id>/<string:redirect_uri>', auth='public', methods=['GET'], csrf=False)
    def settings(self, app_id, redirect_uri):
        url = f"https://oauth.zaloapp.com/v4/oa/permission?app_id={app_id}&redirect_uri={redirect_uri}"
        return http.Redirect(url)
