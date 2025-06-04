from django.shortcuts import render

# Create your views here.

def product_listing_page(request):
    return render(request, 'products/product_listing_page.html')
def product_detail_page(request):
    return render(request, 'products/product_detail_page.html')
def search(request):
    return render(request, 'products/search.html')