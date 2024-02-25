from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TrainingClass(models.Model):
    _inherit = 'training.class'
    
    second_description = fields.Text('Second Description')
    description = fields.Text('First Description')
    class_type = fields.Selection(required=False)


class TrainingClass(models.Model):
    _name = 'training.class.copy'
    _inherit = 'training.class'
    
    copy_description = fields.Text('Copy Description')
