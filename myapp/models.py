from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
