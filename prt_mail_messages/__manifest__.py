# -*- coding: utf-8 -*-
{
    'name': 'Mail Messages Easy.'
            ' Show all messages, Show sent messages, Reply to message, Forward message, Quote message, Move message'
            ' Email client style for messages views and more',
    'version': '12.0.1.0',
    'summary': """Read and manage all Odoo messages in one place!""",
    'author': 'Ivan Sokolov',
    'category': 'Sales',
    'license': 'GPL-3',
    'website': 'https://demo.cetmix.com',
    'description': """
 Show all messages, Show sent message, Reply to messages, Forward messages, Move messages, Quote messages
""",
    'depends': ['base', 'mail'],
    'live_test_url': 'https://demo.cetmix.com',
    'images': ['static/description/banner.png'],

    'data': [
        'security/groups.xml',
        'views/prt_mail.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
