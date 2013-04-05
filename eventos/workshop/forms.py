# coding: utf-8

from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
    
    name = forms.CharField(required=True)
    email = forms.CharField()
    phone = forms.CharField()
    text = forms.CharField(widget=forms.Textarea, required=True)