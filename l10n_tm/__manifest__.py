# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014-2018 CodUP (<http://codup.com>).
#
##############################################################################

{
    'name': 'Turkmenistan - Accounting',
    'version': '3.1',
    'category': 'Localization',
    'description': """
This is the base module to manage the accounting chart for Turkmenistan in OpenERP.
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
