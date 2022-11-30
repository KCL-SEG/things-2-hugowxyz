"""Forms of the project."""

from django import forms

# Create your forms here.

class ThingForm(forms.Form):
    name = forms.CharField(max_length=35)
    description = forms.CharField(max_length=120, widget=forms.Textarea, required=False)
    quantity = forms.IntegerField(widget=forms.NumberInput)
