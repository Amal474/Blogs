# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class CustomerFeedbackWizardReport(models.AbstractModel):
    _name = 'report.customer_feedback.wizard_report_template'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['customer.feedback'].search([('customer_id', '=', data['data']['customer_id'][0])])
        return {
            'doc_model': 'customer.feedback',
            'docs': docs,
        }
