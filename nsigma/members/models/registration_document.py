import os
from functools import partial

from django.db import models


def upload_path(instance, filename):
    _, ext = os.path.splitext(filename)
    return 'registration-documents/{0}-{1}{2}'.format(instance.name, instance.member, ext)


class RegistrationDocument(models.Model):
    MAX_NAME_LEN = 50

    member = models.ForeignKey(
        'Member',
        on_delete=models.CASCADE,
        related_name='documents',
    )
    name = models.CharField(max_length=MAX_NAME_LEN,)
    created_date = models.DateField(auto_now_add=True,)
    last_update_date = models.DateField(auto_now=True,)
    file = models.FileField(upload_to=upload_path)

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.created_date)

    @property
    def is_in_registration(self):
        return self.registrations.count() > 0
