from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'nome': "Fiallraven - Foldsack No.1 Backpack, Fits 15 Laptops",
        'preço': 109.95,
        'descricao': "Your perfect pack for everyday is and walks in the forest. Stash your Laptop (up to 15 inches) in the padden sleeve, your everyday",
        'categoria': "Men's Clothing",
        'imagem': "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg"
    }
    return render(request, 'main/index.html', context)


def sobre(request):
    return render(request, 'main/sobre.html')


def contato(request):
    return render(request, 'main/contato.html')
