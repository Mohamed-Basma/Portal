from odoo import models, fields,api
from odoo.exceptions import UserError


class KitStages(models.Model):
    _name = 'kit.stages'
    _description = 'Kit Product With 4 Stages'

    name = fields.Char(string="Product", required=True)
    price = fields.Float(
        string='Price', 
        required=False)
    reference = fields.Char(string="Reference", readonly=True)
    quantity = fields.Float(string="Quantity", default=1.0)

    bom_type = fields.Selection([
        ('kit', 'Kit'),
        ('manufacture', 'Manufacture this product')
    ], default='kit', string="BoM Type")

    product_uom_id = fields.Many2one(
        comodel_name='uom.uom',
        string=' product_uom_id',
        required=False)

    stage = fields.Selection([
        ('draft', 'Draft'),
        ('first', 'First Status'),
        ('second', 'Second Status'),
        ('third', 'Third Status'),
        ('forth', 'Forth Status'),
        ('cancel', 'Cancel'),
    ], default='draft', string='Stage')

    component_ids = fields.One2many(
        'kit.component', 'kit_id', string="Components"
    )

    @api.model
    def create(self, vals):
        # الحصول على جميع القيم الصحيحة وتحويلها لأرقام
        records = self.search([])

        # استخراج أكبر رقم موجود
        existing_numbers = []
        for rec in records:
            if rec.reference and rec.reference.isdigit():
                existing_numbers.append(int(rec.reference))

        next_number = max(existing_numbers) + 1 if existing_numbers else 1

        vals['reference'] = str(next_number)
        return super().create(vals)

    def action_draft(self):
        for rec in self:
             rec.stage = 'draft'


    def action_first_stage(self):
        for rec in self:
            rec.stage = 'first'

    def action_second_stage(self):
        for rec in self:
            rec.stage = 'second'

    def action_third_stage(self):
        for rec in self:
            rec.stage = 'third'

    def action_forth_stage(self):
        for rec in self:

            # 🔒 منع الضغط مرة ثانية
            if rec.stage == 'forth':
                raise UserError("This record is already in the 'Forth' stage. You cannot apply it again.")

            # تغيير المرحلة
            rec.stage = 'forth'

            # شرط: لو مفيش اسم → ماينشئش منتج
            if not rec.name:
                raise UserError("Product name is required to create a product.")

            # إنشاء المنتج في Odoo
            self.env['product.product'].create({
                'name': rec.name,
                'list_price': rec.price or 0.0,
                'sale_ok': True,  # ✔ المنتج قابل للبيع
                'available_in_pos': True,  # ✔ يظهر في POS
                'type': 'product',  # ✔ منتج مخزني (مطلوب للـ POS)
            })

    def action_cancel_stage(self):
        for rec in self:
            rec.stage = 'cancel'
