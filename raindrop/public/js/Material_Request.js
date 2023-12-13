frappe.ui.form.on("Material Request", {


    refresh(frm)
    {
        $('button:contains("Create")').hide()
        frm.add_custom_button(__("Create Purchase Order"), function() {
            frappe.model.with_doctype('Purchase Order', function() {
                var mr = frappe.model.get_new_doc('Purchase Order');
                var items = frm.get_field('items').grid.get_selected_children();
                if(!items.length) {
                    items = frm.doc.items;
                }

                mr.work_order = frm.doc.work_order;
                items.forEach(function(item) {
                    var mr_item = frappe.model.add_child(mr, 'items');
                    mr_item.item_code = item.item_code;
                    mr_item.item_name = item.item_name;
                    mr_item.uom = item.uom;
                    mr_item.stock_uom = item.stock_uom;
                    mr_item.conversion_factor = item.conversion_factor;
                    mr_item.item_group = item.item_group;
                    mr_item.description = item.description;
                    mr_item.image = item.image;
                    mr_item.qty = item.qty;
                    mr_item.warehouse = item.s_warehouse;
                    mr_item.schedule_date = frappe.datetime.nowdate();
                });
                frappe.set_route('Form', 'Purchase Order', mr.name);
               
            });

            
               
        });
        frm.add_custom_button(__("Transfer Material"), function() {
            frappe.model.with_doctype('Stock Entry', function() {
                var mr = frappe.model.get_new_doc('Stock Entry');
                var items = frm.get_field('items').grid.get_selected_children();
                if(!items.length) {
                    items = frm.doc.items;
                }

                mr.stock_entry_type = "Material Transfer";
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
                    mr_item.basic_rate = item.rate
                    mr_item.t_warehouse = item.warehouse;
               
                   
                });
                frappe.set_route('Form', 'Stock Entry', mr.name);
               
            });

            
               
        });
    }


})