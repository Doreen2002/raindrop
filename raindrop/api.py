import frappe
from datetime import datetime
import datetime as real_Date
import nepali_datetime
import pandas as pd


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

    with open('https://hpl.raindropinc.com/files/HPL_COA_FINAL_NPR (3) - Sheet1 (1).csv', 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            try:
                doc = frappe.new_doc('Account')
                doc.account_type = row[1]
                doc.root_type = row[2]
                doc.report_type = row[3]
                doc.internal_id = row[4]
                doc.account_number = row[5]
                doc.account_name = row[6]
                doc.display_name = row[7]
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
            
          
@frappe.whitelist()
def update_account_naming():
    account_like_name = ['1100 - Cash In Hand - HPL']
    for value in account_like_name:
        name = frappe.db.get_list('Account',  filters= {'name': value}, pluck='name')
        print(name)
        doc = frappe.get_doc('Account', name[0])
        doc.name = '11000 - 19300 - Cash In Hand - HPL'
        doc._save()
        frappe.db.commit()

       



