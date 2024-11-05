from django.shortcuts import get_object_or_404
from typing import List
from ninja import Router
from ninja_jwt.authentication import JWTAuth

from apps.utils import MessageSchema

from .models import User
from .schemas import UserOut, UserIn

# from apps.utils import MessageSchema


router = Router(auth=JWTAuth())

unauthenticated_error = {
    "message": "You do not have the required permission to perform this request."
}


@router.get('/', response=List[UserOut])
def list_users(request):
    return User.objects.all()


@router.get('/me', response={200: UserOut, 401: MessageSchema})
def get_current_user(request):
    return request.user


@router.get('/{user_id}', response={200: UserOut, 401: MessageSchema})
def get_user(request, user_id: str):
    user = get_object_or_404(User, pk=user_id)
    if not (request.user.is_superuser or (request.user.id == user.id)):
        return 401, unauthenticated_error

    return user


@router.patch('/{user_id}', response={200: UserOut, 401: MessageSchema})
def update_users(request, user_id: str, data: UserIn):
    user = get_object_or_404(User, pk=user_id)
    if not (request.user.is_superuser or (request.user.id == user.id)):
        return 401, unauthenticated_error

    for attr, value in data.dict(exclude_unset=True).items():
        setattr(user, attr, value)
    user.save()

    return user


@router.delete('/')
def delete_user(request, user_id: str):
    user = get_object_or_404(User, pk=user_id)
    if not (request.user.is_superuser or (request.user.id == user.id)):
        return 401, unauthenticated_error

    user.delete()

    return 204
