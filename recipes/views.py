from django.shortcuts import render
# Create your views here.

# "Views" são funções que são chamadas pelos "paths", retornam caminhos de templates
# Os templates são codigos HTML 
def home(request):
    return render(request, 'recipes/home.html', status="404", context={
        "name": "Luis Salas"
    })
