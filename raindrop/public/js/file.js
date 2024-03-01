frappe.ui.form.on("File", {

      
frm.add_custom_button(__('Salary Payment Data'), function(){

  frappe.call({
            method: 'raindrop.api.salary_payment',
            args: {
                owner: frm.doc.owner,
		
            },
	      freeze: true,
	      callback: (r) => {
                  }
  })

}, __("Upload"));
    
})
