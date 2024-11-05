from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from apps.utils import DefaultFields


User = get_user_model()


class Category(DefaultFields, models.Model):
    name = models.CharField(max_length=100)

    class Meta(DefaultFields.Meta):
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


def file_upload_path(instance, filename):
    return "media/recipe/{0}/".format(filename)


class Recipe(DefaultFields, models.Model):
    name = models.CharField(max_length=200, db_index=True)
    rating = models.IntegerField(default=0)
    image = models.ImageField(
        upload_to=str(file_upload_path), null=True, blank=True)
    duration = models.CharField(
        max_length=50, help_text=_('e.g. 2hrs, 1hr 25mins'))

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name=_('recipes'))
    user_likes = models.ManyToManyField(
        User, blank=True, related_name='liked_recipes')
    category = models.ManyToManyField(
        Category, blank=True, related_name='recipes')

    @property
    def likes(self):
        return self.user_likes.all().count()

    class Meta(DefaultFields.Meta):
        ordering = ['name']
        verbose_name_plural = 'Recipies'

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class Ingredient(DefaultFields, models.Model):
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=50, help_text=_('e.g. cups, tbs, kg.'))
    quantity = models.FloatField(default=0.0)
    recipes = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta(DefaultFields.Meta):
        ordering = ['created', 'name']

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)


class Step(DefaultFields, models.Model):
    value = models.TextField()
    recipe = models.ForeignKey(
        'Recipe', related_name='procedures', on_delete=models.CASCADE)

    class Meta(DefaultFields.Meta):
        ordering = ['created']

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.value)
