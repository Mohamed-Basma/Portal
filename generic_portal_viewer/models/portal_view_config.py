from odoo import models, fields

class PortalViewConfig(models.Model):
    _name = 'portal.view.config'
    _description = 'Portal View Configuration'

    name = fields.Char(string="Page Title", required=True)
    model_name = fields.Char(string="Model Name", required=True)
    active = fields.Boolean(default=True)