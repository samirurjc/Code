from django import forms

class ContentForm(forms.Form):
    content = forms.CharField(label='Content', widget=forms.Textarea)