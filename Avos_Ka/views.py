from django.contrib.auth.models import User
from django.http import HttpResponse


def register_new_user(request):
    if request.method == 'post':
        User.objects.create(username='VeryTest', password='123456789')
        return HttpResponse('ОК')
