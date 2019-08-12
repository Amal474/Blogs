# -*- coding: utf-8 -*-
{
    'name': 'Sale Report XLS',
    'summary': 'Generate XLS report for sale order',
    'version': '12.0.1.0.0',
    'category': 'Sales',
    'website': 'https://www.abrusnetworks.com',
    'images': ['static/description/banner.jpg'],
    'author': 'Abrus Networks',
    'company': 'Abrus Networks',
    'maintainer': 'Abrus Networks',
    'installable': True,
    'depends': [
        'base',
        'sale',
        'sale_management',
        'report_xlsx',
    ],
    'data': [
        'report/templates.xml',
        'wizard/sale_xls_wizard.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
