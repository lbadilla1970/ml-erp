from odoo import models, fields


class Haber(models.Model):
    _name = 'haber.haber'
    _description = 'Haber'
    _inherit = ['mail.thread']

    name = fields.Char(string='Nombre', required=True, tracking=True)
    tipo = fields.Selection([
        ('imponible', 'Imponible'),
        ('no_imponible', 'No Imponible')
    ], string='Tipo', tracking=True)
    afecta_prevision = fields.Boolean(string='Afecta Previsión', tracking=True)
    afecta_sueldo_liquido = fields.Boolean(string='Afecta Sueldo Líquido', tracking=True)
