from django.db import models
from django.contrib.auth.models import User

ACCOUNT_TYPES = (
    ('person', 'PERSON'),
    ('doctor', 'DOCTOR')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=6, choices=ACCOUNT_TYPES)

    def __str__(self):
        return f'{self.user.username} type'
