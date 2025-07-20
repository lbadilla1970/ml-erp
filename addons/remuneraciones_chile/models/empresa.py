from odoo import models, fields


class Empresa(models.Model):
    _name = 'organizacion.empresa'
    _description = 'Empresa'
    _inherit = ['mail.thread']

    name = fields.Char(string='Nombre', required=True, tracking=True)
    rut = fields.Char(string='RUT', tracking=True)
    direccion = fields.Char(string='Dirección', tracking=True)
    giro = fields.Char(string='Giro', tracking=True)
    representante_legal = fields.Char(string='Representante Legal', tracking=True)
    email = fields.Char(string='Email', tracking=True)
    telefono = fields.Char(string='Teléfono', tracking=True)
