import frappe

def purchase_order_query(user, assigned=None):
    if frappe.session.user != "Administrator"  or frappe.session.user != "umesh.sharma@hpl.com.np"  or frappe.session.user != "bimala.khadka@hpl.com.np" or frappe.session.user != "surya.karki@hpl.com.np":
        user = frappe.session.user
        assigned = frappe.db.get_list("ToDo", pluck='allocated_to')
        return "(`tabPurchase Order`.owner = {user}  or `tabPurchase Order`.custom_purchase_approver__id = {user}  or `tabPurchase Order`.custom_initiator = {user}  or `tabPurchase Order`.custom_purchase_request_manager = {user} or {user} IN {assigned} )".format(user=frappe.db.escape(user), assigned = assigned)

# def purchase_invoice_query(user):
#     if frappe.session.user != "Administrator"  or frappe.session.user != "umesh.sharma@hpl.com.np"  or frappe.session.user != "bimala.khadka@hpl.com.np" or frappe.session.user != "surya.karki@hpl.com.np" or frappe.session.user != "keshav.kc@hpl.com.np":
#         user = frappe.session.user
#         return "(`tabPurchase Invoice`.owner = {user}  or `tabPurchase Invoice`.custom_purchase_approver__id = {user}  or `tabPurchase Invoice`.custom_purchase_receipt__manager = {user} )".format(user=frappe.db.escape(user))

