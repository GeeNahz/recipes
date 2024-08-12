from ninja import ModelSchema
from .models import Profile, User


class UserOut(ModelSchema):
    class Meta:
        model = User
        exclude = ['password', 'date_joined', 'last_login', 'is_superuser',
                   'is_staff', 'is_verified', 'groups', 'user_permissions']


class UserIn(ModelSchema):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        fields_optional = '__all__'


class ProfileOut(ModelSchema):
    class Meta:
        model = Profile
        fields = '__all__'
