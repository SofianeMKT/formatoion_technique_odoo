# -*- coding: utf-8 -*-

from odoo import models, fields, api


class training_test(models.Model):
     _name = 'formation.odoo'
     _description = 'Odoo formation'

     name = fields.Char()
     date = fields.Char()


