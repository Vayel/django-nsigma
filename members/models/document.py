import os
from functools import partial

from django.db import models


def upload_path(instance, filename):
    _, ext = os.path.splitext(filename)
    return 'registration-documents/{0}-{1}{2}'.format(
        instance.name,
        instance.created_date,
        ext,
    )


class Document(models.Model):
    MAX_NAME_LEN = 50

    name = models.CharField(max_length=MAX_NAME_LEN,)
    created_date = models.DateField(auto_now_add=True,)
    last_update_date = models.DateField(auto_now=True,)
    file = models.FileField(upload_to=upload_path)

    class Meta:
        abstract = True

    def __str__(self):
        return '{0} ({1})'.format(self.name, self.created_date)
