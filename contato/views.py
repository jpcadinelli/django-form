from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContatoFrom

def index(request):
    form = ContatoFrom()
    context = {
        'form': form
    }
    return render(request, 'contato/index.html', context=context)