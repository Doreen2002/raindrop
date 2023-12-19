import frappe 



def on_update(doc, method):
    po = doc.items[0].purchase_order
    material = frappe.db.get_value("Purchase Order", po, 'custom_email_initiator')
    material_req = material
    doc.custom_email__initiator = material_req
    
       
    

