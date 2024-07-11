from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe
# Create your views here.

# "Views" são funções que são chamadas pelos "paths", retornam caminhos de templates
# Os templates são codigos HTML 
def home(request):
    # busca todas as receitas, e ordena por 'id'
    recipes = Recipe.objects.all().order_by('id') #você está buscando todos os objetos da classe Recipe no banco de dados, ordenando por 'id'
    return render(request, 'recipes/pages/home.html', status="404", context={
        "recipes": recipes,
    })


def category(request, category_id):
    # busca todas as receitas, e ordena por 'id'
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('id')
    return render(request, 'recipes/pages/category.html', status="404", context={
        "recipes": recipes, #O contexto passado para o template inclui a variável recipes, que contém os objetos recuperados do banco de dados
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', status="404", context={
        "recipe": make_recipe(),
        "is_detail_page": True
    })
