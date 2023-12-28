import frappe 


def on_update(doc, method):
    purchase_approver = frappe.db.get_value("Employee", {"user_id":doc.owner}, "custom_purchase_approver_id")
    if purchase_approver == '' or purchase_approver == None and "Administrator"  in frappe.get_roles():
        frappe.throw("Please ask Administrator to set Purchase Approver For you")
    if doc.workflow_state == "Approved":
        total = 0
        for item in doc.items:
            total += item.amount
        buying = frappe.get_doc('Buying Settings')
        if total > buying.custom_purchase_amount_limit and "Purchase Master Manager"  in frappe.get_roles() :
                frappe.throw("The Material Purchase Is Above Limit, Recommend to General Manager ")
                doc.workflow_state = "Pending"
    

    

@frappe.whitelist()
def add_approver(owner):
    purchase_approver = frappe.db.get_value("Employee", {"user_id":owner}, "custom_purchase_approver_id")
    if purchase_approver != '' or purchase_approver != None:
        return purchase_approver
