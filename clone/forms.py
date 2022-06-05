from django import forms
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class PostForm(forms.ModelForm):
    helper = Formhelper()
    helper.form_method= 'POST'
    helper.add_input(Submit('post','post',css_class='btn-primary'
    ))

    class Meta:
        model=Post
        fields = [
            'image'
            'caption'
        ]


