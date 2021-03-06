from django.db import models

from .document import Document


class RegistrationDocument(Document):
    member = models.ForeignKey(
        'Member',
        on_delete=models.CASCADE,
        related_name='registration_documents',
    )
