{
    'name': 'E-Commerce',
    'category': 'Website',
    'summary': 'Sell Your Products Online',
    'version': '1.0',
    'description': """
OpenERP E-Commerce
==================

        """,
    'author': 'OpenERP SA',
    'depends': ['website', 'sale', 'point_of_sale'],
    'data': [
        'views/website_sale.xml',
        'security/ir.model.access.csv',
        'security/website_sale.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
}
