# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.



from odoo import api, fields, models, _
from odoo.exceptions import UserError



class claseunefa(models.Model):
    _name = "clase.unefa"
    

    name = fields.Char(string='Estudiante', required=True, readonly=False,)
    partner_id = fields.Many2one('res.partner', string='Cliente',)
    semestre_id = fields.Many2one('clase.semestre', string='Semestre',)
    
    materias = fields.One2many('clase.materias', 'unefa_id', string='Order Lines', )

    
    
    
class claseunefa1(models.Model):
    _name = "clase.semestre"
    

    name = fields.Char(string='Semestre', required=True, readonly=False,)
    
class claseunefa2(models.Model):
    _name = "clase.materias"
    

    name = fields.Char(string='Materias', required=True, readonly=False,)
    uc = fields.Char(string='Unidades', required=True, readonly=False,)
    
    unefa_id = fields.Many2one('clase.unefa"', string='Unefa',)
   
