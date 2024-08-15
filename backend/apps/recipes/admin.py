from django.contrib import admin

from .models import Recipe, Category, Ingredient, Step


class StepAdmin(admin.ModelAdmin):
    model = Step
    list_display = ('recipe', 'created')


class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ("name", "unit", "quantity", 'created',)


class StepInline(admin.TabularInline):
    model = Step


class IngredientInline(admin.TabularInline):
    model = Ingredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [IngredientInline, StepInline]
    list_display = ("name", "rating", "duration", "owner", 'created',)


admin.site.register(Category)
admin.site.register(Step, StepAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
