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
def list_users(request):
    return Recipe.objects.all()


# Get recipe (annon)
@router.get('/me', response={200: RecipeOut, 401: MessageSchema})
def get_user(request):
    user = request.user
    return user


# Update recipe [patch] (is_authenticated, recipe owner)
@router.patch('/{user_id}', response={200: RecipeOut, 401: MessageSchema})
def update_users(request, user_id: str, data: UserIn):
    user = get_object_or_404(User, pk=user_id)
    if not (request.user.is_superuser or (request.user.id == user.id)):
        return 401, {'message': 'You do not have the required permission to perform this request.'}

    for attr, value in data.dict(exclude_unset=True).items():
        setattr(user, attr, value)
    user.save()

    return user
# Delete recipe (is_authenticated, recipe owner)
