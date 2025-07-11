# -*- coding: utf-8 -*-
{
    'name': "prma_footer",
    'version': '0.1',
    'author': "JL",
    'website': "https://www.prma-reunion.fr",

    'category': 'Website',

    'summary': """ Custom ODOO Footer """,
    'description': """ Custom ODOO Footer without Odoo """,

    'depends': ['website'],

    'data': [
	'views/website_footer_templates_inherit.xml',
    ],

    'installable': True,
    'application': True,
}
