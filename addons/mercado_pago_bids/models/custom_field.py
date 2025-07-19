from odoo import fields, models


class MercadoPagoCustomField(models.Model):
    _name = 'mercado_pago.custom.field'
    _description = 'Custom Field Definition'
    _rec_name = 'name'

    name = fields.Char('Field Name', required=True)


class MercadoPagoCustomValue(models.Model):
    _name = 'mercado_pago.custom.value'
    _description = 'Custom Field Value'

    bid_id = fields.Many2one('mercado_pago.bid', string='Bid', ondelete='cascade')
    field_id = fields.Many2one('mercado_pago.custom.field', string='Field', required=True)
    value = fields.Char('Value')
