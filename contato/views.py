from django.shortcuts import render
from .models import Contato

def contato(request) :
    return render(request, 'contato/index.html')

def formulario_contato(request) :
    novo_contato = Contato()
    novo_contato.nome = request.POST.get('nome')
    novo_contato.telefone = request.POST.get('telefone')
    novo_contato.email = request.POST.get('email')
    novo_contato.mensagem = request.POST.get('mensagem')
    novo_contato.save()

    context = {
        'contatos': Contato.objects.all(),
    }
    return render(request, 'contato/contatos.html', context=context)