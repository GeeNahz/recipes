from django.shortcuts import get_object_or_404
from typing import List
from ninja import Router

from .models import User
from .schemas import UserOut, UserIn

# from apps.utils import MessageSchema


router = Router()


@router.get('/', response=List[UserOut])
def list_users(request):
    return User.objects.all()


# @router.patch('/{user_id}', response=UserOut)
# def update_users(request, user_id: str, data: UserIn):
#     user = get_object_or_404(User, pk=user_id)
#     return User.objects.all()
