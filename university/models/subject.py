# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversitySubject(models.Model):
    _name = 'university.subject'

    name = fields.Char()
    code = fields.Char()

    student_id = fields.Many2one('university.student')