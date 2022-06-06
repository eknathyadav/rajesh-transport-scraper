from django.db import models
from django.forms import CharField

# Create your models here.


class Source(models.Model):
    source_name = models.CharField(max_length=50)
    source_code = models.CharField(max_length=50)

    def __str__(self):
        return self.source_name


class Destination(models.Model):
    source = models.ManyToManyField(Source)
    dest_name = models.CharField(max_length=50)
    dest_code = models.CharField(max_length=50)

    def __str__(self):
        return self.dest_name
