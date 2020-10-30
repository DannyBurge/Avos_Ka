from django.shortcuts import render
from django.views import generic
from Avos_Ka.models import Recepie


class RecepieListView(generic.ListView):
    model = Recepie
    template_name = "./Recepies/recepie_list.html"


class RecepieDetailView(generic.DetailView):
    model = Recepie
    template_name = "./Recepies/recepie_detail.html"