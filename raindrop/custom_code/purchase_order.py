import frappe 


def on_update(doc, method):
    if doc.workflow_state == "Approved" and doc.material_request_type == "Purchase":
        stock_entry = frappe.new_doc('Stock Entry')
        stock_entry.posting_date = doc.transaction_date
        stock_entry.stock_entry_type = "Material Issue"
        for item in doc.items:
            frappe.throw(f"{frappe.db.get_value('Item', item.item_code, 'is_stock_item')}")
            if frappe.db.get_value('Item', item.item_code, 'is_stock_item') == 1:
                stock_entry.append('items', {
                    "item_code":item.item_code,
                    "rate":item.rate,
                    "qty":item.qty,
                    "material_request":doc.name,
                    "material_request_item":item.name,
                    "s_warehouse":item.warehouse
                })
        stock_entry.insert()
        frappe.db.commit()

        if doc.workflow_state == "Approved" and doc.material_request_type == "Purchase":
            material_request = frappe.new_doc('Material Request')
            material_request.posting_date = doc.transaction_date
            material_request.material_request_type = "Purchase"
            for item in doc.items:
                if frappe.db.get_value('Item', item.item_code, 'is_stock_item') == 0:
                    material_request.append('items', {
                        "item_code":item.item_code,
                        "rate":item.rate,
                        "qty":item.qty,
                        "warehouse":item.warehouse
                    })
            material_request.insert()
            frappe.db.commit()
