from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from functional_App import models, forms
# Create your views here.


class IndexView(TemplateView):
    template_name="index.html"



class BookDetaiView(CreateView):
    model=models.Donar
    form_class=forms.BookDetailForm
    template_name="functional_App/User.html"


class ShowView(TemplateView):
    template_name="functional_App/showMemore.html"