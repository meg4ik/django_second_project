from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Product
        fields = ['title', 'description','price']

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "CFE" in title:
            raise forms.ValidationError("This is a not valid title")
        else:
            return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        else:
            return email

