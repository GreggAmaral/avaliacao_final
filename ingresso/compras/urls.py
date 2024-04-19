from django.urls import path
from .import views

urlpatterns = [
    path('', views.comprar, name='comprar'),
    path('transacao/<str:Reserva_lugar>', views.transacao, name='transacao'), 
    path('finalizado/', views.finalizado, name="finalizado"),
]