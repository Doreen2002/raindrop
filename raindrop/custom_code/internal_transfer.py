import frappe 
from frappe.utils import today

def on_update(doc, method):
    if frappe.db.get_value('Workflow', 'Purchase Request', 'is_active') == 1:
    #     if doc.workflow_state == "Approved" and doc.material_request_type == "Material Transfer":
    #         stock_entry = frappe.new_doc('Stock Entry')
    #         stock_entry.posting_date = doc.transaction_date
    #         stock_entry.stock_entry_type = "Material Issue"
    #         for item in doc.items:
    #             if frappe.db.get_value('Item', item.item_code, 'is_stock_item') == 1:
    #                 stock_entry.append('items', {
    #                     "item_code":item.item_code,
    #                     "rate":item.rate,
    #                     "qty":item.qty,
    #                     "material_request":doc.name,
    #                     "material_request_item":item.name,
    #                     "s_warehouse":item.warehouse,
    #                     "schedule_date":today()
    #                 })
    #         if stock_entry.items != []:
    #             stock_entry.insert()
    #             frappe.db.commit()

        # elif doc.workflow_state == "Approved" and doc.material_request_type == "Material Transfer":
        #     material_request = frappe.new_doc('Material Request')
        #     material_request.posting_date = doc.transaction_date
        #     material_request.material_request_type = "Purchase"
        #     for item in doc.items:
        #         if frappe.db.get_value('Item', item.item_code, 'is_stock_item') == 0:
        #             material_request.append('items', {
        #                 "item_code":item.item_code,
        #                 "rate":item.rate,
        #                 "qty":item.qty,
        #                 "warehouse":item.warehouse,
        #                 "schedule_date":today()
        #             })
        #     if stock_entry.items != []:
        #         material_request.insert()
        #         frappe.db.commit()

            

        if doc.workflow_state == "Approved" and doc.material_request_type == "Purchase":
            total = 0
            # po_order = frappe.new_doc('Purchase Order')
            # po_order.posting_date = doc.transaction_date
            # po_order.supplier = doc.custom_supplier
            for item in doc.items:
                total += item.amount
            #     po_order.append('items', {
            #         "item_code":item.item_code,
            #         "rate":item.rate,
            #         "qty":item.qty,
            #         "warehouse":item.warehouse,
            #         "material_request":doc.name,
            #         "material_request_item":item.name,
            #         "schedule_date":today()
            #     })
            buying = frappe.get_doc('Buying Settings')
            # if total <= buying.custom_purchase_amount_limit:
            #     if po_order.items != []:
            #         po_order.insert(ignore_mandatory=True)
            #         frappe.db.commit()

            if total > buying.custom_purchase_amount_limit:
                frappe.throw("The Material Purchase Is Above Limit, Recommend to General Manager ")
                doc.workflow_state = "Pending"
                    
