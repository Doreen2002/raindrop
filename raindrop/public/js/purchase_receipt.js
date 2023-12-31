frappe.ui.form.on("Purchase Receipt", {

onload_post_render: function(frm){
        var bt = ['Make Stock Entry', 'Purchase Return',  'Retention Stock Entry', 'Subscription']
        bt.forEach(function(bt){
            frm.page.remove_inner_button(bt, 'Create')
            });
        
        
    },
        before_save(frm)
                {
           frappe.call({
            method: 'raindrop.custom_code.purchase_receipt.add_approver',
            args: {
                owner: frm.doc.owner
            },
            freeze: true,
            callback: (r) => {
                frm.doc.custom_purchase_approver__id = r.message
                frm.refresh_fields()
            },
            error: (r) => {
                console.log(r)
            }
            
        })
                },
    refresh(frm)
    {
             
            
        cur_frm.set_df_property('custom_purchase_approver__id', 'read_only', 1)
        cur_frm.refresh_fields()
        cur_frm.set_df_property('custom_email__initiator', 'read_only', 1)
        cur_frm.refresh_fields()
        
        $("button:contains('Get Items From')").hide();

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
