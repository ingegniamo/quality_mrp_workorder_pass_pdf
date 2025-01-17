from odoo import SUPERUSER_ID, api, fields, models, _
from odoo.exceptions import UserError
from odoo.fields import Command
from odoo.tools import float_compare, float_round, is_html_empty, float_is_zero

class QualityCheck(models.Model):
    _inherit = "quality.check"
    @api.model_create_multi
    def create(self, values):
        for value in values:
            if 'point_id' in value and not value.get('worksheet_document'):
                value['worksheet_document'] = self.env['quality.point'].browse(value['point_id']).worksheet_document
        return super().create(values)