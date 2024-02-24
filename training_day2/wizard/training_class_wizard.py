from odoo import fields, api, models


class TrainingClassWizard(models.TransientModel):
    _name = 'training.class.wizard'
    _description = 'Training Class Wizard'

    name = fields.Char('Name', required=True)

    def action_change(self):
        records = self.env[self._context.get('active_model')].browse(
            self._context.get('active_ids'))
        records.write({'name': self.name})
