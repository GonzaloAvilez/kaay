#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django import forms
from .models import Order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

 
class OrderCreateForm(forms.ModelForm):
	def __init__ (self, *args, **kwargs):
		super(OrderCreateForm,self).__init__ (*args,**kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.layout = Layout (
			Field('first_name'),
			Field('last_name'),
			Field('email'),
			Field('address'),
			Field('postal_code'),
			Field('city'),
			)
	
	class Meta:
		model = Order
		fields = ['first_name', 'last_name', 'email', 'address',
				'postal_code', 'city']