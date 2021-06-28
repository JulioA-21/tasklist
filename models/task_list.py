from odoo import models, fields


class TaskList(models.Model):
     _name = "task.list"
     name = fields.Char("Nombre")
     status  = fields.Selection([('draft', 'Draft'),('done', 'Done'),('pending', 'Pending')])
     in_charge_id = fields.Many2one('hr.employee',string='A cargo')
     
     def action_btn_done(self):
          self.status = 'done'
     def action_btn_draft(self):
          self.status = 'draft'
     def action_btn_pending(self):
          self.status = 'pending'