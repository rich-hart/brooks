from django.db import models


class Show(models.Model):
    name = models.CharField(max_length=255)
    home = models.URLField()
    logo = models.URLField()
    def __str__(self):
        return self.name
