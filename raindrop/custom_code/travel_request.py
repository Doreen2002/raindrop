import frappe

def before_insert(doc, method):
    if doc.travel_type == "Domestic":
		doc.custom_travel_request_approver = add_approver(doc.owner, doc.cost_center)
      
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
