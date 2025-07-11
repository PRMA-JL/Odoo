# -*- coding: utf-8 -*-
{
    'name': "prma_event",
    'version': '1.0',
    'author': "JL",
    'website': "https://www.prma-reunion.fr",

    'category': 'Website/Event',

    'summary': """ Hide register button if max attendees is zero """,
    'description': """ Overrides the registration template to hide the button when max attendees = 0 """,

    'depends': ['website_event'],

    'data': [
        'views/event_registration_template_inherit.xml',
    ],

    'installable': True,
    'application': True,
    'license': "LGPL-3",
}
