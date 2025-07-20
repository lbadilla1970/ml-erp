from odoo import models, fields


class Descuento(models.Model):
    _name = 'descuento.descuento'
    _description = 'Descuento'
    _inherit = ['mail.thread']

    name = fields.Char(string='Nombre', required=True, tracking=True)
    tipo = fields.Selection([
        ('legal', 'Legal'),
        ('otros', 'Otros')
    ], string='Tipo', tracking=True)
    afecta_liquido = fields.Boolean(string='Afecta Líquido', tracking=True)
    legal = fields.Boolean(string='Legal', tracking=True)
