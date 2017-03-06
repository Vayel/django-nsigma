from django.db import models
from django.conf import settings


class Manager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.annotate(last_registration_date=models.Max('registrations__date'))
        return qs


class Member(models.Model):
    MAX_PHONE_NUMBER_LEN = 20 
    MAX_POSTAL_ADDRESS_LEN = 100 
    MAX_CITY_LEN = 50 
    MAX_STUDENT_LOGIN_LEN = 10

    user = models.OneToOneField(settings.AUTH_USER_MODEL,)
    phone_number = models.CharField(max_length=MAX_PHONE_NUMBER_LEN,)
    street = models.CharField(max_length=MAX_POSTAL_ADDRESS_LEN,)
    postcode = models.IntegerField()
    city = models.CharField(max_length=MAX_CITY_LEN,)

    objects = Manager()

    def __str__(self):
        return '{0} {1} ({2})'.format(
            self.user.first_name,
            self.user.last_name,
            self.user.username
        )

    @property
    def postal_address(self):
        return '{0}\n{1} {2}'.format(self.street, self.postcode, self.city)

    @property
    def last_registration(self):
        return self.registrations.last()
