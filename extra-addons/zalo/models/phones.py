# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class phones(models.Model):
    _name = "zalo.phones"
    _description = "zalo.phones"
    users_id=fields.Integer(string="users_id")
    zalo_id = fields.Integer(string="zalo_id")
    phone = fields.Text("Phone Number")


#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
