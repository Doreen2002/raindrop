import frappe 

def on_cancel(doc, method):
    doc.workflow_state = "Cancelled"

def before_insert(doc, method):
    if doc.custom_initiator != None:
        doc.owner = doc.custom_initiator
    doc.custom_purchase_approver__id = add_approver(doc.modified_by, doc.cost_center)
    doc.custom_initiator_manager = add_approver(doc.owner, doc.cost_center)
    doc.custom_purchase_request_manager = add_approver(doc.owner, doc.cost_center)
    if doc.workflow_state != "Draft" and  "General Manager" not  in frappe.get_roles() :
         doc.custom_purchase_approver__id = get_single_approver(doc.modified_by)[0].supervisor

    
def on_update(doc, method):
    
    #get logged emloyee ID
    employee = frappe.db.get_value("Employee", {"user_id":doc.owner}, "name")
    #get logged supervisor at particular cost center
    purchase_approver = frappe.db.get_value("Employee Cost Center Manager", {"parent":employee, "cost_center":doc.cost_center}, "supervisor")
    if purchase_approver == '' or purchase_approver == None and "Administrator" not in frappe.get_roles():
        frappe.throw("Please ask Administrator to set Purchase Approver For you")
    if doc.workflow_state == "Approved":
        total = 0
        limit_amount = 0
        for item in doc.items:
            total += item.amount
        
        limit_amount += frappe.db.get_value("Employee", {"user_id": frappe.session.user}, "custom_purchase_limit") 
        if "General Manager" not  in frappe.get_roles() :
            if total > limit_amount :
                    frappe.throw(f"The Material Purchase Is Above Limit, Send to General Manager or Immediate Manger. Limit is {limit_amount } and total amount on PO is {total} ")
               
    

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
    
@frappe.whitelist()
def get_single_approver(owner):
    approver_list = []
    employee = frappe.db.get_value("Employee", {"user_id":owner}, "name")
    approvers = frappe.db.get_all("Employee Cost Center Manager", filters={"parent":employee}, fields=['*'])
    return approvers







