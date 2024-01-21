import frappe 
from frappe.utils import today
from frappe.utils import cint, cstr, flt, get_link_to_form, getdate, new_line_sep, nowdate
from frappe import _, msgprint

def get_mr_items_ordered_qty(doc, mr_items):
    mr_items_ordered_qty = {}
    mr_items = [d.name for d in doc.get('items') if d.name in mr_items]

    doctype = qty_field = None
    if self.material_request_type in ('Material Issue',
            'Material Transfer', 'Customer Provided'):
        doctype = frappe.qb.DocType('Stock Entry Detail')
        qty_field = doctype.transfer_qty
    elif doc.material_request_type == 'Manufacture':
        doctype = frappe.qb.DocType('Work Order')
        qty_field = doctype.qty

    if doctype and qty_field:
        query = \
            frappe.qb.from_(doctype).select(doctype.material_request_item,
                Sum(qty_field)).where((doctype.material_request
                == self.name)
                & doctype.material_request_item.isin(mr_items)
                & (doctype.docstatus
                == 1)).groupby(doctype.material_request_item)

        mr_items_ordered_qty = frappe._dict(query.run())

    return mr_items_ordered_qty


def update_completed_qty(doc, method):
    mr_items = None
    doc = frappe.get_doc("Material Request", doc.items[0].material_request)
    if doc.material_request_type == 'Purchase':
        return

    if not mr_items:
        mr_items = [d.name for d in doc.items]

    mr_items_ordered_qty = get_mr_items_ordered_qty(frappe.get_doc("Material Request", doc.name), mr_items)
    mr_qty_allowance = frappe.db.get_single_value('Stock Settings',
            'mr_qty_allowance')

    for d in doc.items:
        if d.name in mr_items:
            if doc.material_request_type in ('Material Issue',
                    'Material Transfer', 'Customer Provided'):
                d.ordered_qty = flt(mr_items_ordered_qty.get(d.name))

                if mr_qty_allowance:
                    allowed_qty = flt(d.qty + d.qty * (mr_qty_allowance
                            / 100), d.precision('ordered_qty'))

                    if d.ordered_qty and d.ordered_qty > allowed_qty:
                        frappe.throw(_('The total Issue / Transfer quantity {0} in Material Request {1}  cannot be greater than allowed requested quantity {2} for Item {3}'
                                ).format(d.ordered_qty, d.parent,
                                allowed_qty, d.item_code))
                elif d.ordered_qty and d.ordered_qty > d.stock_qty:

                    frappe.throw(_('The total Issue / Transfer quantity {0} in Material Request {1} cannot be greater than requested quantity {2} for Item {3}'
                                 ).format(d.ordered_qty, d.parent,
                                 d.qty, d.item_code))


def on_update(doc, method):
    #get logged emloyee ID
    employee = frappe.db.get_value("Employee", {"user_id":doc.owner}, "name")
    #get logged supervisor at particular cost center
    purchase_approver = frappe.db.get_value("Employee Cost Center Manager", {"parent":employee, "cost_center":doc.custom_cost_center}, "supervisor")
    if purchase_approver == '' or purchase_approver == None and "Administrator" not in frappe.get_roles():
        frappe.throw("Please ask Administrator to set Purchase Approver For you")

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
        


            
                    
