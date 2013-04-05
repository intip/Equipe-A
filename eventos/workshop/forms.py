# coding: utf-8

from django import forms

class ContactForm(forms.ModelForm):
    
    name = forms.CharField(required=True)
    email = forms.CharField()
    phone = forms.CharField()
    text = forms.CharField(widget=forms.Textarea, required=True)