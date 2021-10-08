from django.db import models


class User(models.Model):

    name = models.CharField(null=True, blank=True, max_length=200)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name
