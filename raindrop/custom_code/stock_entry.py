from erpnext.stock.doctype.stock_entry.stock_entry import StockEntry
import frappe
from frappe import _
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

def validate(doc, method): 
	total_transfered = 0
	for item in doc.items:
		stock = frappe.db.get_all("Stock Entry Detail", filters = {"material_request_item": item.material_request_item}, fields=['*'])
		for s in stock:
			total_transfered += s.qty
		total_transfered += item.qty
		mr = frappe.db.get_value("Material Request Item", item.material_request_item, 'qty')
		if total_transfered > frappe.db.get_value("Material Request Item", item.material_request_item, 'qty'):
			frappe.throw(f"Cannot Transfer {total_transfered} more than requested {mr} for Item {item.item_name}")
		
															  
		

def on_save(doc, method):
    if doc.stock_entry_type == 'Material Issue':
        from erpnext.stock.stock_ledger import is_negative_stock_allowed
        for d in doc.items:
            allow_negative_stock = \
                is_negative_stock_allowed(item_code=d.item_code)
            previous_sle = get_previous_sle({
                'item_code': d.item_code,
                'warehouse': d.s_warehouse or d.t_warehouse,
                'posting_date': doc.posting_date,
                'posting_time': doc.posting_time,
                })

        # get actual stock at source warehouse

            d.actual_qty = previous_sle.get('qty_after_transaction') \
                or 0

        # validate qty during submit

            if d.s_warehouse and not allow_negative_stock \
                and flt(d.actual_qty, d.precision('actual_qty')) \
                < flt(d.transfer_qty, d.precision('actual_qty')):
                frappe.throw(_('Row {0}: Quantity not available for {4} in warehouse {1} at posting time of the entry ({2} {3})'
                             ).format(d.idx,
                             frappe.bold(d.s_warehouse),
                             formatdate(doc.posting_date),
                             format_time(doc.posting_time),
                             frappe.bold(d.item_code)) + '<br><br>'
                             + _('Available quantity is {0}, you need {1}'
                             ).format(frappe.bold(flt(d.actual_qty,
                             d.precision('actual_qty'))),
                             frappe.bold(d.transfer_qty)),
                             NegativeStockError,
                             title=_('Insufficient Stock'))
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
