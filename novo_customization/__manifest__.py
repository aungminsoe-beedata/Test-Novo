# -*- coding: utf-8 -*-
{
    'name': "novo_customization",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product','hr','hr_payroll','account','account_accountant','point_of_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/product_template.xml',
        'views/payslip.xml',
        'views/report_payslip_template.xml',
        'views/paper_format.xml',
        'views/sales_invoice.xml',
        'views/sales_invoice_template.xml',
        'views/pos_invoice.xml'
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

