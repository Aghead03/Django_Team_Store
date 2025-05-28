from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')
def contact_us(request):
    return render(request, 'pages/contact_us.html')
def about(request):
    return render(request, 'pages/about.html')