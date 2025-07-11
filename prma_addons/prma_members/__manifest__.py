# -*- coding: utf-8 -*-
{
    'name': "prma_members",
    'version': '0.1',
    'author': "JL",
    'website': "https://www.prma-reunion.fr",

    'category': 'Website',

    'summary': """ Custom ODOO Members module """,
    'description': """ Custom ODOO Members module without left column and displaying for unlogged user """,

    'depends': ['website_membership', 'website', 'membership'],

    'data': [
	'views/website_members_templates_inherit.xml',
    ],

    'installable': True,
    'application': True,
}
