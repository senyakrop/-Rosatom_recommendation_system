from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from .models import User
# Create your views here.

'''def auth(request):
    return render(request, 'auth.html')

def upload(request):
    login = request.POST.get('name', 'Undefined')
    password = request.POST.get('password', '1234')
    return render(request, 'upload.html')'''
def auth(request):
    if request.method == 'POST':
        user = User()
        user.login = request.POST.get('login')
        user.password = request.POST.get('password')
        user.save()
        return render(request, 'upload.html')
    else:
        userform = UserForm()
        return render(request, 'auth.html', {'form': userform})

