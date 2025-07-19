from odoo import models, fields


class ChangeBidStateWizard(models.TransientModel):
    _name = 'mercado_pago.change.state.wizard'
    _description = 'Change Bid State Wizard'

    estado = fields.Selection(
        selection=lambda self: self.env['mercado_pago.bid']._fields['estado'].selection,
        string='Nuevo Estado',
        required=True
    )

    def action_confirm(self):
        bids = self.env['mercado_pago.bid'].browse(self.env.context.get('active_ids', []))
        bids.write({'estado': self.estado})
        return {'type': 'ir.actions.act_window_close'}
