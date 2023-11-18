import frappe
from datetime import datetime
import datetime as real_Date
import nepali_datetime
import pandas as pd
import requests


@frappe.whitelist()
def get_nepali_date(date):
    date_str = date
    date_format = '%Y-%m-%d'
    year = datetime.strptime(date_str, date_format).year
    month = datetime.strptime(date_str, date_format).month
    day = datetime.strptime(date_str, date_format).day
    return str(nepali_datetime.date.from_datetime_date(real_Date.date(year, month, day)))
    
import csv
@frappe.whitelist()
def create_charter_of_accounts():
    url = "http://34.138.131.178/files/chart_of_account_error_rows - Sheet1.csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
        try:
            doc = frappe.new_doc('Account')
            doc.account_type = row[1]
            doc.root_type = row[2]
            doc.report_type = row[3]
            doc.internal_id = row[4]
            doc.account_number = row[5]
            doc.account_name = row[6]
            doc.display_name = f'{row[5]} {row[6]}'
            doc.description = row[9]
            doc.sun_account_code = row[10]
            doc.is_disabled = row[11]
            doc.attention = row[12]
            doc.bank_account = row[13]
            doc.equivalent_npr_tds_account = row[14]
            doc.facsimile = row[15]
            doc.payment_instruction = row[16]
            doc.summary = row[17]
            doc.localized_display_name = row[18]
            doc.localized_name = row[19]
            doc.tds_npr_account = row[20]
            doc.tds_usd_account = row[21]
            doc.salutation = row[22]
            doc.subsidiary = row[23]
            doc.parent_account = row[0]
            doc.is_group = 0
            doc.insert(ignore_mandatory=True, ignore_links=True)
            frappe.db.commit()
        except Exception as e:
            print(f'{e}')


import csv
@frappe.whitelist()
def create_first_item_group():
    url = "http://test4:8000/files/NPR Item Master Final (2) - Sheet1 (2).csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
         try:
             if row[0] != '' and  not frappe.db.exists('Item Group', row[0]):
                doc = frappe.new_doc('Item Group')
                doc.item_group_name = row[0].strip()
                doc.is_group = 1
                doc.insert(ignore_mandatory=True, ignore_links=True)
                frappe.db.commit()
         except Exception as e:
             print(f'{e}')

@frappe.whitelist()
def create_second_item_group():
    url = "http://test4:8000/files/NPR Item Master Final (2) - Sheet1 (2).csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
        try:
            if row[1] != '' and  not frappe.db.exists('Item Group', row[1]) and row[1][:1] not in '0123456789':
                doc = frappe.new_doc('Item Group')
                doc.item_group_name = row[1].strip()
                doc.is_group = 1
                doc.parent_item_group = row[0].strip()
                doc.insert(ignore_mandatory=True, ignore_links=True)
                frappe.db.commit()
        except Exception as e:
            print(f'{e}')

@frappe.whitelist()
def create_third_item_group():
    url = "http://test4:8000/files/NPR Item Master Final (2) - Sheet1 (2).csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
        try:
            if  row[2][:1] not in '0123456789':
                doc = frappe.new_doc('Item Group')
                doc.item_group_name = row[2].strip()
                doc.is_group = 1
                doc.parent_item_group = row[1].strip()
                doc.insert(ignore_mandatory=True, ignore_links=True)
                frappe.db.commit()
        except Exception as e:
            print(f'{e}')

@frappe.whitelist()
def create_four_item_group():
    url = "http://test4:8000/files/NPR Item Master Final (2) - Sheet1 (2).csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
        try:
            doc = frappe.new_doc('Item Group')
            doc.item_group_name = row[3].strip()
            doc.is_group = 1
            doc.parent_item_group = row[2].strip()
            doc.insert(ignore_mandatory=True, ignore_links=True)
            frappe.db.commit()
        except Exception as e:
            print(f'{e}')

@frappe.whitelist()
def create_uom():
    url = "http://test4:8000/files/NPR Item Master Final (2) - Sheet1 (2).csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
        try:
            if row[37] != '' and  not frappe.db.exists('UOM', row[37]):
                doc = frappe.new_doc('UOM')
                doc.uom_name = row[37].strip()
                doc.enabled = 1
                doc.insert(ignore_mandatory=True, ignore_links=True)
                frappe.db.commit()
        except Exception as e:
            print(f'{e}')

@frappe.whitelist() 
def create_item():
    url = "http://test4:8000/files/NPR Item Master Final (1) - Sheet1 (1).csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
        try:
            doc = frappe.new_doc('Item') 
            doc.custom_internal_id = row[8].strip()
            doc.item_name = row[11].strip()
            doc.item_code = f'{row[9].strip()} {row[11].strip()}' 
            if row[5].strip() != '':
                doc.item_group = row[5].strip()
            if row[5].strip() == '':
                doc.item_group  = "No Group"
            if row[5][:1]  in '0123456789':
                doc.item_group  = "No Group"
            doc.custom_parent = row[10].strip()
            doc.custom_name = row[9].strip()
            doc.custom_display_name = row[11].strip()
            doc.description = row[12].strip()
            doc.custom_type = row[13].strip()
            doc.custom_sub_type = row[14].strip()
            doc.standard_rate = row[15].strip()
            doc.custom_item_collection = row[16].strip()
            doc.custom_jobtech_code = row[17].strip()
            doc.custom_old_item_code = row[18].strip()
            doc.custom_ups_code = row[19].strip()
            doc.custom_vendor = row[20].strip()
            doc.custom_offer_support = row[21].strip()
            doc.cost_center = row[22].strip()
            if row[13] == "Inventory Item":
                doc.is_stock_item= 1
            if row[13] != "Inventory Item":
                doc.is_stock_item= 0
            if row[23] == "No":
                doc.disabled= 0
            if row[23] == "Yes":
                doc.disabled= 1
            doc.custom_costing_method = row[34].strip()
            if row[34] == "FIFO":
                doc.valuation_method = "FIFO"
            if row[34] == "Average":
                doc.valuation_method = "Moving Average"
            if row[37] != '':
                doc.stock_uom = row[37].strip()
            if row[37] == '':
                doc.stock_uom = "No Uom"
            doc.purchase_uom = row[37].strip()
            doc.sales_uom = row[37].strip()
            doc.custom_primary_units_type = row[41].strip()
            doc.custom_tax_schedule = row[33].strip()
            doc.custom_subsidiary = row[45].strip()
            doc.custom_include_children = row[46].strip()
            doc.custom_location = row [47].strip()
            doc.insert(ignore_mandatory=True, ignore_links=True)
            frappe.db.commit()
        except Exception as e:
            print(f'{e}')
  
               
def create_price_list():
    url = "http://test4:8000/files/NPR Item Master Final (2) - Sheet1 (2).csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
        try:
            doc = frappe.new_doc('Item Price')
            doc.item_code =  f'{row[9].strip()} {row[11].strip()}'
            doc.price_list = "Standard Buying"
            doc.price_list_rate = row[43].strip()
            doc.insert(ignore_mandatory=True, ignore_links=True)
            frappe.db.commit()
        except Exception as e:
            print(f'{e}')

            
          

#supplier apis

def create_supplier():
    url = "http://test4:8000/files/HPL Vendor Master Final - Sheet1.csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
        try:
            doc = frappe.new_doc('Supplier')
            doc.custom_internal_id =  row[0].strip()
            doc.custom_id = row[1].strip()
            doc.custom_name = row[2].strip()
            doc.supplier_name = row[3].strip()
            doc.email = row[4].strip()
            doc.phone = row[5].strip()
            doc.fax = row[7].strip()
            if row[9].strip() == "No":
                doc.supplier_type = "Company"
            if row[9].strip() == "Yes":
                doc.supplier_type = "Individual"
            doc.company_name=  row[10].strip() 
            doc.company_phone=  row[11].strip()
            doc.primary_subsidiary_ = row[12].strip()  
            doc.website = row[13].strip() 
            doc.custom_company_address = row[14].strip()
            if row[15].strip() == "No":
                doc.disable = 1
            if row[15].strip() == "Yes":
                doc.disable = 1
            doc.custom_sun_sys_vendor_id = row[16].strip()
            doc.custom_vendor_source = row[17].strip()
            doc.custom_hpl_employee = row[20].strip()
            doc.custom_reapproval = row[29].strip()
            doc.supplier_group = row[22].strip()
            doc.tax_id = row[24].strip()
            doc.terms = row[25].strip()
            if row[26].strip() == "Nepalese Rupee":
                doc.default_currency = "NPR"
                doc.country = "Nepal"
            if row[26].strip() == "Euro":
                doc.default_currency = "EUR"
            if row[26].strip() == "Norwegian Krone":
                doc.default_currency = "NOK"
            if row[26].strip() == "US Dollar":
                doc.default_currency = "USD"
                doc.country = "United States"
            if row[26].strip() == "British Pound":
                doc.default_currency = "GBP"
            if row[26].strip() == "Singaporean Dollar":
                doc.default_currency = "SGD"
            if row[26].strip() == "Indian Rupees":
                doc.default_currency = "INR"
            if row[26].strip() == "Japanese Yen":
                doc.default_currency = "JPY"
            if row[26].strip() == "Hongkong Dollar":
                doc.default_currency = "HKD"
            if row[26].strip() == "Swiss Franc":
                doc.default_currency = "CHF"
            if row[26].strip() == "Philippine Peso":
                doc.default_currency = "PHP"
            if row[26].strip() == "Danish Krona":
                doc.default_currency = "DKK"
            if row[26].strip() == "Australian Dollar":
                doc.default_currency = "AUD"
            doc.country = ""
            doc.billing_address = row[37].strip()
            doc.insert(ignore_mandatory=True, ignore_links=True)
            frappe.db.commit()
        except Exception as e:
            print(f'{e}')
    


def create_supplier_group():
    url = "http://test4:8000/files/HPL Vendor Master Final - Sheet1.csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
        try:
            doc = frappe.new_doc('Supplier Group')
            doc.supplier_group_name =  row[22].strip()
            doc.insert(ignore_mandatory=True, ignore_links=True)
            frappe.db.commit()
        except Exception as e:
            print(f'{e}')
    


def create_bank_account():
    url = "http://test4:8000/files/HPL Vendor Master Final - Sheet1.csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
        try:
            doc = frappe.new_doc('Bank Account')
            doc.account_name =  row[30].strip()
            doc.bank_account_no = row[31].strip()
            doc.branch_code = row[33].strip
            doc.iban = row[35].strip()
            doc.party_type = "Supplier"
            doc.party = row[3].strip()
            doc.bank = create_bank(reader)
            doc.insert(ignore_mandatory=True, ignore_links=True)
            frappe.db.commit()
        
        except Exception as e:
            print(f'{e}')


def create_bank(reader):
    for row in reader:
        try:
            doc = frappe.new_doc('Bank')
            doc.bank_name = row[34].strip()
            doc.swift_number = row[36].strip()
            doc.insert(ignore_mandatory=True, ignore_links=True)
            frappe.db.commit()
            return doc.name
        except Exception as e:
            print(f'{e}')


import csv
import requests
import frappe

from datetime import datetime

def date_converter(date_str):
    date_obj = datetime.strptime(date_str, "%d/%m/%Y")
    formatted_date = date_obj.strftime("%Y-%m-%d")
    return formatted_date



def create_purchase_order():
    with open('/home/frappe/frappe-bench/apps/raindrop/po_number  - Sheet1.csv') as design_file:
        reader_po = csv.reader(design_file, delimiter=',')
        for value in reader_po:
            try:
                items = []
                with open('/home/frappe/frappe-bench/apps/raindrop/po - Sheet1.csv') as templates:
                    reader = csv.reader(templates, delimiter=',')
                    items.clear()
                    for row in reader:
                        if  row[0].strip() == value[0].strip():
                            if row[46] == '0':
                                tax = ''
                            elif row[46] != '0':
                                tax = "Nepal Tax - HPL"
                            if row[43] == '':
                                item = "Virtual Item"
                            elif row[43] != '':
                                item = frappe.db.get_value('Item', {'custom_name':row[43]}, 'name')
                            if row[45] != '' and float(row[45]) >= 1:
                                qty = row[45]
                            else:
                                qty = 1
                                rate = 0
                            if row[44] != '' and (row[45] != '' and float(row[45]) >= 1):
                                rate = row[44]
                            elif row[44] == '':
                                rate = 0
                            if row[43] == '':
                                items.append(
                                {
                                "item_code":"Virtual Item",
                                "qty": 1,
                                "rate": row[40],
                                "schedule_date":date_converter(value[1]),
                                "description":row[14],
                                "expense_account":"Vitual Item Expenses - HPL",
                                "custom_expense_category":value[33],
                                "cost_center":f'{row[36]} - HPL'
                                    }
                                    )
                            elif row[43] != '':
                                items.append(
                                {
                                "item_code":frappe.db.get_value('Item', {'custom_name':row[43]}, 'name'),
                                "qty": qty ,
                                "rate": rate,
                                "schedule_date":date_converter(value[1]),
                                "description":row[14],
                                "custom_expense_category":value[33],
                                "cost_center":f'{row[36]} - HPL'
                                    }
                                    )
               
                if len(items) > 0:
                    doc = frappe.new_doc('Purchase Order')
                    doc.supplier = value[31]
                    doc.custom_internal_id = value[0]
                    doc.custom_subsidiary_ =value[4]
                    doc.custom_document_number = value[2]
                    if value[46] == '0':
                        doc.taxes_and_charges =''
                    if value[46] != '0':
                        doc.taxes_and_charges = "Nepal Tax - HPL"
                        doc.append('taxes',
                                   {
                                       'type':"On Net Total",
                                       "rate":13,
                                       "account_head":"VAT - HPL",
                                       "description":value[14]
                                   })
                    if value[6] == "KIRNE (N)":
                        doc.set_warehouse = "KIRNE (N) - HPL"
                    if value[6] == "KATHMANDU (N)":
                        doc.set_warehouse="KATHMANDU (N) - HPL"
                    if value[6] == "PALATI (N)":
                        doc.set_warehouse="PALATI (N) - HPL"
                    if value[6] == "KATHMANDU":
                        doc.set_warehouse="KATHMANDU - HPL"
                    if value[6] == "KIRNE":
                        doc.set_warehouse="KIRNE - HPL"
                    doc.custom_billable = value[48]
                    doc.cost_center = f'{value[36]} - HPL'
                    doc.custom_billing_address = value[26]
                    doc.custom_shipping_address = value [27]
                    doc.custom_expense_category = value[33]
                    doc.custom_match_bill_to_receipt = value[49]
                    doc.custom_requested_by = value[11]
                    doc.terms = value[9]
                    doc.custom_tds_reclass_of = value[19]
                    doc.custom_procurement_person = value[15]
                    doc.memo = value[14]
                    doc.custom_created_by = value[3]
                    doc.custom_vendor_price_ref = value[17]
                    doc.custom_current_approver= value[22]
                    doc.custom_resubmit= value[23]
                    if frappe.db.exists('Project', value[30]) :
                        doc.project = value[30]
                    if not frappe.db.exists('Project', value[30]) and value[30] != '':
                        pro = frappe.new_doc('Project')
                        pro.project_name = value[30]
                        pro.insert(ignore_mandatory=True )
                        frappe.db.commit()
                        doc.project = value[30]
                    doc.custom_line_id= value[32]
                    doc.transaction_date = date_converter(value[1])
                    doc.schedule_date = date_converter(value[1])
                    for item in items:
                        doc.append("items", item)
                    doc.docstatus = 1
                    
                    doc.submit()
                    frappe.db.commit()
            except Exception as e:
                print(f'{e} {value[2]}')
   


def create_purchase_order_2023():
    with open('/home/frappe/frappe-bench/apps/raindrop/PO Number 2020 to 2023 - Sheet1.csv') as design_file:
        reader_po = csv.reader(design_file, delimiter=',')
        for value in reader_po:
            try:
                items = []
                with open('/home/frappe/frappe-bench/apps/raindrop/PO  2020 to 2023 - Sheet1.csv') as templates:
                    reader = csv.reader(templates, delimiter=',')
                    items.clear()
                    for row in reader:
                        if  row[0].strip() == value[0].strip():
                            if row[38] == '0%':
                                tax = ''
                            elif row[38] != '0%':
                                tax = "Nepal Tax - HPL"
                            if row[39] == '':
                                item = "Virtual Item"
                            elif row[43] != '':
                                item = frappe.db.get_value('Item', {'custom_name':row[43]}, 'name')
                            if row[43] != '' and float(row[43]) >= 1:
                                qty = row[43]
                            else:
                                qty = 1
                                rate = 0
                            if row[40] != '' and (row[40] != '' and float(row[40]) >= 1):
                                rate = row[40]
                            elif row[40] == '':
                                rate = 0
                            if row[39] == '' and row[34] != '':
                                if not frappe.db.exists('Account', f"{row[34].strip()} - HPL"):
                                    acc = frappe.new_doc('Account')
                                    acc.account_name = row[34].strip()
                                    acc.account_type = "Expense Account"
                                    acc.root_type = "Expense"
                                    acc.report_type = "Profit and Loss"
                                    acc.parent_account = "52000 - Other Expenses - HPL"
                                    acc.is_group = 0
                                    acc.insert(ignore_mandatory=True)
                                    frappe.db.commit()
                                    items.append(
                                    {
                                    "item_code":"Virtual Item",
                                    "qty": 1,
                                    "rate": row[54],
                                    "schedule_date":date_converter(value[1]),
                                    "description":row[14],
                                    "expense_account":f"{row[34].strip()} - HPL",
                                    "custom_expense_category":value[33],
                                    "cost_center":f'{row[36]} - HPL'
                                        }
                                        )

                                items.append(
                                {
                                "item_code":"Virtual Item",
                                "qty": 1,
                                "rate": row[54],
                                "schedule_date":date_converter(value[1]),
                                "description":row[14],
                                 "expense_account":f"{row[34].strip()} - HPL",
                                 "custom_expense_category":value[33],
                                 "cost_center":f'{row[36]} - HPL'
                                    }
                                    )
                            elif row[39] != '':
                                items.append(
                                {
                                "item_code":frappe.db.get_value('Item', {'custom_name':row[39]}, 'name'),
                                "qty": qty ,
                                "rate": rate,
                                "schedule_date":date_converter(value[1]),
                                "description":row[14],
                                "expense_account":"49000 - OtherCostGoodSold - HPL",
                                "custom_expense_category":value[33],
                                "cost_center":f'{row[36]} - HPL'
                                    }
                                    )
               
                if len(items) > 0:
                    doc = frappe.new_doc('Purchase Order')
                    doc.supplier = value[31]
                    if value[5] == "Nepalese Rupee":
                        doc.currency = "NPR"
                    elif value[5] == "Euro":
                        doc.currency = "EUR"
                    elif value[5] == "US Dollar":
                        doc.currency = "USD"
                    elif value[5] == "Indian Rupees":
                        doc.currency = "INR"
                    elif value[5] == "British Pound":
                        doc.currency = "GBP"
                    elif value[5] == "Norwegian Krone":
                        doc.currency = "NOK"
                    doc.conversion_rate = value[25]
                    doc.custom_internal_id = value[0]
                    doc.custom_subsidiary_ =value[4]
                    doc.custom_document_number = value[2]
                    if value[38] == '0%':
                        doc.taxes_and_charges =''
                    if value[38] != '0%':
                        doc.taxes_and_charges = "Nepal Tax - HPL"
                        doc.append('taxes',
                                   {
                                       'type':"On Net Total",
                                       "rate":13,
                                       "account_head":"VAT - HPL",
                                       "description":value[14]
                                   })
                    if value[6] == "KIRNE (N)":
                        doc.set_warehouse = "KIRNE (N) - HPL"
                    if value[6] == "KATHMANDU (N)":
                        doc.set_warehouse="KATHMANDU (N) - HPL"
                    if value[6] == "PALATI (N)":
                        doc.set_warehouse="PALATI (N) - HPL"
                    if value[6] == "KATHMANDU":
                        doc.set_warehouse="KATHMANDU - HPL"
                    if value[6] == "KIRNE":
                        doc.set_warehouse="KIRNE - HPL"
                    doc.custom_billable = value[48]
                    doc.cost_center = f'{value[36]} - HPL'
                    doc.custom_billing_address = value[26]
                    doc.custom_shipping_address = value [27]
                    doc.custom_expense_category = value[33]
                    doc.custom_match_bill_to_receipt = value[49]
                    doc.custom_requested_by = value[11]
                    doc.terms = value[9]
                    doc.custom_tds_reclass_of = value[19]
                    doc.custom_procurement_person = value[15]
                    doc.memo = value[14]
                    doc.custom_created_by = value[3]
                    doc.custom_vendor_price_ref = value[17]
                    doc.custom_current_approver= value[22]
                    doc.custom_resubmit= value[23]
                    if frappe.db.exists('Project', value[30]) :
                        doc.project = value[30]
                    if not frappe.db.exists('Project', value[30]) and value[30] != '':
                        pro = frappe.new_doc('Project')
                        pro.project_name = value[30]
                        pro.insert(ignore_mandatory=True )
                        frappe.db.commit()
                        doc.project = value[30]
                    doc.custom_line_id= value[32]
                    doc.transaction_date = date_converter(value[1])
                    doc.schedule_date = date_converter(value[1])
                    for item in items:
                        doc.append("items", item)
                    doc.docstatus = 1
                    doc.submit()
                    frappe.db.commit()
            except Exception as e:
                print(f'{e} {value[2]}')
   


def create_goods_received_2023():
    with open('/home/frappe/frappe-bench/apps/raindrop/GRN HPL 2020 to 2023 - Sheet1 (1).csv' ) as design_file:
        reader_po = csv.reader(design_file, delimiter=',')
        for value in  reader_po:
            try:
                po_name = frappe.db.get_value("Purchase Order", {"custom_document_number":value[31]}, 'name')
                if po_name != None:
                    po_items = frappe.db.get_all('Purchase Order Item', filters={"parent":po_name}, fields=['*'])
                    po_taxes = frappe.db.get_all('Purchase Taxes and Charges', filters={"parent":po_name}, fields=['*'])
                    items = []
                    taxes = []
                
                    if value[9] == '':
                        cost_center = "Main - HPL"
                    if value[9] != '':
                        cost_center = f'{value[9]} - HPL',
                    for item in po_items:
                        items.append(
                            {
                                "item_code":item.item_code,
                                "rate":item.rate,
                                "quantity":item.quantity,
                                "cost_center": item.cost_center,
                                "expense_account":item.expense_account,
                                "purchase_order": item.parent,
                                "purchase_order_item": item.name

                            }
                        )
                    for tax in po_taxes:
                        taxes.append(
                        {
                        'type':tax.type,
                        "rate":tax.rate,
                        "account_head":tax.account_head,
                        "description":tax.description
                        })

                    if len(items) > 0:
                        doc = frappe.new_doc('Purchase Receipt')
                        doc.supplier = value[16]
                        #doc.purchase_order = frappe.db.get_value("Purchase Order", {"custom_document_number":value[31]}, 'name')
                        doc.set_posting_time = 1
                        doc.posting_date = date_converter(value[1])
                        
                        if value[5] == "Nepalese Rupee":
                            doc.currency = "NPR"
                        elif value[5] == "Euro":
                            doc.currency = "EUR"
                        elif value[5] == "US Dollar":
                            doc.currency = "USD"
                        elif value[5] == "Indian Rupees":
                            doc.currency = "INR"
                        elif value[5] == "British Pound":
                            doc.currency = "GBP"
                        elif value[5] == "Norwegian Krone":
                            doc.currency = "NOK"
                        doc.conversion_rate = value[14]
                        doc.custom_internal_id = value[0]
                        doc.custom_subsidiary_ =value[4]
                        doc.custom_document_number = value[2]
                        if value[6] == "KIRNE (N)":
                            doc.set_warehouse = "KIRNE (N) - HPL"
                        if value[6] == "KATHMANDU (N)":
                            doc.set_warehouse="KATHMANDU (N) - HPL"
                        if value[6] == "PALATI (N)":
                            doc.set_warehouse="PALATI (N) - HPL"
                        if value[6] == "KATHMANDU":
                            doc.set_warehouse="KATHMANDU - HPL"
                        if value[6] == "KIRNE":
                            doc.set_warehouse="KIRNE - HPL"
                        doc.cost_center = cost_center
                        doc.custom_requested_by = value[8]
                        doc.custom_created_by = value[3]
                        doc.custom_vendor_price_ref = value[12]
                        if frappe.db.exists('Project', value[15]) :
                            doc.project = value[15]
                        if not frappe.db.exists('Project', value[15]) and value[15] != '':
                            pro = frappe.new_doc('Project')
                            pro.project_name = value[15]
                            pro.insert(ignore_mandatory=True )
                            frappe.db.commit()
                            doc.project = value[15]
                        doc.custom_line_id= value[17]
                        for item in items:
                            doc.append("items", item)
                        for tax in taxes:
                            doc.append('taxes', tax)
                        doc.docstatus = 1
                        doc.submit()
                        frappe.db.commit()
                        frappe.db.set_value('Purchase Order', po_name, 'status', 'To Bill')
            except Exception as e:
                print(f' {e} {value[2]} {po_name}')




def create_purchase_invoice_2023():
    with open('/home/doreenalita/frappe/frappe-bench/apps/raindrop/HPL Purchase Invoice NPR 2020_2013 - Sheet1 (1).csv' ) as design_file:
        reader_po = csv.reader(design_file, delimiter=',')
        for value in  reader_po:
            try:
                items = []
                with open('/home/doreenalita/frappe/frappe-bench/apps/raindrop/HPL Purchase Invoice Number NPR 2020_2013 - Sheet1.csv' ) as templates:
                    reader = csv.reader(templates, delimiter=',')
                    for row in reader:
                        cost_center = "Main - HPL"
                        if row[45] != '':
                            cost_center = f"{row[45]} - HPL"
                        if row[0] == value[0] and  frappe.db.get_value("Purchase Order", {"custom_document_number":row[52]}, 'name') != None:
                            name = frappe.db.get_value("Purchase Order", {"custom_document_number":row[52]}, 'name')
                            items.append(
                                {
                                "item_code": frappe.db.get_value("Item", {"custom_name":row[39]}, 'name'),
                                "rate":row[40],
                                "quantity":row[43],
                                "cost_center": cost_center,
                                "expense_account":f"{35} - HPL",
                                "description":row[15],
                                "purchase_order": frappe.db.get_value("Purchase Order", {"custom_document_number":row[52]}, 'name'),
                                "purchase_order_item": frappe.db.get_value("Purchase Order Item", {"parent":name}, 'name')
                                }
                            
                            )
                doc = frappe.new_doc("Purchase Invoice")
                doc.custom_bill_number = value[1]
                doc.custom_internal_id = value[0]
                doc.posting_date = value[2]
                doc.custom_document_number = value[3]
                doc.custom_created_by = value[4]
                doc.custom_subsidiary = value[5]
                if value[44] != '0%':
                    doc.taxes_and_charges = "Nepal Tax - HPL"
                    doc.append('taxes',
                    {
                        'type':"On Net Total",
                        "rate":13,
                        "account_head":"VAT - HPL",
                        "description":value[15]
                            })
                if value[6] == "Nepalese Rupee":
                    doc.currency = "NPR"
                elif value[6] == "Euro":
                    doc.currency = "EUR"
                elif value[6] == "US Dollar":
                    doc.currency = "USD"
                elif value[6] == "Indian Rupees":
                    doc.currency = "INR"
                elif value[6] == "British Pound":
                    doc.currency = "GBP"
                elif value[6] == "Norwegian Krone":
                    doc.currency = "NOK"
                if value[7] == "KIRNE (N)":
                    doc.update_stock = 1
                    doc.set_warehouse = "KIRNE (N) - HPL"
                if value[7] == "KATHMANDU (N)":
                    doc.update_stock = 1
                    doc.set_warehouse="KATHMANDU (N) - HPL"
                if value[7] == "PALATI (N)":
                    doc.update_stock = 1
                    doc.set_warehouse="PALATI (N) - HPL"
                if value[7] == "KATHMANDU":
                    doc.update_stock = 1
                    doc.set_warehouse="KATHMANDU - HPL"
                if value[7] == "KIRNE":
                    doc.update_stock = 1
                    doc.set_warehouse="KIRNE - HPL"
                doc.conversion_rate = value[26]
                doc.custom_procurement_person = value[16]
                doc.terms = value[10]
                doc.custom_billing_address = value[27]
                doc.project = value[31]
                doc.custom_shipping_address = value[28]
                doc.custom_accounting_approval  = value[25]
                doc.custom_resubmit = value[24]
                doc.custom_match_bill_to_receipt = value[49]
                doc.custom_vendor_price_ref_date = value[19]
                doc.custom_current_approval = value[23]
                doc.custom_vendor = value[18]
                doc.supplier = value[32]
                doc.custom_line_id = value[33]
                for item in items:
                    doc.append('items', item)
                doc.docstatus = 1
                print(items)
                # doc.insert()
                # frappe.db.commit()
            except Exception as e:
                print(f' {e} {items} ')



def create_customer():
    url = "http://34.138.131.178/files/HPL NPR Customer Master.csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    next(reader, None)
    for row in reader:
      try:
        doc = frappe.new_doc('Customer')
        if row[31] != '':
            if not frappe.db.exists('Account', f"{row[31].strip()} - HPL"):
                acc = frappe.new_doc('Account')
                acc.account_name = row[31].strip()
                acc.account_type = "Receivable"
                acc.root_type = "Asset"
                acc.report_type = "Balance Sheet"
                acc.parent_account = "15000 - Accounts Receivable - HPL"
                acc.is_group = 0
                acc.insert(ignore_mandatory=True)
                frappe.db.commit()
        if row[31] != '':
            doc.append('accounts',
                    {
                        'company':"Himal Power Limited",
                        "account":f"{row[31].strip()} - HPL"
                    })
        doc.custom_internal_id =  row[0].strip()
        doc.custom_id = row[1].strip()
        doc.custom_name = row[2].strip() 
        doc.custom_email = row[3].strip()
        doc.custom_phone = row[4].strip()
        doc.custom_fax = row[6].strip()
        doc.custom_is_individual = row[9].strip()
        doc.custom_company_name=  row[10].strip() 
        doc.custom_status = row[11].strip()
        doc.custom_address = row[19].strip()
        doc.custom_primary_subsidiary_= row[20].strip()
        doc.custom_default_receivables_account = f"{row[31].strip()} - HPL"
        doc.custom_primary_currency = row[35].strip()
        doc.custom_terms = row[36].strip()
        doc.custom_tax_number = row[37].strip()
        doc.custom_credit_limit = row[38].strip()
        doc.customer_name = f'{row[1].strip()}{row[2].strip()}'
        doc.customer_group = "commercial"
        doc.territory = "Nepal"  
        doc.custom_customer_id = row[1].strip()
        doc.insert()
        frappe.db.commit()
      except Exception as e:
        print(f'{e}')


def create_sales_invoice_2023():
    with open('/home/frappe/frappe-bench/apps/raindrop/HPL Sales Invoice  NUmber NPR 2020_2023 - Sheet1.csv') as design_file:
        reader_po = csv.reader(design_file, delimiter=',')
        for value in reader_po:
            try:
                items = []
                with open('/home/frappe/frappe-bench/apps/raindrop/HPL Sales Invoice   NPR 2020_2023 - Sheet1.csv') as templates:
                    reader = csv.reader(templates, delimiter=',')
                    items.clear()
                    for row in reader:
                        
                        if row[34] != '':
                            if not frappe.db.exists('Account', f"{row[34].strip()} - HPL"):
                                acc = frappe.new_doc('Account')
                                acc.account_name = row[34].strip()
                                acc.account_type = ""
                                acc.root_type = "Income"
                                acc.report_type = "Profit and Loss"
                                acc.parent_account = "51000 - Direct Expenses - HPL"
                                acc.is_group = 0
                                acc.insert(ignore_mandatory=True)
                                frappe.db.commit()
                        if  row[0].strip() == value[0].strip():
                            if row[44] == '0':
                                tax = ''
                            elif row[44] != '0':
                                tax = "Nepal Tax - HPL"
                            elif row[43] != '':
                                item = frappe.db.get_value('Item', {'custom_name':row[39]}, 'name')
                            if row[43] != '' and float(row[43]) >= 1:
                                qty = row[43]
                            else:
                                qty = 1
                                rate = 0
                            if row[40] != '' and (row[43] != '' and float(row[43]) >= 1):
                                rate = row[40]
                            elif row[40] == '':
                                rate = 0
                            if row[39] != '':
                                items.append(
                                {
                                "item_code":frappe.db.get_value('Item', {'custom_name':row[39]}, 'name'),
                                "qty": row[43],
                                "rate": row[40],
                                "description":row[14],
                                "income_account":f"{row[34].strip()} - HPL",
                                "cost_center":f'{row[12]} - HPL'
                                    }
                                    )
               
                if len(items) > 0:
                    doc = frappe.new_doc('Sales Invoice')
                    if not frappe.db.exists('Customer', value[30]):
                        cus = frappe.new_doc('Customer')
                        cus.customer_name = value[30]
                        cus.customer_group = "Commercial"
                        cus.territory = "Nepal"
                        cus.insert()
                        frappe.db.commit()
                    doc.customer = value[30]
                    doc.set_posting_time = 1
                    doc.posting_date = date_converter(value[1])
                    doc.due_date = date_converter(value[16])
                    doc.custom_internal_id = value[0]
                    doc.custom_subsidiary_ =value[4]
                    doc.custom_document_number= value[2]
                    doc.custom_created_by = value[3]
                    if value[5] == "Nepalese Rupee":
                        doc.currency = "NPR"
                    elif value[5] == "Euro":
                        doc.currency = "EUR"
                    elif value[5] == "US Dollar":
                        doc.currency = "USD"
                    elif value[5] == "Indian Rupees":
                        doc.currency = "INR"
                    elif value[5] == "British Pound":
                        doc.currency = "GBP"
                    elif value[5] == "Norwegian Krone":
                        doc.currency = "NOK"
                    if value[46] == '0':
                        doc.taxes_and_charges =''
                    if value[44] != '0':
                        doc.taxes_and_charges = "Nepal Tax - HPL"
                        doc.append('taxes',
                                   {
                                       'type':"On Net Total",
                                       "rate":13,
                                       "account_head":"VAT - HPL",
                                       "description":value[14]
                                   })
                    doc.update_stock = 1
                    if value[6] == "KIRNE (N)":
                        doc.set_warehouse = "KIRNE (N) - HPL"
                    if value[6] == "KATHMANDU (N)":
                        doc.set_warehouse="KATHMANDU (N) - HPL"
                    if value[6] == "PALATI (N)":
                        doc.set_warehouse="PALATI (N) - HPL"
                    if value[6] == "KATHMANDU":
                        doc.set_warehouse="KATHMANDU - HPL"
                    if value[6] == "KIRNE":
                        doc.set_warehouse="KIRNE - HPL"
                    doc.terms = value[9]
                    doc.cost_center = f'{value[12]} - HPL'
                    doc.custom_approval_status = value[13]
                    doc.custom_procurement_person = value[15]
                    doc.custom_vendor_price_ref = value[17]
                    doc.custom_vendor_price_ref_date = value[18]
                    doc.custom_tds_reclass_of = value[19]
                    doc.custom_vat_reclass_of = value[20]
                    doc.custom_current_approver = value[22]
                    doc.custom_resubmit = value[23]
                    doc.custom_accounting_approval = value[24]
                    doc.conversion_rate = value[25]
                    doc.custom_billing_address = value[26]
                    doc.custom_shipping_address = value[27]
                    for item in items:
                        doc.append("items", item)
                    doc.docstatus = 1
                    doc.insert()
                    frappe.db.commit()
            except Exception as e:
                print(f'{e} {value[2]}')

def create_jounal_entry():
    with open('/home/frappe/frappe-bench/apps/raindrop/HPL Journal Number NPR 2020_2023 - Sheet1 (2).csv' ) as design_file:
        reader_po = csv.reader(design_file, delimiter=',')
        for value in reader_po:
            try:
                items = []
                with open('/home/frappe/frappe-bench/apps/raindrop/HPL Journal Entry NPR 2020_2023 - Sheet1.csv') as templates:
                    reader = csv.reader(templates, delimiter=',')
                    items.clear()
                    for row in reader:
                        if  row[0].strip() == value[0].strip():
                            if row[7] != '':
                                if not frappe.db.exists('Account', f"{row[7].strip()} - HPL"):
                                    acc = frappe.new_doc('Account')
                                    acc.account_name = row[7].strip()
                                    acc.account_type = ""
                                    acc.root_type = "Income"
                                    acc.report_type = "Profit and Loss"
                                    acc.parent_account = "51000 - Direct Expenses - HPL"
                                    acc.is_group = 0
                                    acc.insert(ignore_mandatory=True)
                                    frappe.db.commit()
                            cost_center = "Main - HPL"
                            if row[15] != '':
                                cost_center = f'{row[15]} - HPL'
                            items.append(
                        {
                            
                            'account': f'{row[7]} - HPL',
                            'debit_in_account_currency':row[8].strip(),
                            'credit_in_account_currency':row[9].strip(),
                            'cost_center':cost_center
                        })
                        
                       
              
                doc = frappe.new_doc('Journal Entry')
                doc.custom_internal_id = value[0]
                doc.posting_date = date_converter(value[1])
                doc.custom_subsidiary = value[2]
                for item in items:
                    
                    doc.append('accounts', item)
              
                doc.user_remark = value[10]
                doc.custom_document_number = value[11]
                doc.custom_created_from = value[12]
                doc.custom_created_by = value[13]
                doc.custom_location = value[15]
                doc.custom_name = value[20]
                doc.custom_party = row[10]
                doc.custom_posting = value[25]
                doc.custom_period =  value[26]
                doc.docstatus = 1
                doc.insert(ignore_mandatory=True)
                frappe.db.commit()
            except Exception as e:
                print(f'{e} {value[11]} ')
def create_cash_bank_received():
    with open('/home/frappe/frappe-bench/apps/raindrop/HPL Journal Number NPR 2020_2023 - Sheet1 (2).csv' ) as design_file:
        reader_po = csv.reader(design_file, delimiter=',')
        for value in reader_po:
            try:
                with open('/home/frappe/frappe-bench/apps/raindrop/HPL Journal Entry NPR 2020_2023 - Sheet1.csv') as templates:
                    reader = csv.reader(templates, delimiter=',')
                    for row in reader:
                        total = 0
                        if  row[0].strip() == value[0].strip():
                            if not frappe.db.exists('Account', f"{row[22].strip()} - HPL"):
                                    acc = frappe.new_doc('Account')
                                    acc.account_name = row[22].strip()
                                    acc.account_type = "Payable"
                                    acc.root_type = "Liability"
                                    acc.report_type = "Balance Sheet"
                                    acc.parent_account = "24300 - Accounts Payable - HPL"
                                    acc.is_group = 0
                                    acc.insert(ignore_mandatory=True)
                                    frappe.db.commit()
                            total = total + row[43]
                payment = frappe.new_doc("Payment Entry")
                payment.party_type = "Supplier"
                payment.party = value[11]
                currency = 'NPR'
                if value[5] == "Nepalese Rupee":
                    currency = "NPR"
                   
                elif value[5] == "Euro":
                    currency = "EUR"
                elif value[5] == "US Dollar":
                    currency = "NPR"
                    
                elif value[5] == "Indian Rupees":
                    currency = "INR"
                elif value[5] == "British Pound":
                    currency = "GBP"
                elif value[5] == "Norwegian Krone":
                    currency = "NOK"
                if value[7] == '':
                    cost_center = "Main - HPL"
                if value[7] != '':
                    cost_center = f'{value[8]} - HPL',
                payment = frappe.new_doc('Payment Entry')
                payment.payment_type = "Pay"	
                payment.custom_internal_id = value[0]
                payment.custom_document_number = value[2]
                payment.custom_subsidiary = value[4]
                payment.custom_location = value[6]
                payment.custom_line_id = value[21]
                payment.custom_created_by = value[2]
                payment.mode_of_payment = "Cash"	
                payment.party_type = "Supplier"
                payment.posting_date = date_converter(value[1])
                payment.paid_to_account_currency  = currency
                payment.paid_from_account_currency = currency
                payment.cost_center = cost_center
                payment.paid_amount = value[16]
                payment.received_amount =  payment.paid_amount 
                payment.paid_to = f'{value[12]} - HPL'
                payment.paid_from = f'{value[22]} - HPL'
                payment.target_exchange_rate = value[15]
                payment.project =value[20]
                payment.reference_no=value[11]
                payment.reference_date = date_converter(value[1])
                payment.cost_center = cost_center
                payment.docstatus = 1
                payment.insert()
                frappe.db.commit()
            except Exception as e:
                print(f"{e} {value}")



def create_supplier_payment():
    with open( '/home/frappe/frappe-bench/apps/raindrop/Supplier Payment Number 2020_2023 - Sheet1.csv' ) as design_file:
        reader_po = csv.reader(design_file, delimiter=',')
        for value in reader_po:
            try:
                total = 0.0
                with open('/home/frappe/frappe-bench/apps/raindrop/Supplier Payment 2020_2023 - Sheet1.csv') as templates:
                    reader = csv.reader(templates, delimiter=',')
                    for row in reader:
                        if  row[0].strip() == value[0].strip():
                            total = total +  float(row[16].replace(',', '')) 
                payment = frappe.new_doc("Payment Entry")
                payment.payment_type = "Pay"	
                if value[4].startswith('5'):
                    payment.party_type = "Supplier"
                    payment.party = value[4]
                    payment.paid_from = f'{value[6]} - HPL'
                elif not value[4].startswith('5'):
                    payment.party_type = "Employee"
                    payment.party = value[4]
                    payment.paid_from = "2110 - Creditors - HPL"
                    payment.paid_to = f'{value[6]} - HPL'
                exchange = 1
                currency = 'NPR'
                if value[13] == "Nepalese Rupee":
                    currency = "NPR"
                elif value[13] == "Euro":
                    currency = "EUR"
                    exchange = 140.34
                elif value[13] == "US Dollar":
                    currency = "USD"
                    exchange = 120.7
                elif value[13] == "Indian Rupees":
                    currency = "INR"
                    exchange = 1.6015
                elif value[13] == "British Pound":
                    currency = "GBP"
                    exchange = 166.77
                elif value[13] == "Norwegian Krone":
                    currency = "NOK"
                    exchange = 13.0846
                if value[8] == '':
                    cost_center = "Main - HPL"
                if value[8] != '':
                    cost_center = f'{value[8]} - HPL',
                payment.custom_payment_type = "Supplier Payment"
                payment.custom_internal_id = value[0]
                payment.custom_period = value[2]
                payment.custom_document_number = value[3]
                payment.custom_subsidiary = value[5]
                payment.custom_memo = value[7]
                payment.custom_location = value[9]
                payment.custom_applied_to_transaction = value[15]
                payment.custom_created_from = value[17]
                payment.custom_line_id = value[18]
                payment.custom_billing_address = value[19]
                payment.custom_applied_to_link_type = value[20]
                payment.custom_created_by = value[22]
                payment.mode_of_payment = "Cash"	
                payment.posting_date = date_converter_month(value[1])
                payment.paid_to_account_currency  = currency
                payment.paid_from_account_currency = currency
                payment.cost_center = cost_center
                payment.paid_amount = total
                payment.received_amount = total
                payment.source_exchange_rate = exchange
                payment.reference_no=value[7]
                payment.reference_date = date_converter_month(value[1])
                payment.cost_center = cost_center
                payment.docstatus = 1
                payment.insert()
                frappe.db.commit()
            except Exception as e:
                print(f"{e} {value[0]}")

def create_expenses():
    with open('/home/frappe/frappe-bench/apps/raindrop/HPL Journal Number NPR 2020_2023 - Sheet1 (2).csv' ) as design_file:
        reader_po = csv.reader(design_file, delimiter=',')
        for value in reader_po:
            try:
                items = []
                with open('/home/frappe/frappe-bench/apps/raindrop/HPL Journal Entry NPR 2020_2023 - Sheet1.csv') as templates:
                    reader = csv.reader(templates, delimiter=',')
                    items.clear()
                    for row in reader:
                        if  row[0].strip() == value[0].strip():
                            if row[7] != '':
                                if not frappe.db.exists('Account', f"{row[7].strip()} - HPL"):
                                    acc = frappe.new_doc('Account')
                                    acc.account_name = row[7].strip()
                                    acc.account_type = ""
                                    acc.root_type = "Income"
                                    acc.report_type = "Profit and Loss"
                                    acc.parent_account = "51000 - Direct Expenses - HPL"
                                    acc.is_group = 0
                                    acc.insert(ignore_mandatory=True)
                                    frappe.db.commit()
                            cost_center = "Main - HPL"
                            if row[15] != '':
                                cost_center = f'{row[15]} - HPL'
                            items.append(
                        {
                            
                            'account': f'{row[7]} - HPL',
                            'debit_in_account_currency':row[8].strip(),
                            'credit_in_account_currency':row[9].strip(),
                            'cost_center':cost_center
                        })
                        
                       
              
                doc = frappe.new_doc('Journal Entry')
                doc.custom_internal_id = value[0]
                doc.posting_date = date_converter(value[1])
                doc.custom_subsidiary = value[2]
                for item in items:
                    
                    doc.append('accounts', item)
              
                doc.user_remark = value[10]
                doc.custom_document_number = value[11]
                doc.custom_created_from = value[12]
                doc.custom_created_by = value[13]
                doc.custom_location = value[15]
                doc.custom_name = value[20]
                doc.custom_party = row[10]
                doc.custom_posting = value[25]
                doc.custom_period =  value[26]
                doc.docstatus = 1
                doc.insert(ignore_mandatory=True)
                frappe.db.commit()
            except Exception as e:
                print(f'{e} {value[11]} ')

def create_payment():
    with open('/home/frappe/frappe-bench/apps/raindrop/Payment Received from customer number 2020_2023 - Sheet1.csv') as design_file:
        reader_po = csv.reader(design_file, delimiter=',')
        for value in reader_po:
            try:
                items = []
                with open('/home/frappe/frappe-bench/apps/raindrop/Payment Received from customer  2020_2023 - Sheet1.csv') as templates:
                    reader = csv.reader(templates, delimiter=',')
                    items.clear()
                    for row in reader:
                        if  row[0].strip() == value[0].strip(): 
                            if row[15] != '' and frappe.db.get_value('Sales Invoice', {'custom_document_number':row[15]}, 'name') !=None:
                                items.append(
                                    {
                                    "reference_doctype":"Sales Invoice", 
                                    "reference_name":frappe.db.get_value('Sales Invoice', {'custom_document_number':row[15]}, 'name'),
                                    "total_amount":frappe.db.get_value('Sales Invoice', {'custom_document_number':row[15]}, 'grand_total'),
                                    "outstanding_amount":frappe.db.get_value('Sales Invoice', {'custom_document_number':row[15]}, 'grand_total'),
                                    "allocated_amount":frappe.db.get_value('Sales Invoice', {'custom_document_number':row[15]}, 'grand_total'),
                        
                                }
                                )
                currency = 'NPR'
                if value[13] == "Nepalese Rupee":
                    currency = "NPR"
                    exchange = 1
                elif value[13] == "Euro":
                    currency = "EUR"
                elif value[13] == "US Dollar":
                    currency = "NPR"
                    exchange = 120.75
                elif value[13] == "Indian Rupees":
                    currency = "INR"
                elif value[13] == "British Pound":
                    currency = "GBP"
                elif value[13] == "Norwegian Krone":
                    currency = "NOK"
                if value[8] == '':
                    cost_center = "Main - HPL"
                if value[8] != '':
                    cost_center = f'{value[8]} - HPL',
                payment = frappe.new_doc('Payment Entry')
                payment.payment_type = "Receive"	
                payment.custom_period = value[2]
                payment.custom_subsidiary = value[4]
                payment.custom_location = value[9]
                payment.custom_line_id = value[18]
                payment.custom_created_by = value[22]
                payment.mode_of_payment = "Cash"	
                payment.party_type = "Customer"
                payment.posting_date = date_converter(value[1])
                payment.paid_to_account_currency  = currency
                payment.paid_from_account_currency = currency
                if len(items) == 0:
                   payment.party = value[3]
                   payment.paid_from = f'{value[20]} - HPL'
                if len(items) != 0:
                    payment.party = frappe.db.get_value('Sales Invoice', {'custom_document_number':row[15]}, 'customer') 
                payment.paid_amount = value[16]
                payment.received_amount =  payment.paid_amount 
                payment.paid_to = f'{value[5]} - HPL'
                payment.paid_from = frappe.db.get_value('Sales Invoice', {'custom_document_number':row[15]}, 'debit_to') 
                payment.target_exchange_rate = exchange
                for item in items:
                    payment.append("references", item
                           )
                payment.reference_no=value[6]
                payment.reference_date = date_converter(value[1])
                payment.cost_center = cost_center
                payment.docstatus = 1
                payment.insert()
                frappe.db.commit()
            except Exception as e:
                print(f'{e} {value[11]} ')



def stock_out():
    with open('/home/frappe/frappe-bench/apps/raindrop/Stock out number - Sheet1.csv') as design_file:
        reader_po = csv.reader(design_file, delimiter=',')
        for value in reader_po:
            try:
                items = []
                recieved = []
                with open('/home/frappe/frappe-bench/apps/raindrop/Stock out - Sheet1.csv' ) as templates:
                    reader = csv.reader(templates, delimiter=',')
                    items.clear()
                    for row in reader:
                        if row[0] == value[0]:
                            frappe.db.set_value('Item', frappe.db.get_value('Item', {'custom_name':row[13]}, 'name'), 'is_stock_item', 1)
                            frappe.db.commit()
                            items.append(  {
                        "s_warehouse": f"{row[12]} - HPL",
                        "item_code":  frappe.db.get_value('Item', {'custom_name':row[13]}, 'name') ,
                        "qty":row[15],
                        "expense_account":f"{row[4]} - HPL",
                        "basic_rate": row[16],
                        "uom": row[14],
                        "cost_center" : f"{row[9]} - HPL"
                    }
                            )
                frappe.db.set_value('Company', "Himal Power Limited", 'default_inventory_account', f"{value[3].strip()} - HPL")
                if value[1] != None or value[1] != '':
                    stock = frappe.new_doc("Stock Entry")
                    stock.set_posting_time = 1
                    stock.posting_date = date_converter(value[1])
                    stock.stock_entry_type = "Material Issue"
                    stock.custom_document_number = value[2]
                    stock.custom_period = value[8]
                    stock.custom_internal_id = value[0]
                    stock.custom_subsidiary = value[7]
                    stock.custom_account_main = value[4]
                    stock.custom_memo_sub = value[5]
                    stock.custom_memo = value[6]
                    for item in items:
                        stock.append('items',item)
                    stock.docstatus = 1
                    stock.insert()
                    frappe.db.commit()
            except Exception as e:
                print(f'{e} {value[1]} ')


def stock_in_one():
    with open('/home/frappe/frappe-bench/apps/raindrop/Stock out number - Sheet1.csv') as design_file:
        reader_po = csv.reader(design_file, delimiter=',')
        for value in reader_po:
            try:
                items = []
                recieved = []
                with open('/home/frappe/frappe-bench/apps/raindrop/Stock out - Sheet1.csv' ) as templates:
                    reader = csv.reader(templates, delimiter=',')
                    items.clear()
                    for row in reader:
                        if row[0] == value[0]:
                            frappe.db.set_value('Item', frappe.db.get_value('Item', {'custom_name':row[13]}, 'name'), 'is_stock_item', 1)
                            frappe.db.commit()
                            recieved.append({
                        "t_warehouse": f"{row[12]} - HPL",
                        "item_code":  frappe.db.get_value('Item', {'custom_name':row[13]}, 'name') ,
                        "qty":row[15],
                        "expense_account":f"{row[3]} - HPL",
                        "basic_rate": row[16],
                        "uom": row[14],
                        "cost_center" : f"{row[9]} - HPL"
                    })
                
                if value[1] != None or value[1] != '':
                    doc = frappe.new_doc("Stock Entry")
                    frappe.db.set_value('Company', "Himal Power Limited", 'default_inventory_account', f"{value[4].strip()} - HPL")
                    doc.set_posting_time = 1
                    doc.posting_date = date_converter(value[1])
                    doc.stock_entry_type = "Material Receipt"
                    doc.custom_document_number = f'{value[2]} Receipt'
                    doc.custom_period = value[8]
                    doc.custom_internal_id = value[0]
                    doc.custom_subsidiary = value[7]
                    doc.custom_account_main = value[4]
                    doc.custom_memo_sub = value[5]
                    doc.custom_memo = value[6]
                    for item in recieved:
                        doc.append('items',item)
                    doc.docstatus = 1
                    doc.insert()
                    frappe.db.commit()
            except Exception as e:
                print(f'{e} {value[1]} ')



def date_converter_month(date_str):
    date_obj = datetime.strptime(date_str, "%m/%d/%Y")
    formatted_date = date_obj.strftime("%Y-%m-%d")
    return formatted_date


def stock_in_two():
    with open('/home/frappe/frappe-bench/apps/raindrop/Stock received number - Sheet1.csv') as design_file:
        reader_po = csv.reader(design_file, delimiter=',')
        for value in reader_po:
            try:
                items = []
                with open('/home/frappe/frappe-bench/apps/raindrop/Stock received - Sheet1.csv') as templates:
                    reader = csv.reader(templates, delimiter=',')
                    items.clear()
                    for row in reader:
                        if row[0] == value[0]:
                            frappe.db.set_value('Item', frappe.db.get_value('Item', {'custom_name':row[13]}, 'name'), 'is_stock_item', 1)
                            frappe.db.commit()
                            items.append(  {
                        "t_warehouse": f"{row[12]} - HPL",
                        "item_code":  frappe.db.get_value('Item', {'custom_name':row[13]}, 'name') ,
                        "qty":row[15],
                        "expense_account":f"{row[3]} - HPL",
                        "basic_rate": row[16],
                        "uom": row[14],
                        "cost_center" : f"{row[9]} - HPL"
                    }
                            )
                doc = frappe.new_doc("Stock Entry")
                frappe.db.set_value('Company', "Himal Power Limited", 'default_inventory_account', f"{value[4].strip()} - HPL")
                if value[1] != None or value[1] != '':
                    doc.set_posting_time = 1
                    doc.posting_date = date_converter_month(value[1])
                    doc.stock_entry_type = "Material Receipt"
                    doc.custom_document_number = value[2]
                    doc.custom_period = value[8]
                    doc.custom_internal_id = value[0]
                    doc.custom_subsidiary = value[7]
                    doc.custom_account_main = value[4]
                    doc.custom_memo = value[6]
                    for item in items:
                        doc.append('items',item)
                    doc.docstatus = 1
                    doc.insert()
                    frappe.db.commit()
            except Exception as e:
                print(f'{e} {value[1]} ')



# cheque payment
def create_cheque_payment():
    with open( '/home/frappe/frappe-bench/apps/raindrop/Exp Cheq Payment Number 2020_2023 - Sheet1.csv') as design_file:
        reader_po = csv.reader(design_file, delimiter=',')
        for value in reader_po:
            try:
                total = 0.0
                with open('/home/frappe/frappe-bench/apps/raindrop/Exp Cheq Payment 2020_2023 - Sheet1.csv') as templates:
                    reader = csv.reader(templates, delimiter=',')
                    for row in reader:
                        if  row[0].strip() == value[0].strip():
                            total = total +  float(row[46].replace(',', '')) 
                payment = frappe.new_doc("Payment Entry")
                payment.payment_type = "Pay"	
                if value[32].startswith('5'):
                    payment.party_type = "Supplier"
                    payment.party = value[32]
                elif not value[32].startswith('5'):
                    payment.party_type = "Employee"
                    payment.party = value[32]     
                currency = 'NPR'
                if value[6] == "Nepalese Rupee":
                    currency = "NPR"
                    payment.paid_from = f'{value[1]} - HPL'
                    payment.paid_to = f'{value[35]} - HPL'
                elif value[6] == "Euro":
                    currency = "EUR"
                    payment.paid_from = create_account(account=f'{value[1]}(EUR)',root_type="Expense", parent="51000 - Direct Expenses - HPL",  currency='EUR')
                    payment.paid_to = create_account(f'{value[35]}(EUR)',"Expense", "51000 - Direct Expenses - HPL" ,  'EUR')
                    payment.source_exchange_rate = float(f'{value[26].strip()}')
                elif value[6] == "US Dollar":
                    currency = "USD"
                    payment.paid_from = create_account(f'{value[1]}(USD)',"Expense", "51000 - Direct Expenses - HPL" ,  'USD')
                    payment.paid_to = create_account(f'{value[35]}(USD)',"Expense", "51000 - Direct Expenses - HPL" , 'USD')
                    payment.source_exchange_rate = float(f'{value[26].strip()}')
                elif value[6] == "Indian Rupees":
                    currency = "INR"
                    payment.paid_from = create_account(f'{value[1]}(INR)',"Expense", "51000 - Direct Expenses - HPL" ,  'INR')
                    payment.paid_to = create_account(f'{value[35]}(INR)',"Expense", "51000 - Direct Expenses - HPL" ,  'INR')
                    payment.source_exchange_rate = float(f'{value[26].strip()}')
                elif value[6] == "British Pound":
                    currency = "GBP"
                    payment.paid_from = create_account(f'{value[1]}(GBP)',"Expense", "51000 - Direct Expenses - HPL" ,  'GBP')
                    payment.paid_to = create_account(f'{value[35]}(GBP)',"Expense", "51000 - Direct Expenses - HPL" ,  'GBP')
                    payment.source_exchange_rate = float(f'{value[26].strip()}')
                elif value[6] == "Norwegian Krone":
                    currency = "NOK"
                    payment.source_exchange_rate = float(f'{value[26].strip()}')
                if value[13] == '':
                    cost_center = "Main - HPL"
                if value[13] != '':
                    cost_center = f'{value[13]} - HPL',
                payment.custom_payment_type = "Exp Cheque Payment"
                payment.custom_internal_id = value[0]
                payment.custom_period = value[2]
                payment.custom_document_number = value[3]
                payment.custom_subsidiary = value[5]
                payment.custom_memo = value[15]
                payment.custom_location = value[7]
                payment.custom_applied_to_transaction = value[15]
                payment.custom_created_from = value[17]
                payment.custom_line_id = value[33]
                payment.custom_billing_address = value[27]
                payment.custom_applied_to_link_type = value[20]
                payment.custom_created_by = value[4]
                payment.mode_of_payment = "Cheque"	
                payment.posting_date = date_converter_month(value[2])
                payment.paid_to_account_currency  = currency
                payment.paid_from_account_currency = currency
                payment.paid_from_account_balance = total
                payment.paid_to_account_balance = total
                payment.cost_center = cost_center
                payment.paid_amount = total
                payment.received_amount = total
                payment.custom_resubmit = value[24]
                payment.custom_approval_status = value[25]
                payment.reference_no=value[7]
                payment.reference_date = date_converter_month(value[2])
                payment.cost_center = cost_center
                payment.docstatus = 1
                payment.insert()
                frappe.db.commit()
            except Exception as e:
                print(f"{e} {value[0],  value[26]}")




def create_cash_bank():
    with open('/home/doreenalita/frappe/frappe-bench/apps/raindrop/HPL Cash Bank Received Others Income Number 2020_2023 - Sheet1.csv') as design_file:
        reader_po = csv.reader(design_file, delimiter=',')
        for value in reader_po:
            try:
                total = 0.0
                with open('/home/doreenalita/frappe/frappe-bench/apps/raindrop/HPL Cash Bank Received Others Income 2020_2023 - Sheet1.csv') as templates:
                    reader = csv.reader(templates, delimiter=',')
                    for row in reader:
                        if  row[0].strip() == value[0].strip():
                            total = total +  float(row[42].replace(',', '')) 
                payment = frappe.new_doc("Payment Entry")
                payment.payment_type = "Pay"
                
                if value[11].startswith('5'):
                    payment.party_type = "Supplier"
                    payment.party = value[11]
                elif not value[32].startswith('5'):
                    payment.party_type = "Employee"
                    payment.party = employee(value[11])  
                    if 	value[11] == '':
                        payment.party_type = "Supplier"
                        payment.party = "No Supplier"  
                currency = 'NPR'
                if value[5] == "Nepalese Rupee":
                    currency = "NPR"
                    payment.paid_from = f'{value[20]} - HPL'
                    payment.paid_to = f'{value[10]} - HPL'
                elif value[5] == "Euro":
                    currency = "EUR"
                    payment.paid_from = create_account(account=f'{value[20]}(EUR)',root_type="Expense", parent="51000 - Direct Expenses - HPL",  currency='EUR')
                    payment.paid_to = create_account(f'{value[35]}(EUR)',"Expense", "51000 - Direct Expenses - HPL" ,  'EUR')
                    payment.source_exchange_rate = float(f'{value[10].strip()}')
                elif value[5] == "US Dollar":
                    currency = "USD"
                    payment.paid_from = create_account(f'{value[20]}(USD)',"Expense", "51000 - Direct Expenses - HPL" ,  'USD')
                    payment.paid_to = create_account(f'{value[10]}(USD)',"Expense", "51000 - Direct Expenses - HPL" , 'USD')
                    payment.source_exchange_rate = float(f'{value[13].strip()}')
                elif value[5] == "Indian Rupees":
                    currency = "INR"
                    payment.paid_from = create_account(f'{value[20]}(INR)',"Expense", "51000 - Direct Expenses - HPL" ,  'INR')
                    payment.paid_to = create_account(f'{value[10]}(INR)',"Expense", "51000 - Direct Expenses - HPL" ,  'INR')
                    payment.source_exchange_rate = float(f'{value[13].strip()}')
                elif value[5] == "British Pound":
                    currency = "GBP"
                    payment.paid_from = create_account(f'{value[20]}(GBP)',"Expense", "51000 - Direct Expenses - HPL" ,  'GBP')
                    payment.paid_to = create_account(f'{value[10]}(GBP)',"Expense", "51000 - Direct Expenses - HPL" ,  'GBP')
                    payment.source_exchange_rate = float(f'{value[13].strip()}')
                elif value[5] == "Norwegian Krone":
                    currency = "NOK"
                    payment.source_exchange_rate = float(f'{value[13].strip()}')
                if value[7] == '':
                    cost_center = "Main - HPL"
                if value[7] != '':
                    cost_center = f'{value[7]} - HPL',
                payment.custom_payment_type = "Exp Cheque Payment"
                payment.custom_internal_id = value[0]
                payment.custom_document_number = value[2]
                payment.custom_subsidiary = value[4]
                payment.custom_memo = value[9]
                payment.custom_location = value[6]
                payment.custom_applied_to_transaction = value[15]
                payment.custom_created_from = value[17]
                payment.custom_line_id = value[19]
                payment.custom_billing_address = value[14]
                payment.custom_applied_to_link_type = value[20]
                payment.custom_created_by = value[3]
                payment.mode_of_payment = "Cash"	
                payment.posting_date = date_converter_month(value[1])
                payment.paid_to_account_currency  = currency
                payment.paid_from_account_currency = currency
                payment.paid_from_account_balance = total
                payment.paid_to_account_balance = total
                payment.cost_center = cost_center
                payment.paid_amount = total
                payment.received_amount = total
                payment.custom_resubmit = value[24]
                payment.custom_approval_status = value[8]
                payment.reference_no=value[9]
                payment.reference_date = date_converter_month(value[1])
                payment.cost_center = cost_center
                payment.project = create_project(value[18])
                payment.docstatus = 1
                payment.insert()
                frappe.db.commit()
            except Exception as e:
                print(f"{e} {value[0],  value[26]}")


def create_account(account, root_type, parent, currency):
    if not frappe.db.exists('Account', f"{account} - HPL"):
        acc = frappe.new_doc('Account')
        acc.account_name = account
        acc.root_type = root_type
        acc.parent_account = parent
        acc.account_currency = currency
        acc.is_group = 0
        acc.insert(ignore_mandatory=True)
        frappe.db.commit()
    return f'{account} - HPL'

def create_project(project):
    if not frappe.db.exists('Project', project) and project != '':
        pro = frappe.new_doc('Project')
        pro.project_name = project
        pro.insert(ignore_mandatory=True )
        frappe.db.commit()
    return project

def employee(employee):
    if not employee.startswith('5') and employee != '':
        if not frappe.db.exists('Employee', employee):
            emp = frappe.new_doc("Employee")
            emp.first_name  = employee
            emp.insert(ignore_mandatory=True)
            frappe.db.commit()
            frappe.rename_doc('Employee', emp.name, employee)
            frappe.db.commit()
           