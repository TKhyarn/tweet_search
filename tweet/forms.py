from django import forms

class SearchForm(forms.Form):
    author = forms.CharField(max_length=100, required=False)
    hastag = forms.CharField(max_length=100, required=False)

class SearchHastag(forms.Form):
    hashtag = forms.CharField(max_length=100)
