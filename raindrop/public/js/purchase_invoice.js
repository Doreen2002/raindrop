frappe.ui.form.on("Purchase Invoice", {
    
onload_post_render: function(frm){
    if(!frappe.user.has_role('Administrator') && !frappe.user.has_role('HPL Accountant')){
        $('button:contains("Create")').hide();
        $('button:contains("Get Items From")').hide();
	// frm.page.remove_inner_button('Purchase Receipt', 'Create');
	// frm.remove_custom_button('Close', 'Status');
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
