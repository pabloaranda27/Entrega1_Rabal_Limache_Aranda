from django import forms

class Form_articles(forms.Form):
    name=forms.CharField(max_length=30)
    price=forms.FloatField()
    description=forms.CharField(max_length=200)
    stock=forms.IntegerField()