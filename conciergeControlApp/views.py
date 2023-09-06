from django.shortcuts import render
from .models import Acervo_Portaria

# Create your views here.
def index(request):
    produtod = Acervo_Portaria.objects.all()
    context = {
        'title': "Concierge Control",
        'produtos': produtod
    }
    return render(request, 'index.html', context)

def jointOwners(request):
    return render(request, 'jointOwners.html')

def produto(request, pk):
    prod = Acervo_Portaria.objects.get(id=pk)

    context = {
        'prod': produto
    }
    return render(request, 'produto.html', context)