from django.shortcuts import render

def showrecepie(request):
    context = {'a': 0}
    return render(request, 'Recepies/recepie.html', context)