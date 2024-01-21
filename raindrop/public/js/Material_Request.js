frappe.ui.form.on("Material Request", {
onload_post_render: function(frm){
	
if (frm.doc.workflow_state == "Pending" && frm.doc.custom_purchase_approver__id != frappe.session.logged_in_user && !frappe.user.has_role("Administrator"))
	 {
		$('.actions-btn-group').hide()
	}
	if ( frm.doc.workflow_state == "Draft" )
	{
		$('.actions-btn-group').show()
	}
	cur_frm.set_df_property('custom_purchase_approver__id', 'hidden', 1);
	cur_frm.set_df_property('custom_internal_requisition_manager', 'hidden', 1);
        cur_frm.refresh_fields();
	if ( cur_frm.doc.__unsaved != 1)
	{
	cur_frm.set_df_property('custom_purchase_order_person', 'hidden', 1);
	cur_frm.set_df_property('custom_inventory_person', 'hidden', 1);
	 cur_frm.refresh_fields();
	}

},

    before_save(frm)
        {
            frappe.call({
            method: 'raindrop.custom_code.internal_transfer.add_approver',
            args: {
                owner: frm.doc.owner,
		custom_cost_center: frm.doc.custom_cost_center

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
    material_request_type(frm)
        {
            if (cur_frm.doc.material_request_type == "Purchase")
        {
             cur_frm.set_df_property('custom_inventory_person', 'hidden', 1)
            cur_frm.refresh_fields() 
             cur_frm.set_df_property('custom_purchase_order_person', 'hidden', 0);
            cur_frm.refresh_fields();
        }
        if (cur_frm.doc.material_request_type == "Material Transfer")
        {
             cur_frm.set_df_property('custom_purchase_order_person', 'hidden', 1)
            cur_frm.refresh_fields() 
            cur_frm.set_df_property('custom_inventory_person', 'hidden', 0)
            cur_frm.refresh_fields() 
        }
        },
    refresh(frm)
    {

	if(frm.is_new)
	{
		frappe.call({
            method: 'raindrop.custom_code.internal_transfer.get_approver',
            args: {
                owner: frm.doc.owner,
		
            },
            freeze: true,
            callback: (r) => {
		console.log(r.message)
                if(r.message.length > 1)
		{
		frm.set_query('custom_cost_center', () => {
                return {
                    filters: {
                        name: ['in', r.message]
                    }
                }
            })
		}
		 if(r.message.length == 1)   
		 {
			frm.doc.custom_cost_center = r.message[0]
			 frm.refresh_fields()
		 }
            },
            error: (r) => {
                console.log(r)
            }
        })
	}
	if ( cur_frm.doc.__unsaved != 1)
	{
	cur_frm.set_df_property('custom_purchase_order_person', 'hidden', 1);
	cur_frm.set_df_property('custom_inventory_person', 'hidden', 1);
	 cur_frm.refresh_fields();
	}
	    
        frm.set_query('custom_inventory_person', () => {
        return {
            filters: {
                name: ['in', ['keshav.kc@hpl.com.np']]
            }
        }
    })
        frm.set_query('custom_purchase_order_person', () => {
                return {
                    filters: {
                        name: ['in', ['chaman.bk@hpl.com.np', 'krishna.pradhan@hpl.com.np']]
                    }
                }
            })
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
        
        
        $('button:contains("Create")').hide();
         $('button:contains("Get Items From")').hide();
        $('div[data-fieldname="custom_email_initiator_"]').hide();
        cur_frm.set_df_property('custom_purchase_approver__id', 'read_only', 1)
        cur_frm.refresh_fields()
         if (cur_frm.doc.material_request_type == "Purchase")
        {
             cur_frm.set_df_property('custom_inventory_person', 'hidden', 1)
            cur_frm.refresh_fields() 
             cur_frm.set_df_property('custom_purchase_order_person', 'hidden', 0);
            cur_frm.refresh_fields();
        }
        if (cur_frm.doc.material_request_type == "Material Transfer")
        {
             cur_frm.set_df_property('custom_purchase_order_person', 'hidden', 1)
            cur_frm.refresh_fields() 
            cur_frm.set_df_property('custom_inventory_person', 'hidden', 0)
            cur_frm.refresh_fields() 
        }
        if (cur_frm.doc.material_request_type == "Purchase" && frappe.user.has_role('HPL Purchasing (Lite)') && cur_frm.doc.workflow_state == "Approved")
        {
            frm.add_custom_button(__("Create Purchase Order"), function() {
            frappe.model.with_doctype('Purchase Order', function() {
                var mr = frappe.model.get_new_doc('Purchase Order');
                var items = frm.get_field('items').grid.get_selected_children();
                if(!items.length) {
                    items = frm.doc.items;
                }

                mr.work_order = frm.doc.work_order;
                mr.custom_email_initiator = frm.doc.custom_email_initiator_;
		mr.custom_purpose = frm.doc.custom_purpose
		mr.cost_center = frm.doc.custom_cost_center;
		frappe.call({
	            method: 'raindrop.custom_code.internal_transfer.add_approver',
	            args: {
	                owner: frm.doc.owner,
			custom_cost_center: frm.doc.custom_cost_center
	            },
	            freeze: true,
	            callback: (r) => {
	                mr.custom_purchase_request_manager = r.message
	                frm.refresh_fields()
	            },
	            error: (r) => {
	                console.log(r)
	            }
	            
	        })
		
                items.forEach(function(item) {
                    var mr_item = frappe.model.add_child(mr, 'items');
                    mr_item.item_code = item.item_code;
                    mr_item.material_request_item = item.name;
                    mr_item.item_name = item.item_name;
                    mr_item.uom = item.uom;
                    mr_item.stock_uom = item.stock_uom;
                    mr_item.conversion_factor = item.conversion_factor;
                    mr_item.item_group = item.item_group;
                    mr_item.description = item.description;
                    mr_item.image = item.image;
                    mr_item.qty = item.qty;
                    mr_item.material_request = frm.doc.name
                    mr_item.warehouse = item.s_warehouse;
                    mr_item.schedule_date = frappe.datetime.nowdate();
                });
                frappe.set_route('Form', 'Purchase Order', mr.name);
               
            });

            
               
        });
        }
        if (cur_frm.doc.material_request_type == "Material Transfer" && frappe.user.has_role('HPL Inventory') && cur_frm.doc.workflow_state == "Approved")
        {
            frm.add_custom_button(__("Issue Material"), function() {
            frappe.model.with_doctype('Stock Entry', function() {
                var mr = frappe.model.get_new_doc('Stock Entry');
                var items = frm.get_field('items').grid.get_selected_children();
                if(!items.length) {
                    items = frm.doc.items;
                }

                mr.stock_entry_type = "Material Issue";
                mr.custom_email_initiator = frm.doc.owner;
		mr.custom_cost_center = frm.doc.custom_cost_center
		mr.purpose = frm.doc.custom_purpose
                frappe.call({
	            method: 'raindrop.custom_code.internal_transfer.add_approver',
	            args: {
	                owner: frm.doc.owner,
			custom_cost_center: frm.doc.custom_cost_center
	            },
	            freeze: true,
	            callback: (r) => {
	                mr.custom_internal_requisition_manager = r.message
	                frm.refresh_fields()
	            },
	            error: (r) => {
	                console.log(r)
	            }
	            
	        })
                items.forEach(function(item) {
                    var mr_item = frappe.model.add_child(mr, 'items');
                    mr_item.item_code = item.item_code;
                    mr_item.item_name = item.item_name;
                    mr_item.uom = item.uom;
                    mr_item.stock_uom = item.stock_uom;
                    mr_item.conversion_factor = item.conversion_factor;
                    mr_item.item_group = item.item_group;
                    mr_item.description = item.description;
                    mr_item.qty = item.qty;
                    mr_item.transfer_qty = item.qty
                    mr_item.basic_rate = item.rate
                    mr_item.t_warehouse = item.warehouse;
		    mr_item.material_request = frm.doc.name;
		   mr_item.material_request_item = item.item_code;
               
                   
                });
                frappe.set_route('Form', 'Stock Entry', mr.name);
               
            });

            
               
        });
        }
        
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
        }


})
