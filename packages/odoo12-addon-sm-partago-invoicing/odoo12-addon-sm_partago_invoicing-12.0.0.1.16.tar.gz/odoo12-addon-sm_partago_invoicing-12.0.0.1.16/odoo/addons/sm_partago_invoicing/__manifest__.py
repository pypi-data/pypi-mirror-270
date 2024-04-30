# -*- coding: utf-8 -*-
{
    'name': "sm_partago_invoicing",

    'summary': """
    Module to modify invoices and cs reports for the user""",

    'author': "Som Mobilitat",
    'website': "http://www.sommobilitat.coop",

    'category': 'vertical-carsharing',
    'version': '12.0.0.1.16',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'mail',
        'web',
        'account',
        'sale',
        'product',
        'project',
        'vertical_carsharing',
        'sm_teletacs',
        'sm_connect',
        'sm_partago_db',
        'sm_partago_tariffs',
        'sm_partago_usage',
        'sm_teletacs',
        'sm_rewards'
    ],

    # demo data
    'demo': [
        'demo/demo_data.xml',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'report/contact.xml',
        'report/invoice_report.xml',
        'report/sm_invoice_report.xml',
        'email_tmpl/invoice_email.xml',
        'email_tmpl/invoice_report.xml',
        'email_tmpl/sale_order.xml',
        'views/views.xml',
        'views/views_cs_task.xml',
        'views/views_res_config_settings.xml',
        'views/views_invoice_report.xml',
        'views/views_invoice_report_wizard.xml',
        'views/views_invoice_line.xml',
        'views/views_teletacs.xml',
        'views/views_members.xml',
        'views/views_report_reservation_compute.xml',
        'views/views_batch_reservation_compute.xml',
        'views/views_batch_reservation_compute_wizard.xml',
        'views/views_invoices.xml',
        'views/views_reservation_compute.xml'
    ],
    'qweb': [
        'static/src/xml/base.xml'
    ]
}
