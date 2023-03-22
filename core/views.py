from django.shortcuts import redirect, render
from .models import Topico, Conteudo, Conversor, Limite
from .forms import TopicoForm, ConteudoForm, ConversorForm, LimiteForm
from .funcoes import calculateNyquist, conversor

# Create your views here.
def index_view(request):
    return render(request, 'core/index.html')

