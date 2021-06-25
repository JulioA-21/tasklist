from odoo import models, fields


class tasklist(models.Model):
     _name = "task.list"
     def action_btn_done(self):
          self.status = 'hecho'
     name = fields.Char("Nombre")
     status  = fields.Selection([('borrador', 'Borrador'),('hecho', 'Hecho'),('pendiente', 'Pendiente')])
     in_charge_id = fields.Many2one('hr.employee',string='A cargo')