# Copyright (c) 2025, Anuradha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Customer(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from test_anuradha.test_anuradha.doctype.monthly_energy_summary.monthly_energy_summary import MonthlyEnergySummary

		address: DF.SmallText | None
		customer_name: DF.Data | None
		mobile_no: DF.Data | None
		monthly_energy_summary: DF.Table[MonthlyEnergySummary]
	# end: auto-generated types
	
	def validate(self):
		self.validate_mobile_number()
	
	

	def validate_mobile_number(self):
		if len(self.mobile_no) != 10:
			frappe.msgprint('Invalid mobile number format. Please enter a 10-digit number.')
			raise frappe.exceptions.ValidationError("Mobile number must be 10 digits.")
