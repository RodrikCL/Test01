from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Test documento"),
			"items": [
				{
					"type": "doctype",
					"name": "uno",
				}
		 		]
		}
		]
