# -*- coding: utf-8 -*-
from odoo import models, fields


class CustomerFeedbackModel(models.Model):
    _name = 'customer.feedback'
    _description = 'Customer Feedback Details'

    customer_id = fields.Many2one('res.partner', string='Customer')
    feedback_type = fields.Many2one('feedback.type', string='Feedback Type')
    rating = fields.Selection([('5', 'Pleased'), ('4', 'Pleased'), ('3', 'Neutral'), ('2', 'Bad'), ('1', 'Worst')],
                              string='Customer Rating', help="Select the rating given by customer.")
    customer_description = fields.Text(string='Description')


class FeedbackTypeModel(models.Model):
    _name = 'feedback.type'
    _description = 'Feedback types'

    name = fields.Char(string='Name')
