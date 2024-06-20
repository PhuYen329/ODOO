from odoo import models, fields, api
from urllib.parse import quote  # Import quote from urllib.parse
import os

class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    app_id = fields.Char(string="App ID", required=True, default="2384973300557904521")
    secret_key = fields.Char(
        string="Secret Key", required=True, default="R2NTAje3DhfINJVYVs43"
    )
    redirect_uri = fields.Char(
        string="Redirect URI",
        required=True,
        default="http://localhost:8069/callback",
    )
    oa_id = fields.Char(string="OA ID")
    code = fields.Char(string="Code")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        IrConfigParam = self.env["ir.config_parameter"].sudo()
        res.update(
            app_id=IrConfigParam.get_param("zalo.app_id", default=""),
            secret_key=IrConfigParam.get_param("zalo.secret_key", default=""),
            redirect_uri=IrConfigParam.get_param("zalo.redirect_uri", default=""),
            oa_id=IrConfigParam.get_param("zalo.oa_id", default=""),
            code=IrConfigParam.get_param("zalo.code", default=""),
        )
        return res

    def execute(self):
        super(ResConfigSettings, self).execute()
        self.env["ir.config_parameter"].sudo().set_param("zalo.app_id", self.app_id)
        self.env["ir.config_parameter"].sudo().set_param(
            "zalo.secret_key", self.secret_key
        )
        self.env["ir.config_parameter"].sudo().set_param(
            "zalo.redirect_uri", self.redirect_uri
        )
        base_url = os.getenv("URL_API_ZALO")
        # Use quote function properly
        url = f"{base_url}/oa/permission?app_id={self.app_id}&redirect_uri={quote(self.redirect_uri)}"
        return {
            "type": "ir.actions.act_url",
            "url": url,
            "target": "self",
        }
