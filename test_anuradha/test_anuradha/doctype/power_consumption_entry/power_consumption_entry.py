# Copyright (c) 2025, Anuradha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from dateutil.relativedelta import relativedelta


class PowerConsumptionEntry(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		customer: DF.Link
		energy_productionkwh: DF.Float
		power_kw: DF.Float
		reading_timestamp: DF.Datetime
		teriff_type: DF.Literal["", "Low", "High"]
	# end: auto-generated types
	


	def autoname(self):
		count = frappe.db.count("Power Consumption Entry", {"customer": self.customer})
		self.name = f"{self.customer}-{count + 1}"
	
	def validate(self):
		self.set_tariff()
		self.set_energy_production()
	
	def on_submit(self):
		self.update_customer_monthly_summary()

	def on_cancel(self):
		self.update_customer_monthly_summary()

	def on_update_after_submit(self):
		self.update_customer_monthly_summary()

	def set_tariff(self):
		if not self.reading_timestamp:
			return
		date_obj = datetime.strptime(self.reading_timestamp, '%Y-%m-%d %H:%M:%S')
		if 6 <= (date_obj.hour) < 18:
			self.teriff_type = "High"
		else:
			self.teriff_type = "Low"

	def set_energy_production(self):
		if not self.power_kw:
			return
		self.energy_productionkwh = self.power_kw * 0.25 


	def update_customer_monthly_summary(self):
		#  Extract month info
		if isinstance(self.reading_timestamp, str):
			date_obj = datetime.strptime(self.reading_timestamp, '%Y-%m-%d %H:%M:%S')
		else:
			date_obj = self.reading_timestamp
		reading_month = date_obj.strftime('%B-%Y')  

		# Get all entries for that customer and month
		entries = frappe.get_all(
			"Power Consumption Entry",
			filters={
				"customer": self.customer,
				"docstatus": 1,
				"reading_timestamp": ["between", get_month_range(date_obj)],
			},
			fields=["teriff_type", "energy_productionkwh"]
		)

		#  Separate Low and High tariff readings
		low_kwh = [e.energy_productionkwh for e in entries if e.teriff_type == "Low"]
		high_kwh = [e.energy_productionkwh for e in entries if e.teriff_type == "High"]

		#  Calculate averages and tariff costs
		avg_low_kwh = round(sum(low_kwh) / len(low_kwh), 2) if low_kwh else 0
		low_tariff = round(avg_low_kwh * 0.1, 4)

		avg_high_kwh = round(sum(high_kwh) / len(high_kwh), 2) if high_kwh else 0
		high_tariff = round(avg_high_kwh * 0.3, 4)

		# Update or insert row in Customer's child table
		customer_doc = frappe.get_doc("Customer", self.customer)

		found = False
		for row in customer_doc.monthly_energy_summary:
			if row.month == reading_month:
				row.avg_low_kwh = avg_low_kwh
				row.low_tariff = low_tariff
				row.avg_high_kwh = avg_high_kwh
				row.high_tariff = high_tariff
				found = True
				break

		if not found:
			customer_doc.append("monthly_energy_summary", {
				"month": reading_month,
				"avg_low_kwh": avg_low_kwh,
				"low_tariff": low_tariff,
				"avg_high_kwh": avg_high_kwh,
				"high_tariff": high_tariff
			})

		customer_doc.save(ignore_permissions=True)
		frappe.db.commit()


def get_month_range(dt):
	start = datetime(dt.year, dt.month, 1)
	end = start + relativedelta(months=1) - relativedelta(seconds=1)
	return [start, end]

		


