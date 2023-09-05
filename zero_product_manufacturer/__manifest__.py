{
    'name': 'Product Manufacturer Managment',
    'version': '5.1.0',
    'category': 'Purchases',
    "author": 'Zero Systems',
    "company": 'Zero for Information Systems',
    "website": "https://www.erpzero.com",
    "email": "sales@erpzero.com",
    "sequence": 0,
    'license': 'OPL-1',
    'live_test_url': 'https://www.youtube.com/playlist?list=PLXFpENL3b6WU9TzMdawrHJsUBqMDXkcbn',
    'summary': 'Adds manufacturers and attributes on the product view',
    "description": """Adds manufacturers and attributes on the product view
    """,
    'depends': ['base','product','purchase'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/view.xml',

    ],
    "price": 35.00,
    "currency": 'EUR',
    'installable': True,
    'auto_install': False,
    "application": True,
    'images': ['static/description/product_manufacturer.png'],
    'pre_init_check_vers': 'pre_init_check_vers',
}

