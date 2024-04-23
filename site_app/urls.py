from django.urls import path
from .views import home, criar, pesquisar, produtos, precos, deletar, atualizar

urlpatterns = [
     path('', home, name='home'),
     path('deletar/<int:id>/', deletar, name='deletar'),
    path('atualizar/<int:id>/', atualizar, name="atualizar"),
    path('pesquisar/<int:id>/', pesquisar, name="pesquisar"),
    path('criar/', criar),
    path('pesquisar/', pesquisar),
    path('produtos/', produtos),
    path('precos/', precos),
    path('precos/<int:id>/', precos),
]

