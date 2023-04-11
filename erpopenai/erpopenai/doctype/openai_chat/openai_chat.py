# encoding=utf8
# -*- coding: utf-8 -*- u
from __future__ import unicode_literals
from __future__ import division
import frappe
import frappe, os , math
from frappe import _
from frappe.model.document import Document
from frappe.utils import get_site_base_path, cint, cstr, date_diff, flt, formatdate, getdate, get_link_to_form, \
    comma_or, get_fullname, add_years, add_months, add_days, nowdate
from frappe.utils.data import flt, nowdate, getdate, cint, rounded, add_months, add_days, get_last_day
from frappe.utils.password import update_password as _update_password
from frappe.utils import cint, cstr, flt, nowdate, comma_and, date_diff, getdate, formatdate
# from umalqurra.hijri_date import HijriDate
import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from frappe.model.mapper import get_mapped_doc
import sys
from frappe.core.doctype.sms_settings.sms_settings import send_sms

from erpopenai import conf
import openai


class OpenAiChat(Document):
	# Define function to generate text using GPT-3
	@frappe.whitelist()
	def generate_text(self):
	    # Set OpenAI API key
	    openai.api_key = conf.api_key
	    
	    response = openai.Completion.create(
	        engine="davinci",
	        prompt=self.message,
	        max_tokens=1024,
	        n=1,
	        stop=None,
	        temperature=0.5,
	    )
	    return response.choices[0].text.strip()


