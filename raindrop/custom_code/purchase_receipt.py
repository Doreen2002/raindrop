import frappe 



def on_update(doc, method):
    po = doc.items[0].purchase_order
    material = frappe.db.get_value("Purchase Order Item", {"parent":po}, 'material_request')
    material_req = frappe.db.get_value("Material Request", material, 'owner')
    doc.custom_email__initiator = material_req
    
       
    

