from django.shortcuts import render
from Avos_Ka.models import Recepie
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin



class RecepiesByUserListView(LoginRequiredMixin, generic.ListView):
    model = Recepie
    template_name = "./Recepies/recepie_list.html"
    # paginate_by = 10

    def get_queryset(self):
        return Recepie.objects.filter(author=self.request.user).order_by('title')


def show_homepage(request):
    recepie_list = ''
    for each_recepie in Recepie.objects.all():
        recepie_list += f'<h3>{each_recepie.display_title()}</h3>'
        recepie_list += f'<div>{each_recepie.display_describe()}</div>'
    context = {"recepie_list": recepie_list}
    return render(request, 'homepage/homepage.html', context)

