# -*- coding: utf-8 -*-
# from odoo import http


# class Zalo(http.Controller):
#     @http.route('/zalo/zalo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zalo/zalo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('zalo.listing', {
#             'root': '/zalo/zalo',
#             'objects': http.request.env['zalo.zalo'].search([]),
#         })

#     @http.route('/zalo/zalo/objects/<model("zalo.zalo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zalo.object', {
#             'object': obj
#         })

