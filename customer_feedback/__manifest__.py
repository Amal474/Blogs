# -*- coding: utf-8 -*-
{
    'name': "Customer Feedback",
    'version': '1.0',
    'summary': """Record Your Customer feedback""",
    'description': """
        Customer Feedback Module
            -create feedback to customers
    """,
    'author': "My Company",
    'category': 'Test',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/customer_feedback_view.xml',
        'wizard/customer_feedback_wizard.xml',
        'report/report_action.xml',
        'report/customer_feedback_report.xml',
        'report/wizard_report.xml',
    ],
    'application': True,
}
