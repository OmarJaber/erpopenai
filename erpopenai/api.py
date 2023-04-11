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

# Define function to generate text using GPT-3
def generate_text():
    # Set OpenAI API key
    openai.api_key = conf.api_key
    
    # Get the count of employees
    employee_count = frappe.db.count("Employee", filters={"company": "WSM"})

    # Set up OpenAI GPT-3 model
    model_engine = "davinci"
    prompt = f"What is the count of employees in WSM?"
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=10,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Get the response from OpenAI
    count_str = completions.choices[0].text.strip()
    employee_count_ai = count_str
    print(completions)
    # Compare the results
    if employee_count_ai == employee_count:
        print("The count of employees matches.")
    else:
        print(f"The count of employees does not match. OpenAI count: {employee_count_ai}, ERPNext count: {employee_count}")






