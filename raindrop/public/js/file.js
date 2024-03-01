frappe.ui.form.on("File", {

      
frm.add_custom_button(__('Salary Payment Data'), function(){

  frappe.call({
            method: 'raindrop.api.salary_payment',
            args: {
                file_url: frm.doc.file_url,
		
            },
	      freeze: true,
	      callback: (r) => {
                  }
  })

}, __("Upload"));
    
})
