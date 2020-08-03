# -*- coding: utf-8 -*-
{
    'name': "hospital_patient",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'mail','board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
#        'views/views.xml',
        'wizard/create_appointment.xml',
        'views/patient.xml',
        'views/appointment.xml',
        'views/doctor.xml',
        'views/lab.xml',
        'views/sale_order.xml',
        'views/settings.xml',
        'views/dashboard.xml',
        'report/patient_card.xml',
        'report/report.xml',
        'report/appointment.xml',
        'report/sale_report_inherit.xml',
        'data/mail_template.xml',
        'data/cron.xml',
        'views/server_action.xml',        
        
#        'views/templates.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
#        'demo/demo.xml',
    ],
}
