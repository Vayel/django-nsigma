from django.db import models
from django.conf import settings


class Manager(models.Manager):
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.annotate(
            alumni=models.Case(
                models.When(user__member__isnull=True, then=False),
                models.When(user__member__isnull=False, then=True),
                default=False,
                output_field=models.BooleanField(),
            )
        )
        return qs


class Client(models.Model):
    """Represent a client in a company. If a client works with us through several
    companies, one instance is created for each.
    """

    POSITION_MAX_LEN = 50
    PHONE_NUMBER_MAX_LEN = 20
    STREET_MAX_LEN = 100
    CITY_MAX_LEN = 50

    # Use a foreign key and not a one-to-one field because we can have multiple
    # instances of Client for one person if this person works with us through
    # several companies.
    user = models.ForeignKey(settings.AUTH_USER_MODEL,)
    company = models.ForeignKey(
        'Company',
        on_delete=models.CASCADE,
    )
    email = models.EmailField()
    position = models.CharField(
        max_length=POSITION_MAX_LEN,
        default='', blank=True,
    )
    street = models.CharField(
        max_length=STREET_MAX_LEN,
        default='', blank=True,
    )
    postcode = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=CITY_MAX_LEN, default='', blank=True,)
    phone_number = models.CharField(
        max_length=PHONE_NUMBER_MAX_LEN,
        default='',
        blank=True,
    )

    objects = Manager()

    def __str__(self):
        return '{0} {1} ({2})'.format(
            self.user.first_name,
            self.user.last_name,
            self.company.name
        )
