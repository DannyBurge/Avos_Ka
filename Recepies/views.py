from django.views import generic
from Avos_Ka.models import Recepie, ProductList, Amount, Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse


class RecepiesByUserListView(LoginRequiredMixin, generic.ListView):
    model = Recepie
    template_name = "./Recepies/recepie_list.html"
    # paginate_by = 10

    def get_queryset(self):
        return Recepie.objects.filter(author=self.request.user).order_by('title')


def add_recepie(request):
    print(request.method)
    if request.method == 'POST':
        recepie_title = f'{request.POST["recepie_title"]}'
        recepie_description = f'{request.POST["recepie_description"]}'
        if len(recepie_title) > 0 and len(recepie_description) > 0:
            recepie = Recepie.objects.create(
                title=recepie_title,
                describe=recepie_description,
                author=request.user,)
            return render(request, './Recepies/recepie_detail.html', context={'recepie': recepie})
    else:
        return render(request, './Recepies/recepie_add.html')


class RecepieListView(generic.ListView):
    model = Recepie
    template_name = "./Recepies/recepie_list.html"


class RecepieDetailView(generic.DetailView):
    model = Recepie
    template_name = "./Recepies/recepie_detail.html"