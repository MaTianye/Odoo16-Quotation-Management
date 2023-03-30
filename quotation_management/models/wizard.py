from odoo import models, fields, api
import pandas as pd
import base64
import re
import random
import datetime
from io import BytesIO


class ImportQuotationWizard(models.TransientModel):
    _name = 'quotation_management.import_wizard'
    _description = 'Quotation Import Wizard'

    file = fields.Binary('Excel File', required=True)
    file_name = fields.Char('File Name', required=True)

    @api.model
    def get_file_data(self, file):
        data = base64.b64decode(file)
        file_stream = BytesIO(data)
        return pd.read_excel(file_stream, sheet_name=None)

    @api.model
    def generate_quotation_id(self, mpn):
        today = datetime.date.today().strftime("%y%m%d")  # Get current date as a 6-character string (YYMMDD)
        random_number = str(random.randint(10, 99))  # Generate a random 2-digit number
        mpn_part = mpn[:2] + mpn[-1]  # Get the first 3 characters of the 'mpn'

        quotation_id = today + random_number + mpn_part

        return quotation_id

    def import_data(self):
        all_data = self.get_file_data(self.file)
        for sheet_name, df in all_data.items():
            for index, row in df.iterrows():
                mpn = row.get('Sku') or row.get('Parts#') or row.get('Lenovo Sku#') or row.get('Part#') or row.get(
                    'MFG Part#') or row.get('Model')
                description = row.get('ProductName') or row.get('WebDescription') or row.get(
                    'Item Description') or row.get('Description') or row.get('Long Description') or row.get(
                    'Descrition')
                price = row.get('Offer') or row.get('Offer price') or row.get('Bulk Price') or row.get(
                    'Take Some Price') or row.get('Price Rebate applied') or row.get('Price')
                available_units = row.get('QTY') or row.get('Qty') or row.get('Inventory') or row.get('In Stock')
                supplier_ids = self.file_name
                quotation_ids = self.generate_quotation_id(mpn)

                if isinstance(available_units, str):
                    available_units = int(re.findall(r'\d+', available_units)[0])

                self.env['quotation.management'].create({
                    'mpn': mpn,
                    'description': description,
                    'price': price,
                    'available_units': available_units,
                    'supplier_ids': supplier_ids,
                    'quotation_ids': quotation_ids,
                    'create_date': fields.Datetime.now
                })
