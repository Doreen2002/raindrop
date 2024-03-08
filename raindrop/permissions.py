def purchase_order_query():
    if frappe.session.user != "Administrator"  or frappe.session.user != "umesh.sharma@hpl.com.np"  or frappe.session.user != "bimala.khadka@hpl.com.np" or frappe.session.user != "surya.karki@hpl.com.np":
        user = frappe.session.user
        return "(`tabPurchase Order`.owner = {user}  or `tabPurchase Order`.custom_purchase_approver__id = {user}  or `tabPurchase Order`.custom_initiator = {user}  or `tabPurchase Order`.custom_purchase_request_manager = {user} )".format(user=frappe.db.escape(user))
