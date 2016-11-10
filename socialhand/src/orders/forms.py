#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django import forms
from .models import Order
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, InlineField

  
class OrderCreateForm(forms.ModelForm):
	def __init__ (self, *args, **kwargs):
		super(OrderCreateForm,self).__init__ (*args,**kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-3'
		self.helper.field_class  = 'col-lg-9'
		self.helper.layout = Layout (
				
				Div(HTML("<h2 class='text-center'>Shipping details</h2>"),
					Field('formatted_address', required=True, css_class="order-form"),	
					Field('postal_code', required=True, css_class="order-form"),
					Field('locality', required=True, css_class="order-form"),
					Field('sublocality', required=True, css_class="order-form"),	
					Field('route', required=False, css_class="order-form"),
					Field('country', required=False, css_class="order-form"),
					Field('country_short', required=False, css_class="order-form"),
					css_class="col-lg-6 no-padding",
					),
				Div(HTML("<h2 class='text-center'>Contact details</h2>"),
					Field('first_name', required=False, css_class="order-form"),
					Field('last_name', required=False, css_class="order-form"),
					Field('email', required=False, css_class="order-form"),
					css_class="col-lg-6",
				),)
	
	class Meta:
		model = Order
		fields = ['first_name', 'last_name', 'email',
				'postal_code', 'locality', 'sublocality',
				'country_short','country', 'route',
				'formatted_address',]