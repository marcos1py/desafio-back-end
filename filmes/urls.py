from django.urls import path
from .views import FilmeView

app_name = 'filmes'

filme_view = FilmeView()

urlpatterns = [
    path('', filme_view.index, name='index'),
]
