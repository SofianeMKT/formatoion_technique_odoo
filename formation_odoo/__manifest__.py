# -*- coding: utf-8 -*-
{
    'name': 'Formation Odoo',
    'version': '13.0.1.0.0',
    'summary': """Formation odoo""",
    'author': 'Amira Azeggagh',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
