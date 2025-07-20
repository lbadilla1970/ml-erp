from odoo import models, fields


class Afp(models.Model):
    _name = 'afp.afp'
    _description = 'AFP'
    _inherit = ['mail.thread']

    name = fields.Char(string='Nombre', required=True, tracking=True)
    tasa_afp = fields.Float(string='Tasa AFP', tracking=True)
    tasa_sis = fields.Float(string='Tasa SIS', tracking=True)
    tasa_apv = fields.Float(string='Tasa APV', tracking=True)
