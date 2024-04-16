# -*- coding: utf-8 -*-
# from odoo import http


# class ZaloTest(http.Controller):
#     @http.route('/zalo_test/zalo_test', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zalo_test/zalo_test/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('zalo_test.listing', {
#             'root': '/zalo_test/zalo_test',
#             'objects': http.request.env['zalo_test.zalo_test'].search([]),
#         })

#     @http.route('/zalo_test/zalo_test/objects/<model("zalo_test.zalo_test"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zalo_test.object', {
#             'object': obj
#         })

