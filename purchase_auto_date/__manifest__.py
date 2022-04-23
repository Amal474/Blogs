# -*- coding: utf-8 -*-
{
    'name': "Purchase Base Automation Sample",
    'version': '15.0.1.0',
    'summary': """Automatic update of notes in purchase""",
    'description': """
        Purchase Base Automation Sample
            -Automatic update of notes in purchase
    """,
    'author': "Mohammed Amal N",
    'category': 'Test',

    # any module necessary for this one to work correctly
    'depends': ['base_automation', 'purchase'],
    'data': [
        'data/data_server_action.xml',
        'data/base_automation.xml',
        'views/purchase_order_views.xml',
    ],
    'application': False,
}
