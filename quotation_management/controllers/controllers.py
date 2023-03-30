# -*- coding: utf-8 -*-
# from odoo import http


# class QuotationManagement(http.Controller):
#     @http.route('/quotation_management/quotation_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quotation_management/quotation_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('quotation_management.listing', {
#             'root': '/quotation_management/quotation_management',
#             'objects': http.request.env['quotation_management.quotation_management'].search([]),
#         })

#     @http.route('/quotation_management/quotation_management/objects/<model("quotation_management.quotation_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quotation_management.object', {
#             'object': obj
#         })
