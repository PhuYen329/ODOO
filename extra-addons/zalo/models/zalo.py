# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class zalo(models.Model):
    _name = "zalo.zalo"
    _inherit = 'res.config.settings'
    _description = "Prototype inheritance"

    app_id = fields.Char(string='App ID', required=True)
    secret_key = fields.Char(string='Secret Key', required=True)



#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
