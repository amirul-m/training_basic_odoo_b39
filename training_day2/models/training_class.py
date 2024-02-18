from odoo import models, fields, api

class TrainingClass(models.Model):
    _name = 'training.class'
    _description = 'Training Class'
    
    name = fields.Char(required=True)
    active = fields.Boolean('Aktif', default=True)
    max_person = fields.Integer('Max Peserta')
    duration_hour = fields.Float('Durasi (Jam)')
    class_type = fields.Selection([
        ('beginner', 'Beginner'), ('middle', 'Middle'), ('advance', 'Advance')
    ], string='Tipe', default='beginner', required=True)
    description = fields.Text('Description')
    start_date = fields.Date('Start Date')
    end_datetime = fields.Datetime('End Datetime')
    training_file = fields.Binary('File')
    logo = fields.Image('Logo')
    mentor_id = fields.Many2one('res.partner', string='Mentor')
    tag_ids = fields.Many2many('res.partner.category', string='Tags')
    duration_days = fields.Integer('Durasi (Hari)', compute='_compute_duration_days')

    @api.depends('start_date', 'end_datetime')
    def _compute_duration_days(self):
        for record in self:
            total = 0
            if record.start_date and record.end_datetime:
                total = (record.end_datetime.date() - record.start_date).days
            record.duration_days = total
