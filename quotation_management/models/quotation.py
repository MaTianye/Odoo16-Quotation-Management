# -*- coding: utf-8 -*-

from odoo import models, fields, api


class QuotationManagement(models.Model):
    _name = 'quotation.management'
    _description = 'Manage Quotation Records'
    #
    mpn = fields.Char(string='MPN')
    description = fields.Text(string='Product Description')
    # value = fields.Integer()
    # latest_price = fields.Float('Latest Price', compute="_value_pc", store=True)
    price = fields.Float(string='Price', store=True)
    available_units = fields.Integer(string='Available Units', store=True)
    quotation_ids = fields.Char(string='Quotation')
    supplier_ids = fields.Char(string='Supplier')
    create_date = fields.Datetime(string='Create Date')

    #
    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
    def action_open_quotations_info_wizard(self):
        return {
            'name': 'Quotation Information',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'quotations.info.wizard',
            'target': 'new',
            'context': {'active_id': self.id},
        }
