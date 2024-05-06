# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class zalo(models.Model):
    _name = "zalo.zalo"
    _description = "zalo.zalo"

    zalo_id = fields.Char(string="Zalo ID")
    secret_id=fields.Char(string='Secret Id') 
    app_id = fields.Char(string="App ID")
    access_token=fields.Char(string='access_token') 

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
