frappe.ui.form.on("Purchase Order", {

onload_post_render: function(frm){
        var bt = ['Purchase Invoice', 'Payment',  'Payment Request', 'Subscription']
        bt.forEach(function(bt){
            frm.page.remove_inner_button(bt, 'Create')
            });
	if (frappe.user.has_role('Other Approvals') && frm.doc.workflow_state == "Pending")
	 {
		if(frm.doc.custom_initiator_manager != frappe.session.logged_in_user)
		{
			$('.actions-btn-group').hide()
		}
	}
	 if (frappe.user.has_role('Other Approvals') && frm.doc.workflow_state != "Pending")
	 {
		if(frm.doc.custom_purchase_approver__id != frappe.session.logged_in_user)
		{
			$('.actions-btn-group').hide()
		}
	}
        
        
    },
	// validate(frm) 
	// 	{
	//     frappe.call({
 //            method: 'raindrop.custom_code.purchase_order.add_approver',
 //            args: {
 //                owner: frappe.session.user_email
 //            },
          
 //            callback: (r) => {
        
 //                frm.set_value('custom_purchase_approver__id', r.message)
 //            },
 //            error: (r) => {
 //                console.log(r)
 //            }
            
 //        })
	// frappe.call({
 //            method: 'raindrop.custom_code.purchase_order.add_approver',
 //            args: {
 //                owner: frm.doc.custom_email_initiator
 //            },
       
 //            callback: (r) => {
 //                frm.set_value('custom_initiator_manager', r.message)
 //            },
 //            error: (r) => {
 //                console.log(r)
 //            }
            
 //        })
			
	// 	},
    refresh(frm)
    {
	    if (frappe.user.has_role('Other Approvals') && frm.doc.workflow_state == "Pending")
	 {
		if(frm.doc.custom_initiator_manager != frappe.session.logged_in_user)
		{
			$('.actions-btn-group').hide()
		}
	}
	 if (frappe.user.has_role('Other Approvals') && frm.doc.workflow_state != "Pending")
	 {
		if(frm.doc.custom_purchase_approver__id != frappe.session.logged_in_user)
		{
			$('.actions-btn-group').hide()
		}
	}
        $("button:contains('Get Items From')").hide();
        $("button:contains('Tools')").hide();
        $("button:contains('Status')").hide();
        $("button:contains('Update Items')").hide()
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
    },
    
})


frappe.ui.form.on("Purchase Taxes and Charges", "account_head", function(frm, cdt, cdn) {
    let item = locals[cdt][cdn]; 
	if (item.account_head.includes('TDS'))
	{
		setTimeout(()=>{
		frappe.model.set_value(cdt, cdn, 'rate', 1.5);
	      	frm.refresh_field('taxes');	
		}, 1500);
		
	}
	if (item.account_head.includes('VAT'))
	{
	   setTimeout(()=>{
		frappe.model.set_value(cdt, cdn, 'rate', 13);
	      	frm.refresh_field('taxes');	
		}, 1500);
	}

    
});


function convertToNepaliDate(gregorianDate) {
    const nepaliDate = NepaliDateConverter.convertToNepali(gregorianDate);
    return `${nepaliDate.year}-${nepaliDate.month}-${nepaliDate.day}`;
  }
