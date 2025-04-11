// Copyright (c) 2025, Anuradha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Customer", {
// 	refresh(frm) {

// 	},
onload: function(frm) {

    frm.get_field('monthly_energy_summary').grid.cannot_add_rows = true;
}
});
