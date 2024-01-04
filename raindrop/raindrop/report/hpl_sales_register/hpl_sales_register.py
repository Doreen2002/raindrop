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
			'fieldtype': 'Currency',
	   
		   
		},
	{
			'fieldname': 'gross_amount',
			'label': _('Gross Amount'),
			'fieldtype': 'Currency',
	   
		   
		},
		{
			'fieldname': 'asus',
			'label': _('Asus Sellout'),
			'fieldtype': 'Data',
	   
		   
		},
		{
			'fieldname': 'discount_one',
			'label': _('Discount 1'),
			'fieldtype': 'Currency',
	   
		   
		},
		{
			'fieldname': 'discount_two',
			'label': _('Discount Two'),
			'fieldtype': 'Currency',
	   
		   
		},
		{
			'fieldname': 'festival_discount',
			'label': _('Festival Discount'),
			'fieldtype': 'Currency',
	   
		   
		},
	
		{
			'fieldname': 'festival_discount_one',
			'label': _('Festival Discount 1'),
			'fieldtype': 'Currency',
	   
		   
		},
	{
			'fieldname': 'qps_discount',
			'label': _('Qps Discount'),
			'fieldtype': 'Currency',
	   
		   
		},
	{
			'fieldname': 'ind_charge_total',
			'label': _('Ind. Charge Total'),
			'fieldtype': 'Currency',
	   
		   
		},
	{
			'fieldname': 'total_amount',
			'label': _('Total Amount'),
			'fieldtype': 'Currency',
	   
		   
		},
	{
			'fieldname': 'blank',
			'label': _(''),
			'fieldtype': 'Data',
	   
		   
		},
	{
			'fieldname': 'taxable_amount',
			'label': _('Taxable Amount'),
			'fieldtype': 'Currency',
	   
		   
		},
	{
			'fieldname': 'vat',
			'label': _('13% VAT'),
			'fieldtype': 'Currency',
	   
		   
		},
	{
			'fieldname': 'blank_two',
			'label': _(''),
			'fieldtype': 'Currency',
	   
		   
		},
	{
			'fieldname': 'invoice_total',
			'label': _('Invoice Total'),
			'fieldtype': 'Currency',
	   
		   
		},
	]
	data = []
	sales_invoice = frappe.db.get_list("Sales Invoice", filters={"docstatus":1}, fields=['*'])
	for sale in sales_invoice:
		items = frappe.db.get_all("Sales Invoice Item", filters={"parent":sale.name}, fields=['*'])
		total = 0
		total_amount  = 0
		total_qty = 0
		for item in items:
			total_amount += item.amount
			total += item.amount
			total_qty += item.qty
			data.append([sale.posting_date, sale.custom_document_number, sale.customer, sale.custom_billing_address, '', '', '', item.description, item.uom, item.qty, item.rate, item.amount, '', '', '', '', '', '', '', total_amount,'', '', '', '', ''])
		data.append(['Invoice Total:', 'Invoice Total:', 'Invoice Total:', 'Invoice Total:', 'Invoice Total:', 'Invoice Total:', 'Invoice Total:', 'Invoice Total:', 'Invoice Total:', total_qty, '-', total, '', '', '', '', '', '', '', total_amount, '', '', '', '', ''])	
	return columns, data


