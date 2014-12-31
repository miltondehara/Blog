from django import forms
from django.forms import ModelForm

from models import Post

"""class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
		"""
class PostForm(ModelForm):
	class Meta:
		model = Post
		
		