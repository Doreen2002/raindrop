frappe.ui.form.on("Purchase Receipt", {

onload_post_render: function(frm){
        var bt = ['Make Stock Entry', 'Purchase Return',  'Retention Stock Entry', 'Subscription']
        bt.forEach(function(bt){
            frm.page.remove_inner_button(bt, 'Create')
            });
        
        
    },
    refresh(frm)
    {
             frm.set_query('custom_purchase_order_person', () => {
                return {
                    filters: {
                        name: ['in', ['chaman.bk@hpl.com.np', 'krishna.pradhan@hpl.com.np']]
                    }
                }
            })
            
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
