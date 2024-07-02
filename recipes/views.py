from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe
# Create your views here.

# "Views" são funções que são chamadas pelos "paths", retornam caminhos de templates
# Os templates são codigos HTML 
def home(request):
    # busca todas as receitas, e ordena por 'id'
    recipes = Recipe.objects.all().order_by('id')
    return render(request, 'recipes/pages/home.html', status="404", context={
        "recipes": recipes,
    })


def category(request, category_id):
    # busca todas as receitas, e ordena por 'id'
    recipes = Recipe.objects.filter(category__id=category_id).order_by('id')
    return render(request, 'recipes/pages/home.html', status="404", context={
        "recipes": recipes,
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', status="404", context={
        "recipe": make_recipe(),
        "is_detail_page": True
    })
