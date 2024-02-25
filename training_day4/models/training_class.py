from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TrainingClass(models.Model):
    _inherit = 'training.class'
    
    second_description = fields.Text('Second Description')
    description = fields.Text('First Description')
    class_type = fields.Selection(required=False)

    def action_confirm(self):
        # Validasi harus ada member
        if not self.member_ids:
            raise ValidationError('Members harus ada minimal 1')
        
        res = super().action_confirm()
        
        # Fill second description
        self.second_description = 'Terkonfirmasi'
        
        return res

class TrainingClass(models.Model):
    _name = 'training.class.copy'
    _inherit = 'training.class'
    
    copy_description = fields.Text('Copy Description')
