from django.db import models


class CandyType(models.Model):
    title = models.CharField(max_length=255)


class Candy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.ForeignKey('CandyType', on_delete=models.CASCADE)


class Cart(models.Model):
    candy = models.ForeignKey('Candy', on_delete=models.CASCADE)
    count = models.IntegerField()
