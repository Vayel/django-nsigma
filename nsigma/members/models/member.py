from django.db import models
from django.conf import settings


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

    def __str__(self):
        return '{0} {1} ({2})'.format(self.first_name, self.last_name, self.username)

    @property
    def username(self):
        return self.user.username

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def email(self):
        return self.user.email

    @property
    def postal_address(self):
        return '{0}\n{1} {2}'.format(self.street, self.postcode, self.city)
