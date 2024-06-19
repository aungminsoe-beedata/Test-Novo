# -*- coding: utf-8 -*-
# from odoo import http


# class NovoCustomization(http.Controller):
#     @http.route('/novo_customization/novo_customization', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/novo_customization/novo_customization/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('novo_customization.listing', {
#             'root': '/novo_customization/novo_customization',
#             'objects': http.request.env['novo_customization.novo_customization'].search([]),
#         })

#     @http.route('/novo_customization/novo_customization/objects/<model("novo_customization.novo_customization"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('novo_customization.object', {
#             'object': obj
#         })

