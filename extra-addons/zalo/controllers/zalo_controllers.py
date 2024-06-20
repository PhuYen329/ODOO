from odoo import http
from odoo.http import request
import logging
import json

from ..services.api_zalo import ZaloAPI
from ..adapter.adapter import Adapter
from ..util.responseData import responseData
from ..define.initialize_default_data import initialize_default_data

_logger = logging.getLogger(__name__)


class ZaloConfigController(http.Controller):

    def _update_or_create_config(self, oa_id, code):
        env = request.env
        config_settings = (
            env["res.config.settings"].sudo().search([], limit=1, order="id desc")
        )
        if config_settings:
            config_settings.write({"oa_id": oa_id, "code": code})
        else:
            config_settings = (
                env["res.config.settings"].sudo().create({"oa_id": oa_id, "code": code})
            )
        return config_settings

    def _get_zalo_response(self, config):
        zalo_api = ZaloAPI(config.app_id, config.secret_key, config.code)
        adapter = Adapter(zalo_api)
        return responseData(adapter)

    @http.route("/callback", type="http", auth="public", website=True)
    def zalo_callback(self, **kwargs):
        oa_id = kwargs.get("oa_id")
        code = kwargs.get("code")

        if not oa_id or not code:
            return http.Response(
                "<html><body><h1>Missing parameters</h1></body></html>",
                status=400,
                content_type="text/html",
            )

        data = initialize_default_data()

        try:
            config_settings = self._update_or_create_config(oa_id, code)
            if config_settings:
                data = self._get_zalo_response(config_settings)
            else:
                data = initialize_default_data(error="Configuration not found")
        except Exception as e:
            _logger.error(f"Error processing Zalo callback: {e}")
            data = initialize_default_data(error=str(e))

        return request.make_response(
            data, headers={"Content-Type": "application/json"}
        )


# # Redirect to the Zalo settings view in res.config.settings
# action = env.ref("zalo.zalo_settings_action")
# return request.redirect("/web#action=%s" % action.id)
