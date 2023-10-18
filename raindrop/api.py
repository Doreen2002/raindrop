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
    url = "http://34.138.131.178/files/NPR Item Master Final (1) - Sheet1.csv" 
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
    url = "http://34.138.131.178/files/NPR Item Master Final (1) - Sheet1.csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
        try:
            if row[1] != '' and  not frappe.db.exists('Item Group', row[1]):
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
    url = "http://34.138.131.178/files/NPR Item Master Final (1) - Sheet1.csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
        try:
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
    url = "http://34.138.131.178/files/NPR Item Master Final (1) - Sheet1.csv" 
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
    url = "http://34.138.131.178/files/NPR Item Master Final (1) - Sheet1.csv" 
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
    url = "http://34.138.131.178/files/NPR Item Master Final (1) - Sheet1.csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
        try:
            doc = frappe.new_doc('Item') 
            doc.custom_internal_id = row[8].strip()
            doc.item_name = row[11].strip()
            doc.item_code = f'{row[9].strip()} {row[11].strip()}' 
            doc.item_group = row[5].strip()
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
            doc.stock_uom = row[37].strip()
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
    url = "http://34.138.131.178/files/NPR Item Master Final (1) - Sheet1.csv" 
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
    url = "http://34.138.131.178/files/HPL Vendor Master Final - Sheet1.csv" 
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
    url = "http://34.138.131.178/files/HPL Vendor Master Final - Sheet1.csv" 
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
    url = "http://34.138.131.178/files/HPL Vendor Master Final - Sheet1.csv" 
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

puchase_order_number = []
def append_po_number():
    url = "http://34.138.131.178/files/HPL PO Transactio NPR - Sheet1.csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
        try:
            puchase_order_number.append(row[2])
        except Exception as e:
            print(f'{e}')

def create_purchase_order():
    qty = 0
    rate = 0
    amount = 0
    url = "http://34.138.131.178/files/HPL PO Transactio NPR - Sheet1.csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
        try:
            doc = frappe.new_doc('Purchase Order')
            doc.supplier = row[7].strip()
            if row[44] != '':
                qty = row[44].strip()
            if row[45] != '':
                rate = row[45].strip()
            if row[39] != '':
                amount = row[39].strip()
            for val in puchase_order_number:
                if row[2] == val:
                    doc.append("items", {
                                "item_code": row[43].strip(),
                                "qty": qty,
                                "rate": rate,
                                "amount":rate,
                                }
                            )
            doc.insert(ignore_mandatory=True, ignore_links=True)
            frappe.db.commit()
        except Exception as e:
            print(f'{e}')
