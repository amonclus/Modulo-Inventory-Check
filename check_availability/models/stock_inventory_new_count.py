from odoo import fields, models


class StockNewCount(models.Model):
    _name = 'stock.new_count'
    _description = 'Stock updated count'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    assigned_to_id = fields.Many2one('res.users', 'Assigned to')
    counted_amount = fields.Integer('product.product')
    name = fields.Char()
    requested_by_id = fields.Many2one('res.users', 'Requested by: ', default=lambda self: self.env.user)
    done_by_date = fields.Date(string="Must be done by: ", default=fields.Datetime.now)
    state = fields.Selection([('new', 'New'), ('counting', 'Counting'), ('done', 'Done')], string='Status', default='new', required=True)
    requested_date = fields.Date(default=fields.Datetime.now)
    product_ids = fields.Many2many('product.product')
    finished_date = fields.Date(string="Finished date")
    comments = fields.Char(string="Comments")

    def action_new_count(self):
        return

    def action_send_inventory_check(self):
        template_id = self.env.ref('check_availability.view_check_availability_mail_template').id
        template_ = self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)
        return

    def send_recurring_mail(self):
        template_id = self.env.ref('check_availability.view_availability_reminder_template').id
        self.env['mail.template'].browse(template_id).send_mail(self.id, force_send=True)
        return
