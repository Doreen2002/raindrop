import frappe 
from frappe.utils import today

def on_update(doc, method):
    purchase_approver = frappe.db.get_value("Employee", {"user_id":doc.owner}, "custom_purchase_approver_id")
    if purchase_approver == '' or purchase_approver == None:
        frappe.throw("Please ask Administrator to set Purchase Approver For you")
    if purchase_approver != '' or purchase_approver != None:
        doc.custom_purchase_approver__id = purchase_approver


            
                    
