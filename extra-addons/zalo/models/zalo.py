# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class zalo(models.Model):
    _name = "zalo.zalo"
    _description = "zalo.zalo"

    zalo_id = fields.Integer(string="zalo_id")


#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
