import frappe

def validate_user_limit(doc,method):
   
   
    # Print the logged-in user's details
    print(frappe.session.user)

    # Check if the current user is an admin
    if frappe.session.user != "Administrator":
        # Fetch the user limit and product limit from Webshop Settings
        webshop_settings = frappe.get_single("Webshop Settings")
      

        # Get the user_limit and product_limit from Webshop Settings
        user_limit = webshop_settings.user_limit if webshop_settings.user_limit else 1  # Default to 3 if no limit set
        product_limit = webshop_settings.product_limit if webshop_settings.product_limit else 1  # Default to 10 if no limit set
        print(product_limit)
        # Count users created by the current admin
        user_count = frappe.db.count("User", filters={"owner": frappe.session.user})

        # Count products created by the current user
        product_count = frappe.db.count("Item", filters={"owner": frappe.session.user})  # Replace "Product" with the actual doctype name for products
          # Validate product creation limit
        print(product_count)
        if product_count >= product_limit:
            # Throw an exception if the product limit is exceeded
            frappe.throw(f"You have reached the limit of {product_limit} products you can create. If you want a higher limit, please subscribe to the 3000 plan.")
        # Validate user creation limit
        if user_count >= user_limit:
            # Throw an exception if the user limit is exceeded
            frappe.throw(f"You have reached the limit of {user_limit} users you can create. If you want a higher limit, please subscribe to the 3000 plan.")
        
      
    

def assign_customer_role(user, method):
    # Check if the user does not have the Customer role already
    if "Customer" not in [role.role for role in user.get("roles")]:
        user.add_roles("Customer")
        frappe.msgprint(f"Customer role assigned to {user.full_name}")




