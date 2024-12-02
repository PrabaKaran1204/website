app_name = "online"
app_title = "on"
app_publisher = "praba"
app_description = "line"
app_email = "prabakaran12042002@gmail.com"
app_license = "mit"


fixtures = [
    # Export specific DocTypes
    {
        "doctype": "Webshop Settings",
        "fields": ["product_limit","user_limit"] },   
        {"dt": "File"},
        {"dt": "Website Settings"},
        {"dt": "Website Theme"},
        {"dt": "Web Page"},
        {"dt": "Custom Field"},
        {"dt": "Item"},
        {"dt": "About Us Settings"},
        {"dt": "Contact Us Settings"},
        {"dt": "Website Slideshow"},
        {"dt": "Portal Settings"}, 
        {"dt": "Dashboard"},
        {"dt": "Item Group"},










    
    
    # # Export specific data from a DocType with filters
    # {"dt": "Custom Script", "filters": [["name", "in", ["Client Script for Sales Order"]]]},

    # # Export custom fields with filters
    # {"dt": "Custom Field", "filters": [["fieldname", "like", "%custom_%"]]}
]

# Apps
# ------------------

required_apps = [
    "frappe",
    "erpnext",
    "webshop",
    "payment"
]

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "online",
# 		"logo": "/assets/online/logo.png",
# 		"title": "on",
# 		"route": "/online",
# 		"has_permission": "online.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/online/css/desk.css"

app_include_js = "/assets/online/js/theme.js"

# website_include_js = ["online/public/js/filter.js"]


# In online/hooks.py
# website_route_rules = [
#     {"from_route": "/custom", "to_route": "index.html"}
# ]

# Add this line to include your custom JavaScript file


# include js, css files in header of web template
# web_include_css = "/assets/online/css/online.css"
# web_include_js = "/assets/online/js/online.js"
# web_include_js = "/assets/online/js/online.js"
# web_include_js = "/assets/online/public/js/theme.js"


# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "online/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/theme.js"}
# doctype_list_js = {"User" : "public/js/User_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "online/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "online.utils.jinja_methods",
# 	"filters": "online.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "online.install.before_install"
# after_install = "online.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "online.uninstall.before_uninstall"
# after_uninstall = "online.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "online.utils.before_app_install"
# after_app_install = "online.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "online.utils.before_app_uninstall"
# after_app_uninstall = "online.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "online.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash":app_include_css = "/assets/online/css/desk.css"
#  "method"
# 	}
# }
# doc_events = {
#     "Coupon Code": {
#         "on_update": "online.public.api.send_coupon_email"
#     }
# }
# In hooks.py
doc_events = {
    "User": {
        "before_insert": "online.public.api.validate_user_limit"
    },
     "Item": {
        "before_insert": "online.public.api.validate_user_limit"
    },  
    "User": {
        "after_insert": "online.public.api.assign_customer_role"
    }
}



# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"online.tasks.all"
# 	],
# 	"daily": [
# 		"online.tasks.daily"
# 	],
# 	"hourly": [
# 		"online.tasks.hourly"
# 	],
# 	"weekly": [
# 		"online.tasks.weekly"
# 	],
# 	"monthly": [
# 		"online.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "online.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": ""
# }

# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "online.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["online.utils.before_request"]
# after_request = ["online.utils.after_request"]

# Job Events
# ----------
# before_job = ["online.utils.before_job"]
# after_job = ["online.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"online.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

