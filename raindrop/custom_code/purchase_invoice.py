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
              
            