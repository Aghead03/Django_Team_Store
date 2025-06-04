from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'account/login.html')
def register(request):
    return render(request, 'account/register.html')
def logout(request):
    return render(request, 'account/logout.html')
def user_profile(request):
    return render(request, 'account/user_profile.html')