import frappe 
from frappe.utils import today
from frappe.utils import cint, cstr, flt, get_link_to_form, getdate, new_line_sep, nowdate
from frappe import _, msgprint
from frappe.utils import now
from erpnext.stock.stock_ledger import NegativeStockError, get_previous_sle, get_valuation_rate
from erpnext.stock.stock_ledger import NegativeStockError, get_previous_sle, get_valuation_rate
from frappe.utils import (
	cint,
	comma_or,
	cstr,
	flt,
	format_time,
	formatdate,
	getdate,
	month_diff,
	nowdate,
)

def on_save(doc, method):
    if doc.material_request_type == 'Material Transfer':
        from erpnext.stock.stock_ledger import is_negative_stock_allowed
        for d in doc.items:
            allow_negative_stock = \
                is_negative_stock_allowed(item_code=d.item_code)
            previous_sle = get_previous_sle({
                'item_code': d.item_code,
                'warehouse': d.from_warehouse or d.warehouse,
                'posting_date': doc.transaction_date,
                'posting_time': now(),
                })

        # get actual stock at source warehouse

            d.custom_actual_qty = previous_sle.get('qty_after_transaction') \
                or 0

        # validate qty during submit

            if d.from_warehouse and not allow_negative_stock \
                and flt(d.custom_actual_qty, d.precision('actual_qty')) \
                < flt(d.qty, d.precision('actual_qty')):
                frappe.msgprint({
			'title': __('Insufficient Stock'),
			'message': __( 'Row {d.idx}: Quantity not available for {frappe.bold(d.item_code))} in warehouse {d.from_warehouse} at posting time of the entry ({formatdate(doc.transaction_date)} {format_time(now())}'),
			'primary_action': {
				    'label': 'Create Purchase Order',
				    'server_action': 'dotted.path.to.method',
				    # 'args': args
				    }
				}
				    )



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
        


            
                    
