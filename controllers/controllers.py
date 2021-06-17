# -*- coding: utf-8 -*-
# from odoo import http


# class Tasklist(http.Controller):
#     @http.route('/tasklist/tasklist/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tasklist/tasklist/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tasklist.listing', {
#             'root': '/tasklist/tasklist',
#             'objects': http.request.env['tasklist.tasklist'].search([]),
#         })

#     @http.route('/tasklist/tasklist/objects/<model("tasklist.tasklist"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tasklist.object', {
#             'object': obj
#         })
