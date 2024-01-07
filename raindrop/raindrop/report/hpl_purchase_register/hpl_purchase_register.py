# Copyright (c) 2024, raindrop and contributors
# For license information, please see license.txt


import frappe
from frappe import _


def execute(filters=None):
	columns =[
	{
            'fieldname': 'date',
            'label': _('Date'),
            'fieldtype': 'Date',
           
        },
	{
            'fieldname': 'invoice_no',
            'label': _('Invoice No'),
            'fieldtype': 'Link',
	    'options': 'Purchase Invoice'
           
        },
	{
            'fieldname': 'supplier',
            'label': _('Supplier Name'),
            'fieldtype': 'Link',
	    'options': 'Supplier'
           
        },
	{
            'fieldname': 'pp no',
            'label': _('PP No'),
            'fieldtype': 'Data',
		# 'options' : 'Document NUmber'
	   
           
        },
	{
            'fieldname': 'vat_no',
            'label': _('Vat No'),
            'fieldtype': 'Data',
	   
           
        },
	{
            'fieldname': 'Item_description',
            'label': _('Item Description'),
            'fieldtype': 'Text',
	   
           
        },
	{
            'fieldname': 'unit',
            'label': _('Unit'),
            'fieldtype': 'Data',
	   
           
        },
	{
            'fieldname': 'qty',
            'label': _('Quantity'),
            'fieldtype': 'Data',
	   
           
        },
	{
            'fieldname': 'rate',
            'label': _('Rate/Unit'),
            'fieldtype': 'Data',
	   
           
        },
	{
            'fieldname': 'gross_amount',
            'label': _('Gross Amount'),
            'fieldtype': 'Data',
	   
           
        },
	{
            'fieldname': 'insurance',
            'label': _('Insurance'),
            'fieldtype': 'Data',
	   
           
        },
	{
            'fieldname': 'bank Commission',
            'label': _('Bank Commission'),
            'fieldtype': 'Data',
	   
           
        },
	{
            'fieldname': 'custom clearing',
            'label': _('Custom Clearing'),
            'fieldtype': 'Data',
	   
           
        },
	{
            'fieldname': 'custom duity',
            'label': _('Custom Duty'),
            'fieldtype': 'Data',
	   
           
        },
	
	{
            'fieldname': 'freight',
            'label': _('Freight'),
            'fieldtype': 'Data',
	   
           
        },
	{
            'fieldname': 'exercise duty',
            'label': _('Exercise Duty'),
            'fieldtype': 'Data',
	   
           
        },
	{
            'fieldname': 'ind_charge_total',
            'label': _('Ind. Charge Total'),
            'fieldtype': 'Data',
	   
           
        },
	{
			'fieldname' : 'net amount',
			'label' : _('Net Amount'),
			'fieldtype' : 'Data',
			
        },
	{
		    'fieldname' : 'vat',
		    'label' : _('13% VAT'),
		    'fieldtype' : 'Data',
			
        },
		 
	{
            'fieldname': 'invoice_totle',
            'label': _('Invoice Total'),
            'fieldtype': 'Data',
	   
           
        },
		
    {
            'fieldname' : 'landed cost',
			'label' : _('Landed Cost'),
			'fieldtype' : 'Data',
        },
	]
	data = []
	purchase_invoice = frappe.db.get_list("Purchase Invoice", filters={"docstatus":1, "is_return":0}, fields=['*'])
	for purchase in purchase_invoice:
		items = frappe.db.get_all("Purchase Invoice Item", filters={"parent":purchase.name}, fields=['*'])
		total = 0
		gross_amount = 0 
		total_qty = 0
		for item in items:
			total += item.amount
			gross_amount += item.amount
			total_qty += item.qty
			data.append([purchase.posting_date, purchase.custom_bill_number, purchase.supplier, purchase.custom_document_number, '', item.description, item.uom, item.qty, item.rate, gross_amount, '', '', '', '', '', '', '', '', gross_amount * 13/100, total, ''])
			
					
		
	return columns, data
