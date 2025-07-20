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
        """Apply the new state to the selected bids.

        If the wizard is triggered without explicitly selected records but from
        a filtered list, ``active_domain`` will contain the domain to apply. In
        that case we update all bids matching that domain. Otherwise only the
        records in ``active_ids`` are updated.
        """

        domain = self.env.context.get("active_domain")
        if domain and not self.env.context.get("active_ids"):
            bids = self.env["mercado_pago.bid"].search(domain)
        else:
            bids = self.env["mercado_pago.bid"].browse(
                self.env.context.get("active_ids", [])
            )

        bids.write({"estado": self.estado})
        return {"type": "ir.actions.act_window_close"}
