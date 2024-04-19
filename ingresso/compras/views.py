from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Reserva
from .forms import ReservaForm
from django.contrib.auth.models import User

@login_required
def comprar(request):
    context = {
        'ingressos': Reserva.objects.filter(comprado=False)
    }
    return  render (request, 'comprar.html', context)

@login_required
def transacao(request, Reserva_lugar):
    ingresso = Reserva.objects.get(lugar=Reserva_lugar)

    if (request.method == 'POST'):
        form = ReservaForm(request.POST, instance=ingresso)
        
        if (form.is_valid()):
            form_=form.save(commit=False)
            form_.comprado=True
            form.save()
            return redirect ('/finalizado/')
        else:
            return render (request, 'transacao.html')
    else:
        return render (request, 'transacao.html')

@login_required
def finalizado(request):
    context = {
        'email': request.user.email,
    }
    return  render (request, 'Finalizar.html', context)
