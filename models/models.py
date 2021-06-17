from odoo import models, fields


class tasklist(models.Model):
     _name = "task.list"
     name = fields.Char("Nombre")
     status  = fields.Selection([('borrador', 'Borrador'),('hecho', 'Hecho'),('pendiente', 'Pendiente')])