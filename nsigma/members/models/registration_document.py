import os
from functools import partial

from django.db import models


def upload_path(instance, filename):
    _, ext = os.path.splitext(filename)
    return 'registration-documents/{0}-{1}{2}'.format(instance.name, instance.id, ext)


class RegistrationDocument(models.Model):
    MAX_NAME_LEN = 50

    member = models.ForeignKey('Member', on_delete=models.CASCADE,)
    name = models.CharField(max_length=MAX_NAME_LEN,)
    file = models.FileField(upload_to=upload_path)
