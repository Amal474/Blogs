# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleXLSWizard(models.TransientModel):
    _name = 'sale.xls.wizard'

    date_end = fields.Date(string='End Date')
    date_start = fields.Date(string='Start Date')

    @api.multi
    def action_create_report(self):
        context = dict(self._context)
        if context is None:
            context = {}
        data = self.read()[0] or {}
        datas = {
            'ids': self._ids,
            'data': data,
            'model': 'sale.xls.wizard'
        }
        return self.env.ref(
            'sale_report_xls.sale_xls_report'
        ).report_action(self, data=datas)
