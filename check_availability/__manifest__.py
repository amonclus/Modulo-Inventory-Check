# -*- coding: utf-8 -*-
{
    'name': "check_availability",

    'summary': """
        """,

    'description': """
        
    """,

    "author": "Kayuulab SRL",
    "website": "http://www.kayuulab.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
    'security/ir.model.access.csv',
    'data/ir_sequence_data_inv.xml',
    'data/mail_template_data.xml',
    'data/auto_email.xml',
    'wizard/check_warehouse_availability_views.xml',
    'views/stock_inventory_new_count_views.xml',
    'views/menuitems_check.xml',
    'reports/inventory_check_report.xml',
    'reports/inventory_check_template.xml',


    ],
    'application': True,
    'images':['static/description/icon.png'],

}