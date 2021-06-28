from os import name
from odoo import models,fields

class TaskListWizard(models.TransientModel):
    _name = "task.list.wizard"
    status_ids  = fields.Selection([('draft', 'Draft'),('done', 'Done'),('pending', 'Pending')])
    task_id = fields.Many2one(
        'task.list',
        string='Tasks',
        )

    def update_status(self):
        print(self.status_ids)
        tasks_ids = self._context.get('active_ids')
        if self._context.get('active_model') == 'task.list' \
                and self._context.get('active_ids', False):
            task = self.env['task.list'].browse(self._context.get('active_ids'))
            for e in task:
                e.status = self.status_ids
