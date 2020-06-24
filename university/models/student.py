# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityStudent(models.Model):
    _name = 'university.student'

    f_name = fields.Char(string='Fist name', required=True)
    l_name = fields.Char('Last name', required=True)
    sexe = fields.Selection([('male', 'Male'), ('female', 'Female')], required=True)
    identity_card = fields.Char('Identity card', help="blablabla")
    address = fields.Text('Address', readonly=True, default="Adresse")
    birthday = fields.Date('Birthday')
    registration_date = fields.Datetime('Registration Date')
    email = fields.Char()
    phone = fields.Integer()

    departement_id = fields.Many2one('university.department', 'Department')
    classroom_id = fields.Many2one('university.classroom')

    subject_ids = fields.One2many('university.subject', 'student_id')


