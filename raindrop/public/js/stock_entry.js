frappe.ui.form.on("Stock Entry", {

	refresh(frm)
		{
			$("button:contains('Create')").hide();
			$("button:contains('Get Items From')").hide();

		},

    form_render(frm)
    {
	
        frm.add_custom_button(__("Create Purchase Request"), function() {
            frappe.model.with_doctype('Material Request', function() {
                var mr = frappe.model.get_new_doc('Material Request');
                var items = frm.get_field('items').grid.get_selected_children();
                if(!items.length) {
                    items = frm.doc.items;
                }

                mr.work_order = frm.doc.work_order;
                mr.custom_email_initiator_= frm.doc.custom_email_initiator;

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
                frappe.set_route('Form', 'Material Request', mr.name);
               
            });

            
               
        });
    }


})


frappe.ui.form.on('Stock Entry Detail', {


	s_warehouse: function(frm, cdt, cdn) {
		
		let item = frappe.get_doc(cdt, cdn);
		if (item.s_warehouse) {
			frappe.model.set_value(cdt, cdn, "allow_zero_valuation_rate", 1);
		}
	},
    
})
