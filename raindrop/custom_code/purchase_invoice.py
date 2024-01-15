import frappe 
import json

def on_submit(doc, method):
    items = []
    
    for tax in doc.taxes:
        for item_val in doc.items:
            items.append(
                        {
                        'party_type': 'Supplier',
                        'party': doc.supplier,
                        'account': item_val.expense_account,
                        'debit_in_account_currency': item_val.base_net_amount * tax.rate/100,
                        'credit_in_account_currency':0,
                        'cost_center':doc.cost_center,
                        'account_currency': doc.currency
                        }
                    )
            items.append(
                        {
                        'party_type': 'Supplier',
                        'party': doc.supplier,
                        'account': tax.account_head,
                        'debit_in_account_currency':0,
                        'credit_in_account_currency':item_val.base_net_amount * tax.rate/100,
                        'cost_center':doc.cost_center,
                        'account_currency': doc.currency
                        }
                    )
    journal = frappe.new_doc('Journal Entry')
    journal.posting_date = doc.posting_date
    journal.multi_currency = 1
    for item in items:
        journal.append('accounts', item)
    journal.docstatus = 1
    journal.insert()
    frappe.db.commit()
    doc.custom_journal_entry= journal.name

def on_update(doc, method):
    #get logged emloyee ID
    employee = frappe.db.get_value("Employee", {"user_id":doc.owner}, "name")
    #get logged supervisor at particular cost center
    purchase_approver = frappe.db.get_value("Employee Cost Center Manager", {"parent":employee, "cost_center":doc.custom_cost_center}, "supervisor")
    if purchase_approver == '' or purchase_approver == None and "Administrator" not in frappe.get_roles():
        frappe.throw("Please ask Administrator to set Purchase Approver For you")

@frappe.whitelist()
def add_approver(owner, custom_cost_center):
    #get logged emloyee ID
    employee = frappe.db.get_value("Employee", {"user_id":owner}, "name")
    #get logged supervisor at particular cost center
    purchase_approver = frappe.db.get_value("Employee Cost Center Manager", {"parent":employee, "cost_center":custom_cost_center}, "supervisor")
    if purchase_approver != '' or purchase_approver != None:
        return purchase_approver
        
@frappe.whitelist()
def get_approver(owner):
    approver_list = []
    employee = frappe.db.get_value("Employee", {"user_id":owner}, "name")
    approvers = frappe.db.get_all("Employee Cost Center Manager", filters={"parent":employee}, fields=['*'])
    if approvers == []:
        frappe.throw("Please ask Administrator to set Purchase Approver For you")
    for appr in approvers:
        approver_list.append(appr.cost_center)
    return approver_list
              
            
