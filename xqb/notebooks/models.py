from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Notebook(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=255)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
