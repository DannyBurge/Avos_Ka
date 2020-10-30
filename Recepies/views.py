from django.shortcuts import render
from Avos_Ka.models import Recepie


def show_recepie(request):
    recepie_list = ''
    for each_recepie in Recepie.objects.all():
        recepie_list += f'<h2>{each_recepie.display_title()}</h2>'
        recepie_list += f'<div>{each_recepie.display_describe()}</div>'
    context = {"recepie_list": recepie_list}
    return render(request, 'Recepies/recepie.html', context)