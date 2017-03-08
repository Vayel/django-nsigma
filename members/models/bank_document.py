from django.db import models

from .document import Document


class BankDocument(Document):
    member = models.ForeignKey(
        'Member',
        on_delete=models.CASCADE,
        related_name='bank_documents',
    )
