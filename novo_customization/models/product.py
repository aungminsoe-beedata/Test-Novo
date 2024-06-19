from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _check_company_auto = True

    brand_name = fields.Char('Brand Name')
