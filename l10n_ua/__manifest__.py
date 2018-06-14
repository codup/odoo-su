# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014-2018 CodUP (<http://codup.com>).
#
##############################################################################

{
    'name': 'Ukraine - Accounting',
    'version': '3.2',
    'category': 'Localization',
    'description': """
This is the base module to manage the accounting chart for Ukraine in Odoo.
    """,
    'author': 'CodUP',
    'website': 'http://codup.com',
    'depends': ['account'],
    'demo': [],
    'data': [
        'data/account_chart.xml',
        'data/account.account.template.csv',
        'data/account_chart_template.xml',
        'data/account_chart_template.yml',
    ],
    'sequence': 1,
    'installable': True,
}
