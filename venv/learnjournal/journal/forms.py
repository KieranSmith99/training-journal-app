from django import forms


class ResourceForm(forms.Form):
    name = forms.CharField(label="Resource name", max_length=100)
    link = forms.CharField(label="Link", max_length=100)
