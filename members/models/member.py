from django.db import models
from django.conf import settings


class Manager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.annotate(last_registration_date=models.Max('registrations__date'))
        return qs


class Member(models.Model):
    PHONE_NUMBER_MAX_LEN = 20 
    STREET_MAX_LEN = 100 
    CITY_MAX_LEN = 50 

    user = models.OneToOneField(settings.AUTH_USER_MODEL,)
    phone_number = models.CharField(max_length=PHONE_NUMBER_MAX_LEN,)
    street = models.CharField(max_length=STREET_MAX_LEN,)
    postcode = models.IntegerField()
    city = models.CharField(max_length=CITY_MAX_LEN,)

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
