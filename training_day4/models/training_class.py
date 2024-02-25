from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TrainingClass(models.Model):
    _name = 'training.class'
    _inherit = ['training.class', 'mail.thread', 'mail.activity.mixin']
    _order = 'number'
    second_description = fields.Text('Second Description')
    description = fields.Text('First Description')
    class_type = fields.Selection(required=False)
    state = fields.Selection(tracking=True)
    number = fields.Char('Number')
    second_number = fields.Char('Second Number')
    third_number = fields.Char('Third Number')

    def action_view_members(self):
        action = self.env['ir.actions.act_window']._for_xml_id(
            'training_day4.training_class_member_action')
        action["domain"] = [("training_id", "=", self.id)]
        return action

    @api.model_create_multi
    def create(self, values):
        res = super().create(values)
        for record in res:
            # create sequence on save
            record.number = self.env['ir.sequence'].next_by_code(
                'training.class')
        return res

    def action_confirm(self):
        # Validasi harus ada member
        if not self.member_ids:
            raise ValidationError('Members harus ada minimal 1')

        res = super().action_confirm()

        # Fill second description
        self.second_description = 'Terkonfirmasi'
        if not self.number:
            self.number = self.env['ir.sequence'].next_by_code(
                'training.class')

        return res


class TrainingClass(models.Model):
    _name = 'training.class.copy'
    _inherit = 'training.class'

    copy_description = fields.Text('Copy Description')
