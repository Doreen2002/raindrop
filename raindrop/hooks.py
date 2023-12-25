from . import __version__ as app_version

app_name = "raindrop"
app_title = "Raindrop"
app_publisher = "raindrop"
app_description = "Raindrop customisations"
app_email = "doreenmwapekatebe8@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/raindrop/css/raindrop.css"
# app_include_js = "/assets/raindrop/js/raindrop.js"

# include js, css files in header of web template
# web_include_css = "/assets/raindrop/css/raindrop.css"
# web_include_js = "/assets/raindrop/js/raindrop.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "raindrop/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"Sales Invoice" : "public/js/sales_invoice.js"}
doctype_js = {"Material Request" : "public/js/Material_Request.js","Stock Entry" : "public/js/stock_entry.js",
	      "Journal Entry":"public/js/journal_entry.js", "Sales Invoice" : "public/js/sales_invoice.js",
	      "Purchase Invoice" : "public/js/purchase_invoice.js", "Purchase Order" : "public/js/purchase_order.js",
	      "Purchase Receipt" : "public/js/purchase_receipt.js"
	     }
# doctype_js = {}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "raindrop.utils.jinja_methods",
#	"filters": "raindrop.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "raindrop.install.before_install"
# after_install = "raindrop.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "raindrop.uninstall.before_uninstall"
# after_uninstall = "raindrop.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "raindrop.utils.before_app_install"
# after_app_install = "raindrop.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "raindrop.utils.before_app_uninstall"
# after_app_uninstall = "raindrop.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "raindrop.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	# "Purchase Invoice": {
	# 	"on_submit": "raindrop.custom_code.purchase_invoice.on_submit",
	# 	# "on_cancel": "method",
	# 	# "on_trash": "method"
	# },
    # "Material Request": {
	# 	"on_update": "raindrop.custom_code.internal_transfer.on_update"
	# 	# "on_cancel": "method",
	# 	# "on_trash": "method"
	# },
    "Purchase Order": {
		"on_update": "raindrop.custom_code.purchase_order.on_update",
		# "on_cancel": "method",
		# "on_trash": "method"
	},
    "Purchase Receipt": {
		"on_update": "raindrop.custom_code.purchase_receipt.on_update",
		# "on_cancel": "method",
		# "on_trash": "method"
	},
     "Stock Entry": {
		"on_update": "raindrop.custom_code.stock_entry.on_save",
		
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"raindrop.tasks.all"
#	],
#	"daily": [
#		"raindrop.tasks.daily"
#	],
#	"hourly": [
#		"raindrop.tasks.hourly"
#	],
#	"weekly": [
#		"raindrop.tasks.weekly"
#	],
#	"monthly": [
#		"raindrop.tasks.monthly"
#	],
# }



# Testing
# -------

# before_tests = "raindrop.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "raindrop.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "raindrop.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["raindrop.utils.before_request"]
# after_request = ["raindrop.utils.after_request"]

# Job Events
# ----------
# before_job = ["raindrop.utils.before_job"]
# after_job = ["raindrop.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"raindrop.auth.validate"
# ]

fixtures = [

     {
        "dt": "Custom Field",
        "filters": [
            [
                "module", "in", [
                    "Raindrop"
                ]
            ]
        ]

    },
    {
        "dt": "Workflow",
        "filters": [
            [
                "name", "in", [
			"Journal Entry", "Sales Invoice", "Payment Entry", "Inventory", "Purchase receipt", "Purchase invoice", "Purchase Order", "Purchase Request"
                ]
            ]
        ]

    },
    {
        "dt": "Notification",
        "filters": [
            [
                "name", "in", [
                    "Purchase Order Pending", "Create Purchase Invoice", "Purchase Order", "Purchase Request", "Purchase Request Status", "Internal Requisition Status", "Internal Requesition", "Purchase Invoice",
			"Purchase Invoice Status", "Purchase Receipt", "Purchase Order Status", "Inventory Transfer Status", "Inventry Transfer"
                ]
            ]
        ]

    },
	{
        "dt": "Email Account",
        "filters": [
            [
                "name", "in", [
			"Raindrop Inc"
                ]
            ]
        ]

    }
   
]
