from odoo import models, fields


class TablaImpuesto(models.Model):
    _name = 'tabla.impuesto'
    _description = 'Tabla Impuesto'
    _inherit = ['mail.thread']

    tramo = fields.Integer(string='Tramo', required=True, tracking=True)
    desde = fields.Float(string='Desde', tracking=True)
    hasta = fields.Float(string='Hasta', tracking=True)
    factor = fields.Float(string='Factor', tracking=True)
    rebaja = fields.Float(string='Rebaja', tracking=True)
    tasa = fields.Float(string='Tasa', tracking=True)
