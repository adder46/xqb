from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from martor.models import MartorField
from taggit.managers import TaggableManager
from taggit.models import Tag

from notebooks.models import Notebook


class Note(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    description = MartorField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE)
    tags = TaggableManager(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class MyTag(models.Model):
    tag = models.OneToOneField(Tag, on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


@receiver(post_save, sender=Tag)
def create_tag(sender, instance, created, **kwargs):
    if created:
        MyTag.objects.create(tag=instance)


@receiver(post_save, sender=Tag)
def save_tag(sender, instance, **kwargs):
    instance.mytag.save()