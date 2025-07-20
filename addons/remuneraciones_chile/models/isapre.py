from odoo import models, fields


class Isapre(models.Model):
    _name = 'isapre.isapre'
    _description = 'Isapre'
    _inherit = ['mail.thread']

    name = fields.Char(string='Nombre', required=True, tracking=True)
    valor_plan_base = fields.Float(string='Valor Plan Base', tracking=True)
    tipo_cobro = fields.Selection([
        ('porcentaje', 'Porcentaje'),
        ('monto_fijo', 'Monto Fijo')
    ], string='Tipo Cobro', tracking=True)
