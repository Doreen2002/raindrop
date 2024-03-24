frappe.ui.form.on("Loan Application", {
onload_post_render: function(frm){
	
// if (frm.doc.workflow_state == "Pending" && frm.doc.expense_approver != frappe.session.logged_in_user && !frappe.user.has_role("Administrator"))
// 	 {
// 		$('.actions-btn-group').hide()
// 	}
// 	if ( frm.doc.workflow_state == "Draft" )
// 	{
// 		$('.actions-btn-group').show()
// 	}
  
	// cur_frm.set_df_property('approval_status', 'hidden', 1);
 //  cur_frm.set_df_property('expense_approver', 'hidden', 1);
  cur_frm.refresh_fields();
	

},

    before_save(frm)
        {
            frappe.call({
            method: 'raindrop.custom_code.loan_application.add_approver',
            args: {
                owner: frm.doc.owner
            },
            freeze: true,
            callback: (r) => {
                frm.doc.custom_purchase_approver__id = r.message;
                frm.refresh_fields();
            },
            error: (r) => {
                console.log(r)
            }
            
        })
        },

    // refresh(frm)
    // {
       
    // },
      

    
})
