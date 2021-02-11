from __future__ import unicode_literals
import frappe
from frappe import _

def get_data():
    return [
        {
            "label": _("Documents"),
            "items": [
                {
                    "type": "doctype",
                    "name": "meetingstructure",
                },
            ]
        },
    ]       