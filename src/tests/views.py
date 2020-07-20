from django.shortcuts import render
from .models import Product

from .forms import ProductForm



def product_create_view(request):
    # 'title': obj.title,
    # 'description': obj.description
    print(request.GET)
    print(request.POST)
    context = {}
    return render(request, "tests/product_create.html", context)



# def product_create_view(request):
#     obj = Product.objects.get(id=2)
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     # context = {
#     # 'title': obj.title,
#     # 'description': obj.description
#     context = {
#         'form': form
#     }
#     return render(request, "tests/product_create.html", context)





# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=2)
    # context = {
    # 'title': obj.title,
    # 'description': obj.description
    context = {
        'object': obj
    }
    return render(request, "tests/product_detail.html", context)