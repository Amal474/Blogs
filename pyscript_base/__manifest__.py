# -*- coding: utf-8 -*-
{
    'name': "PyScript Base",
    'version': '15.0.1.0',
    'summary': """Sample pyscript to Odoo website""",
    'description': """
        Examples
            -Added print functionality
    """,
    'author': "Mohammed Amal N",
    'category': 'Website/Website',

    # any module necessary for this one to work correctly
    'depends': ['website'],
    'data': [
        'views/pyscript_template.xml',
        'views/website_menu.xml',
    ],
    'application': False,
}
