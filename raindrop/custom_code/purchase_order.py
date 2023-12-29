import frappe 


def on_update(doc, method):
    frappe.db.set_value('Purchase Order', doc.name, {
    'custom_purchase_approver__id': add_approver(doc.modified_by),
    'custom_initiator_manager': add_approver(doc.custom_email_initiator)
})
    purchase_approver = frappe.db.get_value("Employee", {"user_id":doc.owner}, "custom_purchase_approver_id")
    if purchase_approver == '' or purchase_approver == None and "Administrator"  in frappe.get_roles():
        frappe.throw("Please ask Administrator to set Purchase Approver For you")
    if doc.workflow_state == "Approved":
        total = 0
        for item in doc.items:
            total += item.amount
        limit_amount = frappe.db.get_value("Employee", {"user_id":doc.owner}, "custom_purchase_approval_limit")
        buying =  float(f'{limit_amount.strip()}') 
        if total > buying and  "HPL Purchasing (Lite)" not  in frappe.get_roles() or "General Manager" not  in frappe.get_roles() :
                frappe.throw("The Material Purchase Is Above Limit, Send to General Manager or Immediate Manger ")
               
    

    

@frappe.whitelist()
def add_approver(owner):
    purchase_approver = frappe.db.get_value("Employee", {"user_id":owner}, "custom_purchase_approver_id")
    if purchase_approver != '' or purchase_approver != None:
        return purchase_approver
