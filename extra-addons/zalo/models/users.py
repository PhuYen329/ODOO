# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class users(models.Model):
    _name = "zalo.users"
    _description = "zalo.users"
    users_id=fields.Integer(string="users_id")
    name = fields.Char("Name", required=True)
    introduces = fields.Text(" Introduces")
    age = fields.Integer("Age", default=1)
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female")], string="Gender", default="male"
    )
    manager_image = fields.Binary(
        "manager Image", attachment=True, help="manager Image"
    )


#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
