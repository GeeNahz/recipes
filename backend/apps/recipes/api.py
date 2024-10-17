from django.shortcuts import get_object_or_404
from typing import List
from ninja import Router
from ninja_jwt.authentication import JWTAuth

from apps.utils import MessageSchema

from .models import Recipe
from .schemas import RecipeOut, RecipeIn

# from apps.utils import MessageSchema


router = Router(auth=JWTAuth())


# Create recipe (is_authenticated)
# List recipes (annon)
@router.get('/', response=List[RecipeOut])
def list_recipes(request):
    return Recipe.objects.all()


# Get recipe (annon)
@router.get('/{recipe_id}', response={200: RecipeOut, 401: MessageSchema})
def get_user(request, recipe_id: str):
    recipe = get_object_or_404(Recipe, pk=recipe_id)  # get.recipe
    return recipe


# Create recipe (is_authenticated)
@router.post(
    '/', response={201: RecipeOut, 401: MessageSchema},
    auth=JWTAuth()
)
def create_recipe(request, data: RecipeIn):
    recipe = Recipe(owner=request.user, **data.dict())
    recipe.save()

    return recipe

# Update recipe [patch] (is_authenticated, recipe owner)


@router.patch(
    '/{recipe_id}', response={200: RecipeOut, 401: MessageSchema},
    auth=JWTAuth()
)
def update_recipe(request, recipe_id: str, data: RecipeIn):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if not (request.user.is_superuser or (request.user.id == recipe.owner.id)):
        return 401, {'message': 'You do not have the required permission to perform this request.'}

    for attr, value in data.dict(exclude_unset=True).items():
        setattr(recipe, attr, value)
    recipe.save()

    return recipe


# Delete recipe (is_authenticated, recipe owner)
@router.delete(
    '/{recipe_id}', response={204: MessageSchema, 401: MessageSchema}
)
def delete_recipe(request, recipe_id: str, data: RecipeIn):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if not (request.user.is_superuser or (request.user.id == recipe.owner.id)):
        return 401, {
            'message': 'You do not have the required permission to perform this request.'
        }

    recipe.delete()

    return 204, {
        'message': f'Recipe with id: {recipe_id} deleted successfully.'
    }
