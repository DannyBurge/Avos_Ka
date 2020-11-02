from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def register_new_user(request):
    if not request.user.is_authenticated:
        form = UserCreationForm(request.GET)
        if request.POST:
            form = UserCreationForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = User.objects.create_user(username=username)
                user.set_password(password)
                user.save()
                if user is not None:
                    login(request, user)
                    return redirect('home')
        return render(request, 'registration/registration.html', context={'form': form})
