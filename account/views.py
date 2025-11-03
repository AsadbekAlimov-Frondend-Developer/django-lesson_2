from django.shortcuts import render
from .forms import LoginForm
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate, login 



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['username']
            user = authenticate(request, username=data['username'], password=data['password '])
            if user.is_active:
                login(request, user)
                return HttpResponse("siz saytga kirdingiz")
            else:
                return HttpResponse("siz faol hisob emasiz, qaytadan royxatdan o'ting !")
        else:
            return HttpResponse("Siz formani to'g'ri to'ldirmadingiz !")
    else:
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'registration/login.html', context)
    
