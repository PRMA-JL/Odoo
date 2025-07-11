# -*- coding: utf-8 -*-
{
    'name': "prma_blog",
    'version': '0.2',
    'author': "JL",
    'website': "https://www.prma-reunion.fr",

    'category': 'Website',

    'summary': """ PRMA Custom ODOO Blogs module """,
    'description': """ PRMA Custom ODOO Blogs module with tag filtering """,

    'depends': ['website_blog', 'website'],

    'data': [
	'views/website_blog_templates_inherit.xml',
	'static/src/xml/snippet.xml',
    ],

    'assets': {
        'website.backend_assets_all_wysiwyg': [
	    'tagged_blog/static/src/js/blog_tag_selector.js',
        ],
        'web.assets_frontend': [
            'tagged_blog/static/src/js/blog_tag_front.js',
        ],
    },

    'installable': True,
    'application': True,
    'license': "LGPL-3",
}
