# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityClassroom(models.Model):
    _name = 'university.classroom'

    name = fields.Char()
    code = fields.Integer()

    professor_ids = fields.Many2many('university.professor', 'professor_classroom_rel', 'name', 'f_name')