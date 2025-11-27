from odoo import models, fields

class KitComponent(models.Model):
    _name = 'kit.component'
    _description = 'Kit Components'

    kit_id = fields.Many2one('kit.stages')

    product_id = fields.Many2one('product.product', string="Component", required=True)
    quantity = fields.Float(string='Quantity', default=1.0)
    uom_id = fields.Many2one('uom.uom', string='Product Unit of Measure')
