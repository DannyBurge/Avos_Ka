from django.shortcuts import render
from Avos_Ka.models import Recepie


def show_homepage(request):
    recepie_list = ''
    for each_recepie in Recepie.objects.all():
        recepie_list += f'<h3>{each_recepie.display_title()}</h3>'
        recepie_list += f'<div>{each_recepie.display_describe()}</div>'
    context = {"recepie_list": recepie_list}
    return render(request, 'homepage/homepage.html', context)
