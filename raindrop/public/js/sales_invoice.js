// frappe.ui.form.on("Sales Invoice", {


//     refresh(frm)
//     {
//         //hide fields 
//     //     frappe.meta.get_docfield("Sales Invoice", "posting_time", cur_frm.doc.name).hidden = 1
//     //    frappe.meta.get_docfield("Sales Invoice", "set_posting_time", cur_frm.doc.name).hidden = 1
//     //    frm.refresh_fields();

//        //read only
//        frappe.meta.get_docfield("Sales Invoice", "due_date", cur_frm.doc.name).read_only= 1
//        frm.refresh_fields();

//        //rename posting date 
//         var exptyp = frappe.meta.get_docfield("Sales Invoice", "posting_date", frm.doc.name);
//         exptyp.label="Nepali Date";
//         frm.refresh_fields();

//        frappe.meta.get_docfield("Sales Invoice", "naming_series", cur_frm.doc.name).options = ["SI-.#####.-7980"]
//        frappe.meta.get_docfield("Sales Invoice", "naming_series", cur_frm.doc.name).default_value = "SI-.#####.-7980"
//        frm.refresh_fields();

//        frappe.call({
//         method: 'raindrop.api.get_nepali_date',
//         args: {
//             date: frm.doc.standard_date
//         },
//         freeze: true,
//         callback: (r) => {
//             frm.doc.posting_date = r.message
//             frm.refresh_fields()
//         },
//         error: (r) => {
//             console.log(r)
//         }
//     })

//     },
//     standard_date(frm)
//     {
//         frappe.call({
//             method: 'raindrop.api.get_nepali_date',
//             args: {
//                 date: frm.doc.standard_date
//             },
//             freeze: true,
//             callback: (r) => {
//                 frm.doc.posting_date = r.message
//                 frm.refresh()
//             },
//             error: (r) => {
//                 console.log(r)
//             }
//         })
//     },
//     standard_payment_date(frm)
//     {
//         frappe.call({
//             method: 'raindrop.api.get_nepali_date',
//             args: {
//                 date: frm.doc.standard_payment_date
//             },
//             freeze: true,
//             callback: (r) => {
//                 frm.doc.due_date = r.message
//                 frm.refresh()
//             },
//             error: (r) => {
//                 console.log(r)
//             }
//         })
//     }
// })



// function convertToNepaliDate(gregorianDate) {
//     const nepaliDate = NepaliDateConverter.convertToNepali(gregorianDate);
//     return `${nepaliDate.year}-${nepaliDate.month}-${nepaliDate.day}`;
//   }