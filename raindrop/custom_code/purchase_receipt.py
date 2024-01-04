import frappe 



def on_update(doc, method):
    po = doc.items[0].purchase_order
    material = frappe.db.get_value("Purchase Order", po, 'custom_email_initiator')
    material_req = material
    doc.custom_email__initiator = material_req
    purchase_approver = frappe.db.get_value("Employee", {"user_id":doc.owner}, "custom_purchase_approver_id")
    if purchase_approver == '' or purchase_approver == None and "Administrator" not in frappe.get_roles():
        frappe.throw("Please ask Administrator to set Purchase Approver For you")

@frappe.whitelist()
def add_approver(owner):
    purchase_approver = frappe.db.get_value("Employee", {"user_id":owner}, "custom_purchase_approver_id")
    if purchase_approver != '' or purchase_approver != None:
        return purchase_approver
       
    

