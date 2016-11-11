from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(label="Subject", max_length=100)
	message = forms.CharField(label="Message", widget=forms.Textarea)
	senders_name = forms.CharField(label="Your name", max_length=100, required=False)
	senders_email = forms.EmailField(label="Email", required=False)
	cc_myself = forms.BooleanField(label="Send a copy to yourself", required=False)
