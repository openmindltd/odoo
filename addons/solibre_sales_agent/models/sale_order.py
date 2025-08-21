from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sales_agent_id = fields.Many2one(
        'res.partner',
        string='Sales Agent',
        # TODO: Add a domain to only show partners that are sales agents
    )
