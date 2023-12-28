frappe.ui.form.on("Material Request", {


    refresh(frm)
    {
        frappe.call({
            method: 'raindrop.api.get_nepali_date',
            args: {
                date: frm.doc.transaction_date
            },
            freeze: true,
            callback: (r) => {
                frm.doc.custom_nepali_date = r.message
                frm.refresh_fields()
            },
            error: (r) => {
                console.log(r)
            }
            
        })
        frappe.call({
            method: 'raindrop.custom_code.internal_transfer.add_approver',
            args: {
                owner: frm.doc.owner
            },
            freeze: true,
            callback: (r) => {
                frm.doc.custom_purchase_approver__id = r.message
                frm.refresh_fields()
            },
            error: (r) => {
                console.log(r)
            }
            
        })
        
        $('button:contains("Create")').hide();
         $('button:contains("Get Items From")').hide();
        $('div[data-fieldname="custom_email_initiator_"]').hide();
        $('div[data-fieldname="custom_purchase_approver__id"]').hide();
        if (cur_frm.doc.material_request_type == "Purchase" && frappe.user.has_role('HPL Inventory') && cur_frm.doc.workflow_state == "Approved")
        {
            frm.add_custom_button(__("Create Purchase Order"), function() {
            frappe.model.with_doctype('Purchase Order', function() {
                var mr = frappe.model.get_new_doc('Purchase Order');
                var items = frm.get_field('items').grid.get_selected_children();
                if(!items.length) {
                    items = frm.doc.items;
                }

                mr.work_order = frm.doc.work_order;
                mr.custom_email_initiator = frm.doc.custom_email_initiator_;
                items.forEach(function(item) {
                    var mr_item = frappe.model.add_child(mr, 'items');
                    mr_item.item_code = item.item_code;
                    mr_item.material_request_item = item.item_name;
                    mr_item.item_name = item.item_name;
                    mr_item.uom = item.uom;
                    mr_item.stock_uom = item.stock_uom;
                    mr_item.conversion_factor = item.conversion_factor;
                    mr_item.item_group = item.item_group;
                    mr_item.description = item.description;
                    mr_item.image = item.image;
                    mr_item.qty = item.qty;
                    mr_item.material_request = frm.doc.name
                    mr_item.warehouse = item.s_warehouse;
                    mr_item.schedule_date = frappe.datetime.nowdate();
                });
                frappe.set_route('Form', 'Purchase Order', mr.name);
               
            });

            
               
        });
        }
        if (cur_frm.doc.material_request_type == "Material Transfer" && frappe.user.has_role('HPL Inventory') && cur_frm.doc.workflow_state == "Approved")
        {
            frm.add_custom_button(__("Transfer Material"), function() {
            frappe.model.with_doctype('Stock Entry', function() {
                var mr = frappe.model.get_new_doc('Stock Entry');
                var items = frm.get_field('items').grid.get_selected_children();
                if(!items.length) {
                    items = frm.doc.items;
                }

                mr.stock_entry_type = "Material Transfer";
                mr.custom_email_initiator = frm.doc.owner;
                items.forEach(function(item) {
                    var mr_item = frappe.model.add_child(mr, 'items');
                    mr_item.item_code = item.item_code;
                    mr_item.item_name = item.item_name;
                    mr_item.uom = item.uom;
                    mr_item.stock_uom = item.stock_uom;
                    mr_item.conversion_factor = item.conversion_factor;
                    mr_item.item_group = item.item_group;
                    mr_item.description = item.description;
                    mr_item.qty = item.qty;
                    mr_item.transfer_qty = item.qty
                    mr_item.basic_rate = item.rate
                    mr_item.t_warehouse = item.warehouse;
               
                   
                });
                frappe.set_route('Form', 'Stock Entry', mr.name);
               
            });

            
               
        });
        }
        
    },
    transaction_date(frm)
        {
            frappe.call({
            method: 'raindrop.api.get_nepali_date',
            args: {
                date: frm.doc.transaction_date
            },
            freeze: true,
            callback: (r) => {
                frm.doc.custom_nepali_date = r.message
                frm.refresh_fields()
            },
            error: (r) => {
                console.log(r)
            }
        })
        }


})
