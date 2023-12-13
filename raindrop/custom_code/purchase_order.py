import frappe 


def on_update(doc, method):
    # if frappe.db.get_value('Workflow', 'Purchase Order', 'is_active') == 1:
    #     if doc.workflow_state == "Approved":
    #         stock_entry = frappe.new_doc('Stock Entry')
    #         stock_entry.posting_date = doc.transaction_date
    #         stock_entry.stock_entry_type = "Material Reciept"
    #         stock_entry.purchase_order = doc.name
    #         for item in doc.items:
    #             if frappe.db.get_value('Item', item.item_code, 'is_stock_item') == 1:
    #                 stock_entry.append('items', {
    #                     "item_code":item.item_code,
    #                     "rate":item.rate,
    #                     "qty":item.qty,
    #                     "s_warehouse":item.warehouse
    #                 })
    #         stock_entry.insert()
    #         frappe.db.commit()

        
        total = 0
        for item in doc.items:
            total += item.amount
        buying = frappe.get_doc('Buying Settings')
        if total > buying.custom_purchase_amount_limit and"Purchase Master Manager"  in frappe.get_roles() :
                frappe.throw("The Material Purchase Is Above Limit, Recommend to General Manager ")
                doc.workflow_state = "Pending"
    

