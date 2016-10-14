﻿# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014-2016 CodUP (<http://codup.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Uzbekistan - Accounting',
    'version': '3.0',
    'category': 'Localization',
    'description': """
This is the base module to manage the accounting chart for Uzbekistan in OpenERP.
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
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: