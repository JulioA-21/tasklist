from os import name
from odoo import models,fields,api

class Wizard(models.TransientModel):
    _name = "tasklist.odoo"

    status_ids  = fields.Selection([('borrador', 'Borrador'),('hecho', 'Hecho'),('pendiente', 'Pendiente')])
    task_id = fields.Many2one(
        'task.list',
        string='Tasks',
        )
    def update_status(self):
        print(self.status_ids)
        tasks_ids = self._context.get('active_ids')
        if self._context.get('active_model') == 'task.list' and self._context.get('active_ids', False):
            task = self.env['task.list'].browse(self._context.get('active_ids'))
            for e in task:
                e.status = self.status_ids
