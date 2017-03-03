from django.db import models
from django.conf import settings


class Member(models.Model):
    MAX_PHONE_NUMBER_LEN = 20 
    MAX_POSTAL_ADDRESS_LEN = 100 
    MAX_CITY_LEN = 50 
    MAX_STUDENT_LOGIN_LEN = 10

    user = models.OneToOneField(settings.AUTH_USER_MODEL,)
    phone_number = models.CharField(max_length=MAX_PHONE_NUMBER_LEN,)
    postal_address = models.CharField(max_length=MAX_POSTAL_ADDRESS_LEN,)
    postcode = models.IntegerField()
    city = models.CharField(max_length=MAX_CITY_LEN,)

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
