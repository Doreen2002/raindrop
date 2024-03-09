import frappe

def purchase_order_query(user):
    if not user:
        user = frappe.session.user
    if frappe.session.user != "Administrator"  or frappe.session.user != "umesh.sharma@hpl.com.np"  or frappe.session.user != "bimala.khadka@hpl.com.np" or frappe.session.user != "surya.karki@hpl.com.np":
        todos = frappe.db.get_list("ToDo", debug=1)
        purchase = frappe.db.get_list("Purchase Order", debug=1)
        return frappe.db.sql("""
        SELECT po.name po.owner td.reference_name td.allocated_to
        FROM `tabToDo` td
        LEFT JOIN `tabPurchase Order` po ON td.reference_name = po.name
        WHERE po.owner = {user} OR td.allocated_to = {user}
        """.format(user=frappe.db.escape(user)))



        #return "(`tabPurchase Order`.owner =   or `tabPurchase Order`.custom_purchase_approver__id = {user}  or `tabPurchase Order`.custom_initiator = {user}  or `tabPurchase Order`.custom_purchase_request_manager = {user} or `tabPurchase Order`.assigned_to in {assigned} )".format(user=frappe.db.escape(user), assigned = assigned)

# def purchase_invoice_query(user):
#     if frappe.session.user != "Administrator"  or frappe.session.user != "umesh.sharma@hpl.com.np"  or frappe.session.user != "bimala.khadka@hpl.com.np" or frappe.session.user != "surya.karki@hpl.com.np" or frappe.session.user != "keshav.kc@hpl.com.np":
#         user = frappe.session.user
#         return "(`tabPurchase Invoice`.owner = {user}  or `tabPurchase Invoice`.custom_purchase_approver__id = {user}  or `tabPurchase Invoice`.custom_purchase_receipt__manager = {user} )".format(user=frappe.db.escape(user))

