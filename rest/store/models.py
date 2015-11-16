from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length=10)


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, verbose_name='related tags')

    class Meta:
        ordering = ('id',)


class Cart(models.Model):
    items = models.ManyToManyField(Item, verbose_name='items in cart')
