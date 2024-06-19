from odoo import api, fields, models

class PosSession(models.Model):
    _inherit = 'pos.session'

    def _change_display_name(self, products):
        for product in products:
            default_code = product['default_code']
            if default_code:
                product['display_name'] = product['display_name'] + " " + default_code

    def _process_pos_ui_product_product(self, products):
        super(PosSession, self)._process_pos_ui_product_product(products)
        self._change_display_name(products)

