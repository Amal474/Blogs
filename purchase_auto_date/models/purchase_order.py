# -*- coding: utf-8 -*-
import datetime
from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    state_update_date = fields.Datetime(
        string='State Updated On', help='State of the record was updated on')

    def action_purchase_date_update(self):
        """Write your automation code in here"""
        self.state_update_date = datetime.datetime.now()
