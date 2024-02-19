frappe.listview_settings['Purchase Order'] = {

    hide_name_column: true, // hide the last column which shows the `name`
    hide_name_filter: true, // hide the default filter field for the name column
     get_indicator(doc) {
        // customize indicator color
        if (doc.docstatus == 2) {
            return [__("Cancelled"), "red", "status,=,Cancelled"];
        }
    },
    formatters: {
        title(val) {
            return val.bold();
        },
        docstatus(val) {
            return val == 2 ? 'Cancelled' : 'No';
        }
    }
  
}
