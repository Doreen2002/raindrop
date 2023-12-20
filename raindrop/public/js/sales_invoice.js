frappe.ui.form.on("Sales Invoice", {


    refresh(frm)
    {

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
                frm.refresh()
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
