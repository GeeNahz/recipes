from typing import Any
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


User = get_user_model()


class Command(BaseCommand):
    help = "Creates superuser account if none is available."

    def handle(self, *args: Any, **options: Any) -> str | None:
        if not User.objects.filter(email="admin@admin.com").exists():
            print("=== Creating superuser account... ===")
            User.objects.create_superuser(
                username="admin",
                email="admin@admin.com",
                password="admin",
            )
            print("=== Superuser account has been successfully created. ===")
        else:
            print(
                "=== Superuser already exists. Skipped creating superuser account. ===")
