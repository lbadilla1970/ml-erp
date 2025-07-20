from odoo import models, fields


class Unidad(models.Model):
    _name = 'organizacion.unidad'
    _description = 'Unidad'
    _inherit = ['mail.thread']

    name = fields.Char(string='Nombre', required=True, tracking=True)
    empresa_id = fields.Many2one('organizacion.empresa', string='Empresa', tracking=True, ondelete='cascade')
