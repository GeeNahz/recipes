from typing import Type, Dict
from django.contrib.auth import get_user_model
from ninja import ModelSchema, Schema
from ninja_jwt.schema import TokenObtainInputSchemaBase
from ninja_jwt.tokens import RefreshToken
from pydantic import UUID4


class UserSchema(Schema):
    id: UUID4 | str
    email: str
    username: str


class MyTokenObtainPairOutSchema(Schema):
    refresh: str
    access: str
    token_type: str
    user: UserSchema
    # role: str  # consider adding roles


class MyTokenObtainPairInputSchema(TokenObtainInputSchemaBase):
    @classmethod
    def get_response_schema(cls) -> Type[Schema]:
        return MyTokenObtainPairOutSchema

    @classmethod
    def get_token(cls, user) -> Dict:
        values = {}
        refresh = RefreshToken.for_user(user)
        values["refresh"] = str(refresh)
        values["access"] = str(refresh.access_token)
        values['token_type'] = 'Bearer'
        # values['role'] = user.role  # consider adding roles
        # this will be needed when creating output schema
        values.update(user=UserSchema.from_orm(user))
        return values


User = get_user_model()


class LoginIn(Schema):
    username: str
    password: str


class LoginOut(Schema):
    access: str
    refresh: str
    token_type: str


class RegisterIn(ModelSchema):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class RegisterOut(Schema):
    id: str
    message: str
