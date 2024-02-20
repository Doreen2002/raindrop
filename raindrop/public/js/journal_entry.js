frappe.ui.form.on("Journal Entry", {
onload_post_render: function(frm){
	
if (frm.doc.workflow_state == "Pending" && frm.doc.custom_purchase_approver__id != frappe.session.logged_in_user && !frappe.user.has_role("Administrator") && !frappe.user.has_role("HPL Accountant Manager"))
	 {
		$('.actions-btn-group').hide()
	}
	if ( frm.doc.workflow_state == "Draft" )
	{
		$('.actions-btn-group').show()
	}
	cur_frm.set_df_property('custom_purchase_approver__id', 'hidden', 1);
        cur_frm.refresh_fields();
	

},

    before_save(frm)
        {
            frappe.call({
            method: 'raindrop.custom_code.journal_entry.add_approver',
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
