# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class zalo(models.Model):
    _name="zalo.zalo"
    _description = "Prototype inheritance"

    # user_id = fields.Char(string='User ID', required=True)
    # name = fields.Char(string='Name')
    # email = fields.Char(string='Email')
    # phone = fields.Char(string='Phone')
    # avatar = fields.Binary(string='Avatar')
    #     @api.depends('value')


#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
