# -*- coding: utf-8 -*-
import random
from odoo import models, fields


class IrModuleAddonsPath(models.Model):
    _name = "ir.module.addons.path"

    name = fields.Char(string='Short Name')
    path = fields.Char(string='Path')
    path_temp = fields.Char(string='Path')
    module_ids = fields.One2many('ir.module.module', 'addons_path_id')
    module_count = fields.Integer(compute='_compute_module_count')

    def _compute_module_count(self):
        for rec in self:
            rec.module_count = len(rec.module_ids)

    def open_apps_view(self):
        self.ensure_one()

        return {'type': 'ir.actions.act_window',
                'name': 'Apps',
                'view_mode': 'kanban,tree,form',
                'res_model': 'ir.module.module',
                'context': {},
                'domain': [('addons_path_id', '=', self.id)],
                }
