from odoo import models, fields


class ParametrosMes(models.Model):
    _name = 'parametros.mes'
    _description = 'Parámetros del Mes'
    _inherit = ['mail.thread']

    mes = fields.Selection([
        ('1', 'Enero'), ('2', 'Febrero'), ('3', 'Marzo'),
        ('4', 'Abril'), ('5', 'Mayo'), ('6', 'Junio'),
        ('7', 'Julio'), ('8', 'Agosto'), ('9', 'Septiembre'),
        ('10', 'Octubre'), ('11', 'Noviembre'), ('12', 'Diciembre')
    ], string='Mes', required=True, tracking=True)
    ano = fields.Integer(string='Año', required=True, tracking=True)
    utm = fields.Float(string='UTM', tracking=True)
    ipc = fields.Float(string='IPC', tracking=True)
    sueldo_minimo = fields.Float(string='Sueldo Mínimo', tracking=True)
    tope_imponible = fields.Float(string='Tope Imponible', tracking=True)
    fecha_inicio = fields.Date(string='Fecha Inicio', tracking=True)
    fecha_termino = fields.Date(string='Fecha Término', tracking=True)
