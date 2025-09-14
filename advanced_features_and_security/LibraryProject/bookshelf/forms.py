from django import forms

# ✅ Simple example form with title & author fields
class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100, label="Book Title")
    author = forms.CharField(max_length=100, label="Author")
