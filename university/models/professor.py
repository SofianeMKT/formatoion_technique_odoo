# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityProfessor(models.Model):
    _name = 'university.professor'

    f_name = fields.Char('Fist name')
    l_name = fields.Char('Last name')
    sexe = fields.Selection([('male','Male'), ('female','Female')])
    identity_card = fields.Char('Identity card')
    address = fields.Text('Address')
    birthday = fields.Date('Birthday')
    start_date = fields.Datetime('Start date')
    email = fields.Char()
    phone = fields.Integer()

    #seance des smart button
    active = fields.Boolean()
    #Seance de domaines
    code = fields.Integer(default=3)
    department_id = fields.Many2one('university.department', domain="[('code', '=', code)]")
    classroom_ids = fields.Many2many('university.classroom', 'professor_classroom_rel', 'f_name', 'name', domain="[('code', '=', code)]")