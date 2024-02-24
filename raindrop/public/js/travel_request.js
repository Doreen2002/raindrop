frappe.ui.form.on("Travel Request", {
	// refresh: function(frm) {
	// 	frm.add_custom_button(__('Expense Claim'), function(){
	// 		console.log('Hai');
	// 		// frappe.msgprint(frm.doc.email);
	// 	}, __("Create"));
	// }

  onload_post_render: function(frm){
	  frm.add_custom_button(__('Expense Claim'), function(){
		              frappe.model.with_doctype('Expense Claim', function() {
                var mr = frappe.model.get_new_doc('Expense Claim');
                var items = frm.get_field('items').grid.get_selected_children();
                if(!items.length) {
                    items = frm.doc.items;
                }

                mr.employee = frm.doc.employee;
                // mr.custom_email_initiator = frm.doc.custom_email_initiator_;
		// mr.custom_purpose = frm.doc.custom_purpose
		mr.cost_center = frm.doc.cost_center;
		// frappe.call({
	 //            method: 'raindrop.custom_code.internal_transfer.add_approver',
	 //            args: {
	 //                owner: frm.doc.owner,
		// 	cost_center: frm.doc.cost_center
	 //            },
	 //            freeze: true,
	 //            callback: (r) => {
	 //                mr.custom_purchase_request_manager = r.message
	 //                frm.refresh_fields()
	 //            },
	 //            error: (r) => {
	 //                console.log(r)
	 //            }
	            
	 //        })
		
                items.forEach(function(item) {
                    var mr_item = frappe.model.add_child(mr, 'items');
                    mr_item.expense_type = item.expense_type;
                    mr_item.amount = item.total_amount;
                    // mr_item.uom = item.uom;
                    // mr_item.stock_uom = item.stock_uom;
                    // mr_item.conversion_factor = item.conversion_factor;
                    // mr_item.item_group = item.item_group;
                    // mr_item.description = item.description;
                    // mr_item.image = item.image;
                    // mr_item.qty = item.qty;
                    // mr_item.warehouse = item.s_warehouse;
                    mr_item.expense_date = frappe.datetime.nowdate();
                });
                frappe.set_route('Form', 'Expense Claim', mr.name);
	  }, __("Create"));
	  if (frm.doc.workflow_state == "Pending" && frm.doc.owner != frappe.session.logged_in_user && !frappe.user.has_role("Administrator"))
	  {
		  $("button:contains('Create')").hide();
	  }
	  // if (frm.doc.workflow_state == "Pending" && frm.doc.custom_travel_request_approver != frappe.session.logged_in_user && !frappe.user.has_role("Administrator"))
	  // {
		 //  $('.actions-btn-group').hide()
	  // }
    frappe.call({
            method: 'raindrop.custom_code.travel_request.get_approver',
            args: {
                owner: frm.doc.owner,
		
            },
	            freeze: true,
	            callback: (r) => {
			console.log(r.message)
	                if(r.message.length > 1)
			{
			frm.set_query('cost_center', () => {
	                return {
	                    filters: {
	                        name: ['in', r.message]
	                    }
	                }
	            })
				frm.refresh_fields()
			}
			 if(r.message.length == 1)   
			 {
				frm.cost_center = r.message[0]
				 frm.refresh_fields()
			 }
	            },
	            error: (r) => {
	                console.log(r)
	            }
        })
  }
	
})
