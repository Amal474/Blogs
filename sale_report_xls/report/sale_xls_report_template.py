# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from odoo import models


class PartnerXlsx(models.AbstractModel):
    _name = 'report.sale_report_xls.sale_xls_report_template'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, model):
        domain = []

        # Formats
        grey_format = workbook.add_format({
            'bg_color': '#b2beb5'
        })
        grey_border_format = workbook.add_format({
            'bg_color': '#b2beb5',
            'bottom': 1,
        })
        grey_bold_format = workbook.add_format({
            'bg_color': '#b2beb5',
            'bold': True,
        })

        # Worksheet
        sheet = workbook.add_worksheet('Payroll Details')

        sheet.set_row(0, None, grey_format)
        sheet.set_row(1, None, grey_format)
        sheet.set_row(2, None, grey_border_format)
        sheet.set_column(0, 0, 30)
        sheet.set_column(1, 1, 40)

        sheet.write(0, 0, 'Sale Order Details', grey_bold_format)
        sheet.write(1, 0, 'Company', grey_bold_format)
        sheet.write(1, 1, 'Your Company', grey_format)
        sheet.write(2, 0, 'Run Date & User :', grey_bold_format)
        user_date = str((datetime.today()
                         + timedelta(hours=4)).strftime("%d-%b-%Y %H:%M: %S"))\
            + ', ' \
            + str(self.env.user.name)
        sheet.write(2, 1, user_date, grey_border_format)

        # Sale Order table headers
        sheet.write(4, 0, 'Sale Order', grey_bold_format)
        sheet.write(4, 1, 'Customer', grey_bold_format)
        sheet.write(4, 2, 'Total', grey_bold_format)

        if data['data']['date_start']:
            domain.append(('date_order', '>=', data['data']['date_start']))
        if data['data']['date_end']:
            domain.append(('date_order', '<=', data['data']['date_end']))
        sale_order_ids = self.env['sale.order'].search(domain, limit=10)
        row = 5

        # Sale Order Table Content
        for sale_id in sale_order_ids:
            sheet.write(row, 0, sale_id.name)
            sheet.write(row, 1, sale_id.partner_id.name)
            sheet.write(row, 2, sale_id.amount_total)
            row += 1
