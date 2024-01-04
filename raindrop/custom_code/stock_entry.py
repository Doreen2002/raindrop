from erpnext.stock.doctype.stock_entry.stock_entry import StockEntry
import frappe
def on_save(doc, method):
    if doc.stock_entry_type == "Material Transfer":
        StockEntry.on_submit(doc)
def on_update(doc, method):
    purchase_approver = frappe.db.get_value("Employee", {"user_id":doc.owner}, "custom_purchase_approver_id")
    if purchase_approver == '' or purchase_approver == None and "Administrator" not in frappe.get_roles():
        frappe.throw("Please ask Administrator to set Purchase Approver For you")

@frappe.whitelist()
def add_approver(owner):
    purchase_approver = frappe.db.get_value("Employee", {"user_id":owner}, "custom_purchase_approver_id")
    if purchase_approver != '' or purchase_approver != None:
        return purchase_approver
