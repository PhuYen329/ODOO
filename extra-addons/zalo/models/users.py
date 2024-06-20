# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class ZaloUsers(models.Model):
    _name = "zalo.users"
    _description = "Zalo Users"
    # _inherit = "res.partner"

    users_id = fields.Integer(string="Users ID")

    introduces = fields.Text("Introduces")
    age = fields.Integer("Age", default=1)
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female")], string="Gender", default="male"
    )
    manager_image = fields.Binary(
        "Manager Image", attachment=True, help="Manager Image"
    )


#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
