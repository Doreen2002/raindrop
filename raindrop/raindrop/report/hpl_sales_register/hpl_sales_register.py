# Copyright (c) 2024, raindrop and contributors
# For license information, please see license.txt

# import frappe


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
	    'option': 'Sales Invoice'
           
        },
	{
            'fieldname': 'customer',
            'label': _('Customer Name'),
            'fieldtype': 'Link',
	    'option': 'Customer'
           
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
	data = [], []
	return columns, data
