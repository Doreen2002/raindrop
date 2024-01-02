import frappe 

def before_insert(doc, method):
    
    doc.custom_purchase_approver__id = add_approver(doc.modified_by)
    doc.custom_initiator_manager = add_approver(doc.custom_email_initiator)
    doc.custom_purchase_request_manager = add_approver(doc.owner)

    
def on_update(doc, method):
    purchase_approver = frappe.db.get_value("Employee", {"user_id":doc.owner}, "custom_purchase_approver_id")
    if purchase_approver == '' or purchase_approver == None and "Administrator"  in frappe.get_roles():
        frappe.throw("Please ask Administrator to set Purchase Approver For you")
    if doc.workflow_state == "Approved":
        total = 0
        for item in doc.items:
            total += item.amount
        limit_amount = frappe.db.get_value("Employee", {"user_id":doc.owner}, "custom_purchase_approval_limit")
        buying =  float(f'{limit_amount.strip()}') 
        if "General Manager" not  in frappe.get_roles() :
            if total > buying:
                    frappe.throw("The Material Purchase Is Above Limit, Send to General Manager or Immediate Manger ")
               
    

    

@frappe.whitelist()
def add_approver(owner):
    purchase_approver = frappe.db.get_value("Employee", {"user_id":owner}, "custom_purchase_approver_id")
    if purchase_approver != '' or purchase_approver != None:
        return purchase_approver
