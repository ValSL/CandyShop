from django.db import models


class CandyType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'


class Candy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(default=5000, max_digits=10, decimal_places=2)
    type = models.ForeignKey('CandyType', on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='candy_pics')

    def __str__(self):
        return f'{self.name}'

