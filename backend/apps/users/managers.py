from django.apps import apps
from django.contrib.auth.models import UserManager

from apps.utils import AUTH_PROVIDERS


class CustomUserManager(UserManager):
    def _create_user(
        self, username, email, password, **extra_fields
    ):
        """
        Create and save a user with the given username, email, and password.
        """

        if not username:
            raise ValueError("The given username must be set")
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        # if not first_name:
        #     raise ValueError("The given first_name must be set")
        # if not last_name:
        #     raise ValueError("The given last_name must be set")

        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )

        email = self.normalize_email(email)
        username = GlobalUserModel.normalize_username(username)

        user = self.model(
            email=email,
            username=username,
            # first_name=first_name,
            # last_name=last_name,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(
        self,
        # first_name=None,
        # last_name=None,
        username=None,
        email=None,
        password=None,
        **extra_fields,
    ):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(
            username, email, password, **extra_fields
        )

    def create_superuser(
        self,
        # first_name=None,
        # last_name=None,
        username=None,
        email=None,
        password=None,
        **extra_fields,
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_verified", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("auth_provider", AUTH_PROVIDERS.get('email'))

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_verified") is not True:
            raise ValueError("Superuser must have is_verified=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(
            username, email, password, **extra_fields
        )
