from django.db import models


class Registration(models.Model):
    member = models.ForeignKey(
        'Member',
        on_delete=models.CASCADE,
        related_name='registrations',
    )
    foreigner = models.BooleanField(default=False,)
    date = models.DateField()
    validated = models.BooleanField(default=False,)
    documents = models.ManyToManyField(
        'RegistrationDocument',
        related_name='registrations',
    )

    def __str__(self):
        return '{0} - {1}'.format(self.member, self.date)
