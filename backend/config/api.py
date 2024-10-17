from ninja import NinjaAPI, Swagger
from ninja_extra import exceptions
from apps.users.api import router as user_router
from apps.authentication.api import router as auth_router
from apps.recipes.api import router as recipes_router


api_v1 = NinjaAPI(
    title='Recipes',
    description='A platform for food lovers to create, save and share recipes',
    version='1.0.0',
    docs=Swagger(),
    docs_url='/docs',
)

api_v1.add_router(
    '/auth', tags=['Auth'], router=auth_router)
api_v1.add_router(
    '/users', tags=['Users'], router=user_router)
api_v1.add_router(
    '/recipes', tags=['Recipes'], router=recipes_router)


def api_exception_handler(request, exc):
    headers = {}

    if isinstance(exc.detail, (list, dict)):
        data = exc.detail
    else:
        data = {"detail": exc.detail}

    response = api_v1.create_response(request, data, status=exc.status_code)
    for k, v in headers.items():
        response.setdefault(k, v)

    return response


api_v1.exception_handler(exceptions.APIException)(api_exception_handler)
