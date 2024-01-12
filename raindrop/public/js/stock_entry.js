frappe.ui.form.on("Stock Entry", {
before_save(frm)
	{
	    frappe.call({
            method: 'raindrop.custom_code.stock_entry.add_approver',
            args: {
                owner: frm.doc.owner,
		custom_cost_center: frm.doc.custom_cost_center
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
	},
    refresh(frm)
    {
	    
        cur_frm.set_df_property('custom_purchase_approver__id', 'read_only', 1)
        cur_frm.set_df_property('custom_purchase_approver__id', 'hidden', 1)
	cur_frm.set_df_property('custom_internal_requisition_manager', 'hidden', 1)
        cur_frm.refresh_fields()
	    
	    $("button:contains('Create')").hide();
	$("button:contains('Get Items From')").hide();

	    frappe.call({
            method: 'raindrop.api.get_nepali_date',
            args: {
                date: frm.doc.posting_date
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
	
        frm.add_custom_button(__("Create Purchase Request"), function() {
            frappe.model.with_doctype('Material Request', function() {
                var mr = frappe.model.get_new_doc('Material Request');
                var items = frm.get_field('items').grid.get_selected_children();
                if(!items.length) {
                    items = frm.doc.items;
                }
		
                mr.work_order = frm.doc.work_order;
                mr.custom_email_initiator_= frm.doc.custom_email_initiator;
		mr.custom_internal_requisition_manager = frm.doc.custom_internal_requisition_manager;
		mr.material_request_type = "Purchase"
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
    },
	posting_date(frm)
		{
			frappe.call({
            method: 'raindrop.api.get_nepali_date',
            args: {
                date: frm.doc.posting_date
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


frappe.ui.form.on('Stock Entry Detail', {


	s_warehouse: function(frm, cdt, cdn) {
		
		let item = frappe.get_doc(cdt, cdn);
		if (item.s_warehouse) {
			frappe.model.set_value(cdt, cdn, "allow_zero_valuation_rate", 1);
		}
	},
    
})
