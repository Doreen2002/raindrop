frappe.ui.form.on("Travel Request", {
	if (frm.doc.workflow_state == "Approved" && frm.doc.owner == frappe.session.logged_in_user || frappe.user.has_role("Administrator"))
	 {
		$('.actions-btn-group').show()
	}
  onload_post_render: function(frm){
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
			frm.set_query('custom_cost_center', () => {
	                return {
	                    filters: {
	                        name: ['in', r.message]
	                    }
	                }
	            })
			}
			 if(r.message.length == 1)   
			 {
				frm.custom_cost_center = r.message[0]
				 frm.refresh_fields()
			 }
	            },
	            error: (r) => {
	                console.log(r)
	            }
        })
  }
})