from django.urls import path
# temos que importar as funções do file "views.py"
from . import views

app_name = 'recipes'

# São requisições HTTP que aparecem na barra de pesquisa
urlpatterns = [
    # "PATH" são caminhos que chamam funções que estão no file "views.py"
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
