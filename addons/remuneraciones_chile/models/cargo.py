from odoo import models, fields


class Cargo(models.Model):
    _name = 'organizacion.cargo'
    _description = 'Cargo'
    _inherit = ['mail.thread']

    name = fields.Char(string='Nombre', required=True, tracking=True)
    unidad_id = fields.Many2one('organizacion.unidad', string='Unidad', tracking=True, ondelete='cascade')
    nivel = fields.Char(string='Nivel', tracking=True)
    sueldo_base_estimado = fields.Float(string='Sueldo Base Estimado', tracking=True)
