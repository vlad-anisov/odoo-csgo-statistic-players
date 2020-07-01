# -*- coding: utf-8 -*-
{
    'name': "csgo_player_statistic",

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
    'depends': ['base', 'website',],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/stats.xml',
        'reports/report.xml',
        'reports/report_player.xml',
    ],
    'application':True,
    'post_init_hook': 'load_players',
    "external_dependencies": {
        'python': ['beautifulsoup4', 'bs4', 'python-utils', 'six']
    }
}
