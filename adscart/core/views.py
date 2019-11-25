from django.shortcuts import render

# Create your views here.
from .models import Item
from django.views.generic import ListView,DeleteView
# Create your views here.
def base_view(request):
    return render(request,'core/product-page.html')

class list_view(ListView):
    model=Item
    fields='__all__'
    template_name='core/home-page.html'

class Detail_view(DeleteView):
    model=Item
    fields='__all__'
    template_name='core/product-page.html'
