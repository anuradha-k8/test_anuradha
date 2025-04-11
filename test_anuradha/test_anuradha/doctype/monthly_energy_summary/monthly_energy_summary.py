# Copyright (c) 2025, Anuradha and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class MonthlyEnergySummary(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		avg_high_kwh: DF.Float
		avg_low_kwh: DF.Float
		high_tariff: DF.Currency
		last_updated: DF.Datetime | None
		low_tariff: DF.Currency
		month: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
	# end: auto-generated types
	pass
