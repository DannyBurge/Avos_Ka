from django.shortcuts import render
from django.http import HttpResponse


def show_homepage(request):
    links = ('<a href=../shoplist/>Список покупок</a><br>'
             '<a href=../recepies/>Список рецептов</a><br>')
    context = {"links": links}
    return render(request, 'homepage/homepage.html', context)
    #return HttpResponse(links)

