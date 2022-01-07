from django.contrib import auth
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import User
from django.contrib.auth import authenticate, login

class LoginView(View):
    def get(self, request):
        context = {
            "form": AuthenticationForm()
        }
        return render(request, 'login.html', context)
        


@login_required
def home(request):
    return render(request, "home.html")


class SignUpView(View):
    def get(self, request):
        context = {
            "form": CustomUserCreationForm()
        }
        return render(request, "register.html", context)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register')