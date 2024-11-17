frappe.ui.form.on('Webshop Settings', {
    refresh(frm) {
        // Check if the user is an Administrator
        console.log("praba")
        if (frappe.session.user === "Administrator") {
            // Show the fields for the Administrator
            frm.fields_dict['user_limit'].df.hidden = 0;
            frm.fields_dict['product_limit'].df.hidden = 0;
        } else {
            // Hide the fields for other users
            frm.fields_dict['user_limit'].df.hidden = 1;
            frm.fields_dict['product_limit'].df.hidden = 1;
        }

        // Refresh the form to apply changes dynamically
        frm.refresh_fields();
    }
});





