from odoo import models, fields

class ServiceRequest(models.Model):
    _name = 'service.request'
    _description = 'Service Request'

    name = fields.Char(string="Request Title", required=True)
    description = fields.Text(string="Description")
    partner_id = fields.Many2one('res.partner', string="Customer", required=True)
    state = fields.Selection([('draft', 'Draft'), ('done', 'Done')], default='draft')