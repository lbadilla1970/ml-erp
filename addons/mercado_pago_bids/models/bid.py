from odoo import fields, models


class MercadoPagoBid(models.Model):
    _name = 'mercado_pago.bid'
    _description = 'Mercado Pago Bid'

    name = fields.Char('Nombre Adquisición')
    numero_adquisicion = fields.Char('Número Adquisición')
    tipo_adquisicion = fields.Char('Tipo Adquisición')
    descripcion = fields.Text('Descripción')
    organismo = fields.Char('Organismo')
    region_compradora = fields.Char('Región Compradora')
    fecha_publicacion = fields.Datetime('Fecha Publicación')
    fecha_cierre = fields.Datetime('Fecha Cierre')
    descripcion_producto_servicio = fields.Char('Descripción del producto/servicio')
    codigo_onu = fields.Char('Código ONU')
    unidad_medida = fields.Char('Unidad de Medida')
    cantidad = fields.Float('Cantidad')
    generico = fields.Char('Genérico')
    nivel_1 = fields.Char('Nivel 1')
    nivel_2 = fields.Char('Nivel 2')
    nivel_3 = fields.Char('Nivel 3')
    estado = fields.Selection([
        ('revisar', 'Por Revisar'),
        ('proceso', 'En Proceso'),
        ('descartada', 'Descartada'),
        ('adjudicada', 'Adjudicada'),
        ('perdida', 'Perdida'),
    ], string='Estado', default='revisar')

    custom_value_ids = fields.One2many('mercado_pago.custom.value', 'bid_id', string='Custom Values')
