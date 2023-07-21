from odoo import fields, models
from odoo.exceptions import ValidationError


class CheckWarehouseAvailabilityWizard(models.TransientModel):
    _name = 'wizard.check_warehouse_availability'
    _description = 'Selects fields which need inventory checks'

    requested_by_id = fields.Many2one('res.users', 'Requested by', default=lambda self: self.env.user)
    assigned_to_id = fields.Many2one('res.users', 'Assigned to')
    product_ids = fields.Many2many('product.product')
    done_by_date = fields.Date(string="Must be done by", default=fields.Datetime.now)
    requested_date = fields.Date(default=fields.Datetime.now)
    name = fields.Char()

    def action_availability(self):
        vals = {
            'name': self.name,
            'done_by_date': self.done_by_date,
            'requested_by_id': self.requested_by_id.id,
            'state': 'new',
            'requested_date': self.requested_date,
            'product_ids': self.product_ids,
            'assigned_to_id': self.assigned_to_id.id,
        }
        vals['name'] = self.env['ir.sequence'].next_by_code(
            'stock.check')

        return self.env['stock.new_count'].create(vals)


