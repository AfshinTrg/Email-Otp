from django.db import models


class OtpCode(models.Model):
    email = models.EmailField(unique=True)
    code = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.email} - {self.code} - {self.created}'

