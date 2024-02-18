# -*- coding: utf-8 -*-
# from odoo import http


# class ProjectTaskPurchase(http.Controller):
#     @http.route('/project_task_purchase/project_task_purchase', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_task_purchase/project_task_purchase/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_task_purchase.listing', {
#             'root': '/project_task_purchase/project_task_purchase',
#             'objects': http.request.env['project_task_purchase.project_task_purchase'].search([]),
#         })

#     @http.route('/project_task_purchase/project_task_purchase/objects/<model("project_task_purchase.project_task_purchase"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_task_purchase.object', {
#             'object': obj
#         })

