import frappe
import csv

from raindrop.api import date_converter, date_converter_month
#jounar entry

def create_jounal_entry_2013():
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

def create_sales_invoice_2013():
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


def create_opening_balance_2013():
    with open('/home/doreenalita/frappe/frappe-bench/apps/raindrop/HPL Inventory Opening Number 2013 - Sheet1.csv' ) as design_file:
        reader_po = csv.reader(design_file, delimiter=',')
        for value in reader_po:
            try:
                items = []
                with open('/home/doreenalita/frappe/frappe-bench/apps/raindrop/HPL Inventory Opening 2013 - Sheet1.csv'  ) as templates:
                    reader = csv.reader(templates, delimiter=',')
                    for row in reader:
                        if row[0] == value[0]:
                            if not frappe.db.exists('Item Group',frappe.db.get_value('Item',{'name': ['like', f'%{row[13]}%']}, 'item_group') ):
                                item_group = frappe.new_doc('Item Group')
                                item_group.item_group_name = frappe.db.get_value('Item', {'name': ['like', f'%{row[13]}%']}, 'item_group') 
                                item_group.insert()
                                frappe.db.commit()
                            frappe.db.set_value('Item', {'name': ['like', f'%{row[13]}%']}, 'is_stock_item', 1)
                            frappe.db.commit()
                            items.append(
                                {
                            "t_warehouse": f"{row[12]} - HPL",
                            "item_code":  frappe.db.get_value('Item', {'name': ['like', f'%{row[13]}%']}, 'name'),
                            "qty":row[15],
                            "expense_account": frappe.db.get_value('Account', {'name': ['like', f'%{value[4]}%']}, 'name'),
                            "description":row[5],
                            "basic_rate": row[16],
                            "cost_center" : f"{row[9]} - HPL"
                        }
                            )
               
                doc = frappe.new_doc("Stock Entry")
                doc.stock_entry_type = "Material Receipt"
                doc.custom_internal_id = value[0]
                doc.custom_document_number = value[2]
                doc.custom_subsidiary = value[7]
                doc.set_posting_time = 1
                doc.posting_date = date_converter_month(value[1])
                for item in items:
                    doc.append('items', item)
                doc.docstatus = 1
                frappe.db.set_value('Company', "Himal Power Limited", 'default_inventory_account', f'{row[3]} - HPL')
                frappe.db.commit()
                doc.insert()
                frappe.db.commit()
            except Exception as e:
                    print(f'{e} {value[0]} ')


def create_purchase_invoice_2020():
    with open( '/home/frappe/frappe-bench/apps/raindrop/HPL Purchase Invoice Number NPR 2020_2013 - Sheet1 (1).csv') as design_file:
        reader_po = csv.reader(design_file, delimiter=',')
        for value in  reader_po:
            try:
                items = []
                taxes = []
                tax_template = []
                with open('/home/frappe/frappe-bench/apps/raindrop/HPL Purchase Invoice NPR 2020_2013 - Sheet1 (3).csv' ) as templates:
                    reader = csv.reader(templates, delimiter=',')
                    for row in reader:
                        cost_center = "Main - HPL"
                        if row[45] != '':
                            cost_center = f"{row[45]} - HPL"
                        if row[0] == value[0] and  not 'TDS' in row[39] and row[39] != '' :
                            name = frappe.db.get_value("Purchase Order", {"custom_document_number":row[52]}, 'name')
                            if row[38] != '0%':
                                tax_template.append(row[38])
                            items.append(
                                {
                                "item_code": frappe.db.get_value("Item", {"custom_name":row[39]}, 'name'),
                                "rate":row[40],
                                "qty":row[43],
                                "cost_center": cost_center,
                                "expense_account":f"{row[35]} - HPL",
                                "description":row[15],
                                "purchase_order": frappe.db.get_value("Purchase Order", {"custom_document_number":row[52]}, 'name'),
                                "purchase_order_item": frappe.db.get_value("Purchase Order Item", {"parent":name}, 'name'),
                                "project":create_project(row[31])
                                }
                            
                            )
                        if row[0] == value[0] and row[39] == '' and not 'TDS' in row[35]:
                            items.append(
                                    {
                                    "item_code":"Virtual Item",
                                    "rate":row[55],
                                    "qty":1,
                                    "cost_center": cost_center,
                                    "expense_account":f"{row[35]} - HPL",
                                    "description":row[15],
                                        }
                                        )
                        
                        if row[0] == value[0]:
                            if 'TDS' in row[39] or 'TDS' in row[35]:
                                if row[39] != '':
                                    taxes.append(
                                    {
                                        'charge_type':"Actual",
                                        "add_deduct_tax":"Deduct",
                                        'rate':0,
                                        "tax_amount":row[40],
                                        "account_head":f"{row[35]} - HPL",
                                        "description":value[15]
                                            })
                                if row[39] == '':
                                    taxes.append(
                                    {
                                        'charge_type':"Actual",
                                        "add_deduct_tax":"Add",
                                        'rate':0,
                                        "tax_amount":row[55],
                                        "account_head":f"{row[35]} - HPL",
                                        "description":value[15]
                                            })
                                    

                doc = frappe.new_doc("Purchase Invoice")
                doc.custom_bill_number = value[1]
                doc.custom_internal_id = value[0]
                doc.set_posting_time = 1
                doc.posting_date = date_converter_month(value[2])
                doc.custom_document_number = value[3]
                doc.custom_created_by = value[4]
                doc.custom_subsidiary = value[5]
                doc.supplier = value[32]
                for item in items:
                    doc.append('items', item)
                if taxes != []:
                    for tax in taxes:
                        doc.append('taxes', tax)
                if tax_template != []:
                    if tax_template[-1] != '0%':
                        doc.taxes_and_charges = "Nepal Tax - HPL"
                        doc.append('taxes',
                        {
                            'charge_type':"On Net Total",
                            "rate":13,
                            "account_head":"VAT - HPL",
                            "description":value[15]
                                })
                if value[6] == "Nepalese Rupee":
                    doc.currency = "NPR"
                    doc.conversion_rate = value[26]
                elif value[6] == "Euro":
                    doc.currency = "EUR"
                    doc.conversion_rate = value[26]
                elif value[6] == "US Dollar":
                    doc.currency = "USD"
                    doc.conversion_rate = value[26]
                elif value[6] == "Indian Rupees":
                    doc.currency = "INR"
                    doc.conversion_rate = value[26]
                elif value[6] == "British Pound":
                    doc.currency = "GBP"
                    doc.conversion_rate = value[26]
                elif value[6] == "Norwegian Krone":
                    doc.currency = "NOK"
                    doc.conversion_rate = value[26]
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
                
                doc.custom_procurement_person = value[16]
                doc.terms = value[10]
                doc.rounding_adjustment = 0
                doc.custom_billing_address = value[27]
                doc.project = value[31]
                doc.custom_shipping_address = value[28]
                doc.custom_accounting_approval  = value[25]
                doc.custom_resubmit = value[24]
                doc.custom_match_bill_to_receipt = value[49]
                doc.custom_vendor_price_ref_date = value[19] 
                doc.custom_current_approval = value[23]
                doc.custom_vendor = value[18]
                doc.custom_line_id = value[33]
                doc.disable_rounded_total = 1
                doc.submit()
                frappe.db.commit()
            
            except Exception as e:
                print(f' {e}  {value[0]}')



def create_employee_expenses_2013():
    with open( '/home/frappe/frappe-bench/apps/raindrop/HPL_Employee_Expenses_report Number 2013_2020 - Sheet1.csv') as design_file:
        reader_po = csv.reader(design_file, delimiter=',')
        for value in reader_po:
            try:
                items = []
                with open('/home/frappe/frappe-bench/apps/raindrop/HPL_Employee_Expenses_report 2013_2020.xlsx - Sheet1.csv') as templates:
                    reader = csv.reader(templates, delimiter=',')
                    for row in reader:
                        if row[0]  == value[0] and row[12] != '':
                            if not frappe.db.exists('Expense Claim Type', row[11]):
                                exp = frappe.new_doc("Expense Claim Type")
                                exp.expense_type = row[11]
                                exp.append("accounts", {
                                    "company":frappe.db.get_list('Company', pluck='name')[0],
                                    "default_account":frappe.db.get_value('Account', {'name': ['like', f'%{value[11]}%']}, 'name')
                                })
                                exp.insert()
                                frappe.db.commit()

                            items.append(
                                {
                                    "expense_type": row[11],
                                    "expense_date": date_converter_month(row[1]) ,
                                    "custom_memo":row[7],
                                    "description":row[7],
                                    "cost_center":f'{row[14]} - HPL',
                                    "custom_receipt":row[17],
                                    "custom_ref_no":row[18],
                                    "custom_name":row[19],
                                    "amount": row[20].strip().replace('(', '').replace(')', ''),
                                     "sanctioned_amount": row[20].strip().replace('(', '').replace(')', '')
                                }
                                
                            )
                if items != []:
                    doc = frappe.new_doc("Expense Claim")
                    frappe.db.set_value('Employee', frappe.db.get_value('Employee', {'name': ['like', f'%{value[3]}%']}, 'name'), 'status', 'Active')
                    frappe.db.commit()
                    doc.employee = frappe.db.get_value('Employee', {'name': ['like', f'%{value[3]}%']}, 'name')
                    doc.custom_internal_id = value[0]
                    doc.custom_document_number = value[2]
                    doc.custom_subsidiary = value[4]
                    doc.custom_period = value[5]
                    doc.custom_line_id = value[10]
                    doc.custom_memo_main = value[6]
                    doc.custom_location = value[15]
                    doc.approval_status = "Approved"
                    doc.payable_account = "24000 - AccountPayable - HPL"
                    for item in items:
                        doc.append('expenses', item)
                    if value[21].strip() == '13%':
                        doc.append('taxes',{
                            "account_head":"25001 - VATOutput USD - HPL",
                            "rate":13
                        })
                        
                    doc.docstatus = 1
                    doc.insert(ignore_mandatory=True)
                    frappe.db.commit()
            except Exception as e:
                print(f'{e} {value[0]} ')



def create_account(account, root_type, parent, currency):
    try:
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
    except Exception as e:
        print(f'{e} {account}')
def create_project(project):
    if not frappe.db.exists('Project', project) and project != '':
        pro = frappe.new_doc('Project')
        pro.project_name = project
        pro.insert(ignore_mandatory=True )
        frappe.db.commit()
    return project

#suppler payment
def create_supplier_payment_2013():
    with open(  '/home/frappe/frappe-bench/apps/raindrop/Supplier Payment Number 2013_2020.xlsx - Sheet1 (1).csv') as design_file:
        reader_po = csv.reader(design_file, delimiter=',')
        for value in reader_po:
            try:
                total = 0.0
                with open('/home/frappe/frappe-bench/apps/raindrop/Supplier Payment 2013_2020.xlsx - Sheet1.csv' ) as templates:
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
                    payment.party = employee(value[4])
                    payment.paid_from = "2110 - Creditors - HPL"
                    payment.paid_to = f'{value[6]} - HPL'
                exchange = 1
                currency = 'NPR'
                if value[13] == "Nepalese Rupee":
                    currency = "NPR"
                elif value[13] == "Euro":
                    currency = "EUR"
                    exchange = value[14]
                elif value[13] == "US Dollar":
                    currency = "USD"
                    exchange = value[14]
                elif value[13] == "Indian Rupees":
                    currency = "INR"
                    exchange = value[14]
                elif value[13] == "British Pound":
                    currency = "GBP"
                    exchange = value[14]
                elif value[13] == "Norwegian Krone":
                    currency = "NOK"
                    exchange = value[14]
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
                payment.custom_created_by = value[23]
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
                print(f"{e} {value[0]} {total}")

def employee(employee):
    if not employee.startswith('5') and employee != '':
        if not frappe.db.exists('Employee', employee):
            emp = frappe.new_doc("Employee")
            emp.first_name  = employee
            emp.insert(ignore_mandatory=True)
            frappe.db.commit()
            frappe.rename_doc('Employee', emp.name, employee)
            frappe.db.commit()
    return employee


#bank transfer 
def create_bank_transfer_2013():
    with open('/home/frappe/frappe-bench/apps/raindrop/Bank Transfer (Contra Voucher)  Number 2013_2020 (1) - Sheet1.csv') as design_file:
        reader_po = csv.reader(design_file, delimiter=',')
        for value in reader_po:
            try:
                items = []
                row_number = 5
                doc = frappe.new_doc('Journal Entry')
                with open('/home/frappe/frappe-bench/apps/raindrop/Bank Transfer (Contra Voucher) 2013_2020 (1) - Sheet1.csv' ) as templates:
                    reader = csv.reader(templates, delimiter=',')
                    items.clear()
                    for row in reader:
                        
                        if  row[0].strip() == value[0].strip():
                            
                            cost_center = "Main - HPL"
                            if row[15] != '':
                                cost_center = f'{row[15]} - HPL'
                            currency = "NPR"
                            if row[6] == "NPR":
                                currency = "NPR"
                                doc.multi_currency = 1
                                items.append(
                                    {
                                        
                                        'account': create_account(account=f'{row[row_number]}',root_type="Expense", parent="51000 - Direct Expenses - HPL",  currency='NPR'),
                                       'debit_in_account_currency':row[8],
                                        'credit_in_account_currency':row[7],
                                        'user_remark': row[16],
                                        'cost_center':cost_center,
                                        'exchange_rate': row[18],
                                        "account_currency":currency
                                    })
                                row_number -=1
                            if row[6] == "Eur":
                                currency = "EUR"
                                account = create_account(account=f'{row[row_number]}(EUR)',root_type="Expense", parent="51000 - Direct Expenses - HPL",  currency='EUR')
                                doc.multi_currency = 1
                            if row[6] == "USD":
                                currency = "USD"
                                doc.multi_currency = 1
                                items.append(
                                    {
                                        
                                        'account': create_account(f'{row[row_number]}(USD)',"Expense", "51000 - Direct Expenses - HPL" ,  'USD'),
                                        'debit_in_account_currency':row[8],
                                        'credit_in_account_currency':row[7],
                                        'user_remark': row[16],
                                        'cost_center':cost_center,
                                        'exchange_rate': row[18],
                                        "account_currency":"USD"
                                    })
                                row_number -=1
                            if row[6] == "INR":
                                currency = "INR"
                                account = create_account(f'{row[row_number]}(INR)',"Expense", "51000 - Direct Expenses - HPL" ,  'INR')   
                                doc.multi_currency = 1
                            if row[6] == "GBP":
                                currency = "GBP"
                                doc.multi_currency = 1
                            if row[6] == "NOK":
                                currency = "NOK"
                                doc.multi_currency = 1
                                items.append(
                                    {
                                        
                                        'account': create_account(f'{row[row_number]}(NOK)',"Expense", "51000 - Direct Expenses - HPL" ,  'NOK'),
                                        'debit_in_account_currency':row[8],
                                        'credit_in_account_currency':row[7],
                                        'user_remark': row[16],
                                        'cost_center':cost_center,
                                        'exchange_rate': row[18],
                                        "account_currency":currency
                                    })
                                row_number -=1
                                    
                    
                        
                        
                       
                
                doc.multi_currency = 1
                doc.custom_internal_id = value[0]
                doc.posting_date = date_converter_month(value[2])
                doc.custom_subsidiary = value[13]
                for item in items:  
                    doc.append('accounts', item)
                doc.custom_transaction_type = "Bank Transfer"
                doc.user_remark = value[10]
                doc.custom_document_number = value[1]
                doc.custom_location = value[14]
                doc.custom_period =  value[12]
                doc.docstatus = 1
                doc.insert(ignore_mandatory=True)
                frappe.db.commit()
            except Exception as e:
                print(f'{e} {value[1]} ')



# cheque payment
def create_cheque_payment_2013():
    with open( '/home/frappe/frappe-bench/apps/raindrop/Exp Cheq Payment  Number 2013_2020 - Sheet1 (1).csv' ) as design_file:
        reader_po = csv.reader(design_file, delimiter=',')
        for value in reader_po:
            try:
                total = 0.0
                with open('/home/doreenalita/frappe-bench2/apps/raindrop/Exp Cheq Payment 2013_2020 - Sheet1 (1).csv') as templates:
                    reader = csv.reader(templates, delimiter=',')
                    for row in reader:
                        if  row[0].strip() == value[0].strip():
                            total = total +  float(row[55].replace(',', '')) 
                payment = frappe.new_doc("Payment Entry")
                payment.payment_type = "Pay"	
                if value[33].startswith('5'):
                    payment.party_type = "Supplier"
                    payment.party = value[33]
                elif not value[33].startswith('5'):
                    payment.party_type = "Employee"
                    payment.party = value[33]     
                currency = 'NPR'
                if value[6] == "Nepalese Rupee":
                    currency = "NPR"
                    payment.paid_from = f'{value[1]} - HPL'
                    payment.paid_to = f'{value[35]} - HPL'
                elif value[6] == "Euro":
                    currency = "EUR"
                    payment.paid_from = create_account(account=f'{value[1]}(EUR)',root_type="Expense", parent="51000 - Direct Expenses - HPL",  currency='EUR')
                    payment.paid_to = create_account(f'{value[35]}(EUR)',"Expense", "51000 - Direct Expenses - HPL" ,  'EUR')
                    payment.source_exchange_rate = float(f'{value[27].strip()}')
                elif value[6] == "US Dollar":
                    currency = "USD"
                    payment.paid_from = create_account(f'{value[1]}(USD)',"Expense", "51000 - Direct Expenses - HPL" ,  'USD')
                    payment.paid_to = create_account(f'{value[35]}(USD)',"Expense", "51000 - Direct Expenses - HPL" , 'USD')
                    payment.source_exchange_rate = float(f'{value[27].strip()}')
                elif value[6] == "Indian Rupees":
                    currency = "INR"
                    payment.paid_from = create_account(f'{value[1]}(INR)',"Expense", "51000 - Direct Expenses - HPL" ,  'INR')
                    payment.paid_to = create_account(f'{value[35]}(INR)',"Expense", "51000 - Direct Expenses - HPL" ,  'INR')
                    payment.source_exchange_rate = float(f'{value[27].strip()}')
                elif value[6] == "British Pound":
                    currency = "GBP"
                    payment.paid_from = create_account(f'{value[1]}(GBP)',"Expense", "51000 - Direct Expenses - HPL" ,  'GBP')
                    payment.paid_to = create_account(f'{value[35]}(GBP)',"Expense", "51000 - Direct Expenses - HPL" ,  'GBP')
                    payment.source_exchange_rate = float(f'{value[27].strip()}')
                elif value[6] == "Norwegian Krone":
                    currency = "NOK"
                    payment.source_exchange_rate = float(f'{value[27].strip()}')
                if value[14] == '':
                    cost_center = "Main - HPL"
                if value[14] != '':
                    cost_center = f'{value[14]} - HPL',
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


def create_cash_bank_2013():
    with open('/home/doreenalita/frappe/frappe-bench/apps/raindrop/HPL Cash Bank Received Others Income  Numbern2013_2020 - Sheet1.csv' ) as design_file:
        reader_po = csv.reader(design_file, delimiter=',')
        for value in reader_po:
            try:
                total = 0.0
                with open('/home/doreenalita/frappe/frappe-bench/apps/raindrop/HPL Cash Bank Received Others Income 2013_2020 - Sheet1.csv' ) as templates:
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
                payment.custom_payment_type = "Cash Bank Received Others Income"
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