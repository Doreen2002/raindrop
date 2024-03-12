frappe.ui.form.on("Travel Request", {
	

  onload_post_render: function(frm){
	  frm.add_custom_button(__('Expense Claim'), function(){
		              frappe.model.with_doctype('Expense Claim', function() {
                var mr = frappe.model.get_new_doc('Expense Claim');
                var items = frm.get_field('costings').grid.get_selected_children();
                if(!items.length) {
                    items = frm.doc.costings;
                }
                mr.employee = frm.doc.employee;
		mr.cost_center = frm.doc.cost_center;
                items.forEach(function(item) {
                    var mr_item = frappe.model.add_child(mr, 'expenses');
                    mr_item.expense_type = item.expense_type;
                    mr_item.amount = item.total_amount;
                    mr_item.expense_date = frappe.datetime.nowdate();
                });
                frappe.set_route('Form', 'Expense Claim', mr.name);
					  })
	  }, __("Create"));
	  if (frm.doc.workflow_state != "Approved"  && !frappe.user.has_role("Administrator"))
	  {
		  $("button:contains('Create')").hide();
	  }
	  
	  if (frm.doc.workflow_state == "Approved" && frm.doc.owner != frappe.session.logged_in_user && !frappe.user.has_role("Administrator"))
	  {
		  $("button:contains('Create')").hide();
	  }
	  if (frm.doc.workflow_state == "Rejected")
	  {
		  $("button:contains('Create')").hide();
	  }
	 
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
				// frm.refresh_fields()
			}
			 if(r.message.length == 1)   
			 {
				frm.doc.cost_center = r.message[0]
				 frm.refresh_fields()
			 }
	            },
	            error: (r) => {
	                console.log(r)
	            }
        })
  }
	
})
