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
    url = "https://hpl.raindropinc.com/files/chart_of_account_error_rows - Sheet1.csv" 
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
    url = "https://hpl.raindropinc.com/files/NPR Item Master Final (1) - Sheet1.csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
         try:
             if row[0] != '' and  not frappe.db.exists('Item Group', row[0]):
                doc = frappe.new_doc('Item Group')
                doc.item_group_name = row[0]
                doc.is_group = 1
                doc.insert(ignore_mandatory=True, ignore_links=True)
                frappe.db.commit()
         except Exception as e:
             print(f'{e}')

@frappe.whitelist()
def create_second_item_group():
    url = "https://hpl.raindropinc.com/files/NPR Item Master Final (1) - Sheet1.csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
        try:
            if row[1] != '' and  not frappe.db.exists('Item Group', row[1]):
                doc = frappe.new_doc('Item Group')
                doc.item_group_name = row[1]
                doc.is_group = 1
                doc.parent_item_group = row[0]
                doc.insert(ignore_mandatory=True, ignore_links=True)
                frappe.db.commit()
        except Exception as e:
            print(f'{e}')

@frappe.whitelist()
def create_third_item_group():
    url = "https://hpl.raindropinc.com/files/NPR Item Master Final (1) - Sheet1.csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
        try:
            doc = frappe.new_doc('Item Group')
            if row[2] != '' and  not frappe.db.exists('Item Group', row[2]):
                doc.item_group_name = row[2]
                doc.is_group = 1
                doc.parent_item_group = row[1]
                doc.insert(ignore_mandatory=True, ignore_links=True)
            frappe.db.commit()
        except Exception as e:
            print(f'{e}')

@frappe.whitelist()
def create_uom():
    url = "https://hpl.raindropinc.com/files/NPR Item Master Final (1) - Sheet1.csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
        try:
            doc = frappe.new_doc('UOM')
            doc.uom_name = row[37]
            doc.enabled = 1
            doc.insert(ignore_mandatory=True, ignore_links=True)
            frappe.db.commit()
        except Exception as e:
            print(f'{e}')

@frappe.whitelist() 
def create_item():
    url = "https://hpl.raindropinc.com/files/NPR Item Master Final (1) - Sheet1.csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
        try:
            doc = frappe.new_doc('Item')
            doc.internal_id = row[8]
            doc.item_name = row[6]
            doc.item_code = f'{row[9]} {row[11]}' 
            doc.item_group = row[5]
            doc.parent = row[10]
            doc.display_name = row[11]
            doc.description = row[12]
            doc.type = row[13]
            doc.sub_type = row[14]
            doc.standard_rate = row[15]
            doc.item_collection = row[16]
            doc.jobtech_code = row[17]
            doc.old_item_code = row[18]
            doc.ups_code = row[19]
            doc.vendor = row[20]
            doc.offer_support = row[21]
            doc.cost_center = row[22]
            if row[13] == "Inventory Item":
                doc.stock_item= 1
            if row[13] != "Inventory Item":
               doc.stock_item= 0
            if row[23] == "No":
                doc.disabled= 0
            if row[23] == "Yes":
                doc.disabled= 1
            doc.costing_method = row[34]
            doc.valuation_method = row[34]
            doc.uom = row[37]
            doc.purchase_uom = row[37]
            doc.sales_uom = row[37]
            doc.primary_units_type = row[41]
            doc.tax_schedule = row[33]
            doc.subsidiary = row[45]
            doc.include_children = row[46]
            doc.location = row [47]
            doc.insert(ignore_mandatory=True, ignore_links=True)
            frappe.db.commit()
        except Exception as e:
            print(f'{e}')
  
               
def create_price_list():
    url = "https://hpl.raindropinc.com/files/NPR Item Master Final (1) - Sheet1.csv" 
    response = requests.get(url)
    content = response.content.decode('utf-8')
    reader = csv.reader(content.splitlines(), delimiter=',')
    for row in reader:
        try:
            doc = frappe.new_doc('Item Price')
            doc.item_code =  f'{row[9]} {row[11]}'
            doc.price_list = "Standard Buying"
            doc.price_list_rate = row[43]
            doc.insert(ignore_mandatory=True, ignore_links=True)
            frappe.db.commit()
        except Exception as e:
            print(f'{e}')

            
          


       



