from django.shortcuts import render
from .models import Wine
from django.views.generic.edit import CreateView

def wines(request):
    wine_list = Wine.objects.all()
    context = {'wine_list': wine_list}
    return render(request, 'wines/wine_list.html', context=context)

class WineCreate(CreateView):
    model = Wine
    fields = '__all__'
    success_url = '/'

def search_products(request):
    search = request.GET['search']
    wines = Wine.objects.filter(name__icontains=search)  #Trae los que cumplan la condicion
    context = {'wines':wines}
    return render(request, 'wines/search.html', context=context)
