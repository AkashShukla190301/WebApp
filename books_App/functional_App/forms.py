from django import forms
from functional_App import models


class BookDetailForm(forms.ModelForm):
       

    class Meta:
        model = models.Donar
        fields = '__all__'

        widgets={
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number':forms.NumberInput(attrs={'class': 'form-control'}),
            'email':forms.EmailInput(attrs={'class': 'form-control'}),
            'address':forms.Textarea(attrs={'class': 'form-control'}),
            'book_photo':forms.FileInput(attrs={'class': 'form-control'}),
        }
