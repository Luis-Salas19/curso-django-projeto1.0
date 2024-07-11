from django.contrib import admin
from .models import Category, Recipe
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    ...


#decorador para registrar o modelo Recipe no painel de administração
@admin.register(Recipe)
#permite que você gerencie objetos Recipe por meio da interface de administração do Django.
class RecipeAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)