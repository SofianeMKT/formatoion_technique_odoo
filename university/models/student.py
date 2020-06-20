# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityStudent(models.Model):
    _name = 'university.student'

    f_name = fields.Char('Fist name', required=True)
    l_name = fields.Char('Last name', required=True)
    sexe = fields.Selection([('male', 'Male'), ('female', 'Female')], required=True)
    identity_card = fields.Char('Identity card', help="blablabla")
    address = fields.Text('Address', readonly=True, default="Adresse")
    birthday = fields.Date('Birthday')
    registration_date = fields.Datetime('Registration Date')
    email = fields.Char()
    phone = fields.Integer()
