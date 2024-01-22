frappe.ui.form.on("Purchase Order", {

onload_post_render: function(frm){
    if(!frappe.user.has_role('Administrator'))
    {
        var bt = ['Purchase Invoice', 'Payment',  'Payment Request', 'Subscription']
        bt.forEach(function(bt){
            frm.page.remove_inner_button(bt, 'Create')
            });
    }
       if (frappe.user.has_role('General Manager'))
	   {
	     cur_frm.page.actions.find('[data-label="Recommend"]').parent().parent().remove();
       }
	
	
	if (frm.doc.workflow_state == "Pending" && frm.doc.custom_initiator_manager != frappe.session.logged_in_user && !frappe.user.has_role("Administrator"))
	 {
		$('.actions-btn-group').hide()
	}
	
	 if (frm.doc.workflow_state != "Pending" || frm.doc.workflow_state != "Draft" )
	 {
		 
		if  ( frm.doc.custom_purchase_approver__id != frappe.session.logged_in_user && !frappe.user.has_role("Administrator"))
	 {
		$('.actions-btn-group').hide()
	}
	 }
	if (frm.doc.workflow_state == "Pending" || frm.doc.workflow_state == "Draft" )
	{
		$('.actions-btn-group').show()
	}
        $("button:contains('Get Items From')").hide();
        $("button:contains('Tools')").hide();
        $("button:contains('Status')").hide();
        $("button:contains('Update Items')").hide()
        
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
	    //cost center code
	    if(frm.is_new)
	{
		frappe.call({
            method: 'raindrop.custom_code.purchase_order.get_approver',
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
	  
        $("button:contains('Get Items From')").hide();
        $("button:contains('Tools')").hide();
        $("button:contains('Status')").hide();
        $("button:contains('Update Items')").hide()
	cur_frm.set_df_property('custom_purchase_approver__id', 'hidden', 1)
	cur_frm.set_df_property('custom_initiator_manager', 'hidden', 1)   
        cur_frm.refresh_fields() 
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

frappe.ui.form.on('Purchase Order Item', {


	refresh: function(frm, cdt, cdn) {
		
	frm.set_df_property('description', 'reqd', 0)
       frm.refresh_fields()
	},
    
})
