frappe.ui.form.on("Expense Claim", {
onload_post_render: function(frm){
	
if (frm.doc.workflow_state == "Pending" && frm.doc.custom_purchase_approver__id != frappe.session.logged_in_user && !frappe.user.has_role("Administrator"))
	 {
		$('.actions-btn-group').hide()
	}
	if ( frm.doc.workflow_state == "Draft" )
	{
		$('.actions-btn-group').show()
	}
  
	cur_frm.set_df_property('approval_status', 'hidden', 1);
  cur_frm.set_df_property('expense_approver', 'hidden', 1);
  cur_frm.refresh_fields();
	

},

    before_save(frm)
        {
            frappe.call({
            method: 'raindrop.custom_code.expense_claim.add_approver',
            args: {
                owner: frm.doc.owner
            },
            freeze: true,
            callback: (r) => {
                frm.doc.expense_approver = r.message;
                frm.refresh_fields();
            },
            error: (r) => {
                console.log(r)
            }
            
        })
        },

    refresh(frm)
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

    },
      

    
})



