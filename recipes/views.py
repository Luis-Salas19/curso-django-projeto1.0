from django.shortcuts import render
from utils.recipes.factory import make_recipe
# Create your views here.

# "Views" são funções que são chamadas pelos "paths", retornam caminhos de templates
# Os templates são codigos HTML 
def home(request):
    return render(request, 'recipes/pages/home.html', status="404", context={
        "recipes": [make_recipe() for _ in range(10)],
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', status="404", context={
        "recipe": make_recipe(),
        "is_detail_page": True
    })
