from ninja import ModelSchema
from .models import Recipe


class RecipeOut(ModelSchema):
    class Meta:
        model = Recipe
        exclude = '__all__'


class RecipeIn(ModelSchema):
    class Meta:
        model = Recipe
        fields = '__all__'
        fields_optional = '__all__'
