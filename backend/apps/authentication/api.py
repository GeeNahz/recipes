import jwt
from typing import Optional
from decouple import config
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse_lazy
from ninja import Router
from ninja.responses import codes_4xx, codes_2xx
from ninja_jwt.tokens import RefreshToken
from ninja_jwt.routers.obtain import obtain_pair_router
from ninja_jwt.routers.blacklist import blacklist_router

from apps.authentication.schemas import RegisterIn, RegisterOut
from apps.utils import AUTH_PROVIDERS, MessageSchema, Util

from .schemas import LoginOut, LoginIn


User = get_user_model()

router = Router()


# @router.post('/login/', response={
#     200: LoginOut,
#     400: MessageSchema
# })
# def login(request, credentials: LoginIn):
#     payload = credentials.dict()
#     user = authenticate(
#         username=payload['username'], password=payload['password'])
#
#     if user is not None:
#         user_tokens = user.tokens()
#         return 200, user_tokens
#
#     return 400, {'message': 'Username or password is incorrect'}

router.add_router('', tags=['Auth'], router=obtain_pair_router)
router.add_router('', tags=['Auth'], router=blacklist_router)


@router.get('/verify-email/', url_name='verify_email', response={
    codes_2xx: None,
    codes_4xx: MessageSchema,
})
def verify_email(request, token: Optional[str] = None):
    if token is None:
        return 400, {'message': 'Bad request. Token was not provided'}

    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[
                str(config("ALGORITHM"))
            ]
        )
        User.objects.get(id=payload["user_id"]).verify_user()

        return redirect(to='http://localhost:3000/login')
    except User.DoesNotExist:
        return 404, {'message': 'User for the provided token does not exist.'}
    except jwt.ExpiredSignatureError:
        # TODO: Give the user a link to request for new activation link
        return 401, {"message": "Activation link expired."}
    except jwt.DecodeError:
        return 400, {"message": "Invalid activation link."}


@router.post('/register/', response=RegisterOut)
def register(request, data: RegisterIn):
    user = User.objects.create_user(
        **data.dict(), auth_provider=AUTH_PROVIDERS.get('email'))

    # Prepare data for email verification
    user_email = data.email
    token = RefreshToken.for_user(user).access_token

    current_site = get_current_site(request).domain
    relative_link = reverse_lazy("api-1.0.0:verify_email")
    abs_url = "http://" + current_site + \
        relative_link + "?token=" + str(token)

    email_body = (
        "Hi " + user.username + ", use link below to verify your email.\n"
        + abs_url + '\n\n' + 'The link will expire in 30 minutes'
    )
    data = {
        "email_body": email_body,
        "email_subject": "Verify your email",
        "to_email": user_email,
    }
    # Send verification email
    Util.send_email(data=data)

    return {
        'id': str(user.id),
        'message': 'A verification link has been sent to your email. Kindly verify your email using the link',
    }
