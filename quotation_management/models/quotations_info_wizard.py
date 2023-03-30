# -*- coding: utf-8 -*-

from odoo import models, fields, api


class QuotationsInfoWizard(models.TransientModel):
    _name = 'quotations.info.wizard'
    _description = 'Quotations Info Wizard'

    Info_mpn = fields.Char(string='MPN')
    all_suppliers = fields.Text('All Suppliers', readonly=True)
    latest_price = fields.Float('Latest Price', readonly=True)
    all_quotationIDs = fields.Text('All Quotations No.', readonly=True)

    @api.model
    def default_get(self, fields_list):
        res = super(QuotationsInfoWizard, self).default_get(fields_list)
        quotation = self.env['quotation.management'].browse(self._context.get('active_id'))

        # Find all suppliers
        all_suppliers = self.env['quotation.management'].search([('mpn', '=', quotation.mpn)]).mapped('supplier_ids')
        supplier_names = ', '.join(all_suppliers)

        # Find the latest price
        latest_price = self.env['quotation.management'].search([('mpn', '=', quotation.mpn)], order='price asc',
                                                               limit=1).price

        # Find all quotations
        all_quotations = self.env['quotation.management'].search([('mpn', '=', quotation.mpn)]).mapped('quotation_ids')
        all_quotation_ids = ', '.join(all_quotations)

        res.update({
            'Info_mpn': quotation.mpn,
            'all_quotationIDs': all_quotation_ids,
            'all_suppliers': supplier_names,
            'latest_price': latest_price,
        })

        return res
