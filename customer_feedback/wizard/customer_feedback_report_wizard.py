# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CustomerFeedbackReportWizard(models.TransientModel):
    _name = 'customer.feedback.report.wizard'
    _description = 'Customer Feedback Report Wizard'

    customer_id = fields.Many2one('res.partner', string='Customer')

    @api.multi
    def print_report(self):
        context = dict(self._context)
        if context is None:
            context = {}
        data = self.read()[0] or {}
        datas = {
            'ids': self._ids,
            'data': data,
            'model': 'customer.feedback.report.wizard'
        }
        print('datas: ', datas)
        return self.env.ref('customer_feedback.action_customer_feedback_wizard_report').report_action(self, data=datas)
