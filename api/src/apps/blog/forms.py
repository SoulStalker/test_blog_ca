from django import forms


class EmailPostForm(forms.Form):
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(widget=forms.Textarea, required=False)


