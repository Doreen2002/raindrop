frappe.ui.form.on("Purchase Order", {

onload_post_render: function(frm){
        var bt = ['Purchase Invoice', 'Payment',  'Payment Request', 'Subscription']
        bt.forEach(function(bt){
            frm.page.remove_inner_button(bt, 'Create')
            });
        
        
    },
    refresh(frm)
    {
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

frappe.ui.form.on('Purchase Taxes and Charges', {


	account_head: function(frm, cdt, cdn) {
		
		let item = frappe.get_doc(cdt, cdn);
		if (item.account_head.includes('TDS'))
                {
                        item.rate = 1.5
                       // frm.refresh_fields()
                }
                if (item.account_head.includes('VAT'))
                {
                      item.rate = 13  
                     //frm.refresh_fields()
                }
	},
    
})
frappe.ui.form.on("Purchase Taxes and Charges", "account_head", function(frm, cdt, cdn) {
    let item = locals[cdt][cdn]; 
	if (item.account_head.includes('TDS'))
	{
		item.rate = 1.5
	      frm.refresh_field('taxes');
	}
	if (item.account_head.includes('VAT'))
	{
	      item.rate = 13  
	    frm.refresh_field('taxes');
	}

    
});


function convertToNepaliDate(gregorianDate) {
    const nepaliDate = NepaliDateConverter.convertToNepali(gregorianDate);
    return `${nepaliDate.year}-${nepaliDate.month}-${nepaliDate.day}`;
  }
