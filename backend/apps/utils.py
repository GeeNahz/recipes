import uuid

from ninja import Schema
from django.db import models
from django.core.mail import EmailMessage
from django_extensions.db.models import TimeStampedModel


class DefaultFields(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        editable=False,
        default=uuid.uuid4,
        db_index=True,
    )

    class Meta(TimeStampedModel.Meta):
        abstract = True


class MessageSchema(Schema):
    message: str


class USER_TYPE:
    MENTOR = "mentor"
    MENTEE = "mentee"

    TYPES = (
        (
            MENTOR,
            "Mentor",
        ),
        (
            MENTEE,
            "Mentee",
        ),
    )


class GENDER:
    MALE = "M"
    FEMALE = "F"

    TYPES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )


AUTH_PROVIDERS = {
    "google": "google",
    "twitter": "twitter",
    "facebook": "facebook",
    "github": "github",
    "email": "email",
}


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data["email_subject"],
            body=data["email_body"],
            to=[data["to_email"]],
        )
        email.send()
