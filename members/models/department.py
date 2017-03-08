from django.db import models


class Department(models.Model):
    MAX_NAME_LEN = 30

    name = models.CharField(max_length=MAX_NAME_LEN,)
    members = models.ManyToManyField(
        'Member',
        through='DepartmentMembership',
        related_name='departments',
    )

    def __str__(self):
        return self.name


class DepartmentMembership(models.Model):
    MAX_JOB_LEN = 50

    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    job = models.CharField(max_length=MAX_JOB_LEN,)
