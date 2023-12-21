frappe.ui.form.on("Purchase Receipt", {


    refresh(frm)
    {
        $("button:contains('Get Items From')").hide();
	    setTimeout(() =>{
        frm.remove_custom_button( 'Make Stock Entry', 'Create');
        }, 500);
     //    setTimeout(() => {
	    //     frm.page.actions.find('[data-label="Make%20Stock%20Entry"]').parent().parent().remove();
     //        frm.page.actions.find('[data-label="Purchase%20Return"]').parent().parent().remove();
     //        frm.page.actions.find('[data-label="Retention%20Stock%20Entry"]').parent().parent().remove();
     //        frm.page.actions.find('[data-label="Subscription"]').parent().parent().remove();
	    // }, 500);

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
