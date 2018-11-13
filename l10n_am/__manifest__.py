# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014-2018 CodUP (<http://codup.com>).
#
##############################################################################

{
    'name': 'Armenia - Accounting',
    'version': '3.2',
    'category': 'Localization',
    'description': """
This is the base module to manage the accounting chart for Armenia in Odoo.
    """,
    'author': 'CodUP',
    'website': 'http://codup.com',
    'depends': ['account'],
    'demo': [],
    'data': [
        'data/account_chart.xml',
        'data/account.account.template.csv',
        'data/account_chart_template.xml',
        'data/account_chart_template_data.xml',
    ],
    'sequence': 1,
    'installable': True,
}
