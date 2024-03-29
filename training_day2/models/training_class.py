from odoo import models, fields, api
from odoo.exceptions import ValidationError

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
    phone_mentor_id = fields.Char('Phone', related='mentor_id.phone')
    member_ids = fields.One2many('training.class.member', 'training_id', string='Members')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Cancelled')
    ], string='Status', default='draft')

    def action_confirm(self):
        self.state = 'confirm'
    
    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'
    
    def action_call_wizard(self):
        return {
            'name': 'Change',
            'res_model': 'training.class.wizard',
            'view_mode': 'form',
            'views': [[False, 'form']],
            'context': {
                'active_model': self._name,
                'active_ids': self.ids,
            },
            'target': 'new',
            'type': 'ir.actions.act_window',
        }
    
    def unlink(self):
        for rec in self:
            if rec.state != 'draft':
                raise ValidationError('Dokumen hanya bisa dihapus ketika draft')
        return super(TrainingClass, self).unlink()

    @api.depends('start_date', 'end_datetime')
    def _compute_duration_days(self):
        for record in self:
            total = 0
            if record.start_date and record.end_datetime:
                total = (record.end_datetime.date() - record.start_date).days
            record.duration_days = total

    @api.constrains('name', 'class_type')
    def _constrains_name_class_type(self):
        if self.name and self.class_type:
            records = self.search([('name', '=', self.name), ('class_type', '=', self.class_type), ('id', '!=', self.id)])
            if records:
                raise ValidationError('Sudah ada Training Class dengan Nama dan Tipe yang sama')

    @api.constrains('mentor_id', 'start_date')
    def _constrains_mentor_start(self):
        if self.mentor_id and self.start_date:
            records = self.search([('mentor_id', '=', self.mentor_id.id), ('start_date', '=', self.start_date), ('id', '!=', self.id)])
            if records:
                raise ValidationError('Sudah ada Training Class dengan Mentor tsb di hari yang sama')
    
    @api.onchange('mentor_id', 'start_date', 'end_datetime')
    def _onchange_for_description(self):
        self.description = f"Mentor: {self.mentor_id.name}\nStart Date: {self.start_date}\nEnd Datetime: {self.end_datetime}"


class TrainingClassMember(models.Model):
    _name = 'training.class.member'

    name = fields.Char('Nama Peserta')
    hadir = fields.Boolean('Kehadiran', default=True)
    training_id = fields.Many2one('training.class', string='Training')
