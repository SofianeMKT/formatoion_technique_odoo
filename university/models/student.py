# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import ValidationError


class UniversityStudent(models.Model):
    _name = 'university.student'

    f_name = fields.Char(string='Fist name', required=True)
    l_name = fields.Char('Last name', required=True)
    sexe = fields.Selection([('male', 'Male'), ('female', 'Female')], required=True)
    identity_card = fields.Char('Identity card', help="blablabla")
    address = fields.Text('Address', readonly=True, default="Adresse")
    birthday = fields.Date('Birthday')
    registration_date = fields.Date('Registration Date')
    email = fields.Char()
    phone = fields.Integer()
    age = fields.Integer()
    state = fields.Selection([('non_enregistrer', 'Non enregistrer'), ('enregistrer', 'Enregistrer')], default= "non_enregistrer")

    departement_id = fields.Many2one('university.department', 'Department')
    classroom_id = fields.Many2one('university.classroom')

    subject_ids = fields.One2many('university.subject', 'student_id')

    api.constrains('registration_date', 'birthday')
    def check_regis(self):
        if self.birthday > self.registration_date:
            raise ValueError("ffff")

    def enregistrer(self):
        if self.sexe == 'female':
            self.state = 'enregistrer'
        else:
            raise ValidationError("This Course is open just for ladies, sorry")

    def annuler(self):
        self.state = 'non_enregistrer'
