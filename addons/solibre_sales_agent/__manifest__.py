{
    'name': 'Solibre Sales Agent',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Adds a sales agent to the sales order.',
    'description': """
This module adds a many2one field to link a sales agent (res.partner) to a sales order.
    """,
    'depends': ['sale'],
    'data': [
        'views/sale_order_view.xml',
        'reports/sale_order_report.xml',
    ],
    'installable': True,
    'application': False,
}
