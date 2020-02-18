from django.db import models


class CandyType(models.Model):
    title = models.CharField(max_length=255)


class Candy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.ForeignKey('CandyType', on_delete=models.CASCADE)

