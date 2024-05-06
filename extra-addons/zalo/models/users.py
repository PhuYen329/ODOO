# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class Users(models.Model):
    _name = "zalo.users"
    _description = "zalo.users"
    user_id = fields.Char(string='User ID', required=True)
    name = fields.Char(string='Name')
    phone = fields.Char(string='Phone')
    age=fields.Integer(string="Age")