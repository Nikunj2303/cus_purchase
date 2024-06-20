from odoo import models, api


class CustomInvoice(models.Model):
    _inherit = 'account.move'

    def post_invoice(self):
        for move in self:
            if move.custom_posted_status == 'posted':
                raise UserError('This invoice is already posted.')
            #
            # # Call the super method to perform the standard post operation
            # res = super(AccountMove, self).post()
            #
            # # Update the custom posted status
            # move.custom_posted_status = 'posted'
        return res
