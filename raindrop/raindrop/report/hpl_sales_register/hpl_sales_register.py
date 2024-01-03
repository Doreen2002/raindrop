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
		'options': 'Sales Invoice'
		   
		},
	{
			'fieldname': 'customer',
			'label': _('Customer Name'),
			'fieldtype': 'Link',
		'options': 'Customer'
		   
		},
	{
			'fieldname': 'address',
			'label': _('Address'),
			'fieldtype': 'Text',
	   
		   
		},
		{
			'fieldname': 'vat_no',
			'label': _('Vat No'),
			'fieldtype': 'Data',
	   
		   
		},
		{
			'fieldname': 'truck_no',
			'label': _('Truck No'),
			'fieldtype': 'Data',
	   
		   
		},
	{
			'fieldname': 'phone_no',
			'label': _('Phone No'),
			'fieldtype': 'Data',
	   
		   
		},
	{
			'fieldname': 'product_description',
			'label': _('Product Description'),
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
			'fieldname': 'asus',
			'label': _('Asus Sellout'),
			'fieldtype': 'Data',
	   
		   
		},
		{
			'fieldname': 'discount_one',
			'label': _('Discount 1'),
			'fieldtype': 'Data',
	   
		   
		},
		{
			'fieldname': 'discount_two',
			'label': _('Discount Two'),
			'fieldtype': 'Data',
	   
		   
		},
		{
			'fieldname': 'festival_discount',
			'label': _('Festival Discount'),
			'fieldtype': 'Data',
	   
		   
		},
	
		{
			'fieldname': 'festival_discount_one',
			'label': _('Festival Discount 1'),
			'fieldtype': 'Data',
	   
		   
		},
	{
			'fieldname': 'qps_discount',
			'label': _('Qps Discount'),
			'fieldtype': 'Data',
	   
		   
		},
	{
			'fieldname': 'ind_charge_total',
			'label': _('Ind. Charge Total'),
			'fieldtype': 'Data',
	   
		   
		},
	{
			'fieldname': 'total_amount',
			'label': _('Total Amount'),
			'fieldtype': 'Data',
	   
		   
		},
	]
	data = []
	sales_invoice = frappe.db.get_list("Sales Invoice", filters={"docstatus":1}, fields=['*'])
	for sale in sales_invoice:
		items = frappe.db.get_all("Sales Invoice Item", filters={"parent":sale.name}, fields=['*'])
		total = 0
		for item in items:
			total_amount += item.amount
			total += item.amount
			data.append([sale.posting_date, sale.custom_document_number, sale.customer, sale.custom_billing_address, '', '', '', item.description, item.uom, item.qty, item.rate, item.amount, '', '', '', '', '', '', '', total_amount])
		data.append(['', 'Total Invoice', '', '', '', '', '', '', total, '', '', '', '', '', '', '', '', '', '', total_amount])	
	return columns, data


