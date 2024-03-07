frappe.ui.form.on("Purchase Invoice", {
	// refresh: function(frm) {
	// 	frm.add_custom_button(__('Expense Claim'), function(){
	// 		console.log('Hai');
	// 		// frappe.msgprint(frm.doc.email);
	// 	}, __("Create"));
	// }
    
onload_post_render: function(frm){
    if(!frappe.user.has_role('Administrator'))
    {
        var bt = ['Purchase Receipt']
        bt.forEach(function(bt){
            frm.page.remove_inner_button(bt, 'Create')
            });
    }
    if(!frappe.user.has_role('Administrator') && !frappe.user.has_role('HPL Accountant')){
        $('button:contains("Create")').hide();
        $('button:contains("Get Items From")').hide();
	// frm.page.remove_inner_button('Purchase Receipt', 'Create');
	// frm.remove_custom_button('Purchase Receipt', 'Create');
	// $('button:contains("Create")').find('li:contains("Purchase Receipt")').hide();

    }     
    },
before_save(frm)
    {
        frappe.call({
            method: 'raindrop.custom_code.purchase_invoice.add_approver',
            args: {
                owner: frm.doc.owner,
                 custom_cost_center: frm.doc.cost_center
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
        
        
        cur_frm.set_df_property('custom_purchase_approver__id', 'read_only', 1)
        cur_frm.refresh_fields()
            
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
    },
    
})



function convertToNepaliDate(gregorianDate) {
    const nepaliDate = NepaliDateConverter.convertToNepali(gregorianDate);
    return `${nepaliDate.year}-${nepaliDate.month}-${nepaliDate.day}`;
  }

frappe.ui.form.on('Purchase Taxes and Charges', {


	custom_deduct_type: function(frm, cdt, cdn) {
		
		let item = frappe.get_doc(cdt, cdn);
		if (item.custom_deduct_type == "Advance") {
			frappe.model.set_value(cdt, cdn, "account_head", "16000 PrepaidSupplier - HPL");
		}
		if (item.custom_deduct_type == "Retention"){
			frappe.model.set_value(cdt, cdn, "account_head", "29900 OtherShortTermLiab - HPL");
			setTimeout(frappe.model.set_value(cdt, cdn, "rate", "5.0"), 1500);
			frappe.model.set_value(cdt, cdn, "add_deduct_tax", "Deduct");
		}
	},
    
})
