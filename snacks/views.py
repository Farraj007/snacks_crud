from django.shortcuts import render
from django.views.generic import (TemplateView,
                                ListView,
                                DetailView,
                                CreateView,
                                UpdateView,
                                DeleteView
                                )
from .models import Snack

class HomeView(TemplateView):
    template_name = 'home.html'
    
class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack
    context_object_name = 'snack_list'       

class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack
    
class SnackCreateView(CreateView):
    template_name = "snack_create.html"
    model = Snack
    fields = ["title","purchaser", "description"]


class SnackUpdateView(UpdateView):
    template_name = "snack_update.html"
    model = Snack
    fields = ["title", "description"]

class SnackDeleteView(DeleteView):
    template_name = "snack_delete.html"
    model = Snack
    success_url ='/'
class FormView(TemplateView):
    template_name = "form.html"