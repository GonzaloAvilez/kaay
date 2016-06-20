from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth import get_user_model
from . import models
from .models import Post
from shop.models import Category, Product


#define user parameter register_registration

User = get_user_model()


class UserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('name'),
            )

    class Meta:
        model = User
        fields = ['name']


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('market'),
            Field('bio'),
            Field('picture'),
            

            Submit('update', 'Update', css_class="btn-success"),
            )

    class Meta:
        model = models.Profile
        fields = ['picture', 'bio', 'market']    


# form for add a new product 
class ShopFor(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(ShopFor, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('category'),
            Field('name'),
            Field('slug'),
            Field('image'),
            Field('description'),
            Field('price'),
            Field('stock'),
            Field('available'),

            

            Submit('update', 'Update', css_class="btn-success"),
            )


    class Meta:
        model = Product
        fields = ('name','slug', 'image', 'category', 'description', 'price','stock',)    

class PostForm(forms.ModelForm):

        class Meta:
            model = Post
            fields = ('title','text','author',)
