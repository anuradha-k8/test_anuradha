// Copyright (c) 2025, Anuradha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Power Consumption Entry", {
    power_kw(frm){
        // Total Energy = 1 kW × 0.25 hour = 0.25 kWh
        frm.set_value('energy_productionkwh', (frm.doc.power_kw * 0.25))
    },
    reading_timestamp(frm){
        set_tariff_based_on_time(frm) 
    }
});
function set_tariff_based_on_time(frm) {
    if (!frm.doc.reading_timestamp) return;

    const readingDateTime = frappe.datetime.str_to_obj(frm.doc.reading_timestamp);
    const hour = readingDateTime.getHours();

    if (hour >= 6 && hour < 18) {
        frm.set_value('teriff_type', 'High');
    } else {
        frm.set_value('teriff_type', 'Low');
    }
}