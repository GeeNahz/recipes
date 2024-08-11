from django.db.models.base import post_save
from apps.utils import AUTH_PROVIDERS, GENDER, USER_TYPE, DefaultFields
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.models import TitleDescriptionModel
from ninja_jwt.tokens import RefreshToken

from .managers import CustomUserManager


class User(DefaultFields, AbstractUser):
    auth_provider = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        default=AUTH_PROVIDERS.get("email"),
    )
    is_verified = models.BooleanField(default=False)

    # Contact details
    email = models.EmailField(
        _("email address"),
        unique=True,
        db_index=True,
    )

    objects = CustomUserManager()

    REQUIRED_FIELDS = [
        "email",
    ]

    class Meta(DefaultFields.Meta, AbstractUser.Meta):
        ordering = ["username"]

    def __str__(self) -> str:
        return str(self.username)

    def verify_user(self):
        if not self.is_verified:
            self.is_verified = True
            self.save()
            return self

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        refresh['username'] = self.username

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "token_type": "Bearer",
        }


class Profile(DefaultFields, models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to="profiles/", blank=True, null=True)
    gender = models.CharField(
        _("gender"),
        max_length=1,
        choices=GENDER.TYPES,
        blank=True,
    )

    # Contact
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)

    class Meta(DefaultFields.Meta):
        pass

    def __str__(self):
        return f'{self.user.username} {self.id}'

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


post_save.connect(create_user_profile, sender=User)
