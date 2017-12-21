from django.db import models

# Create your models here.


class Investment(models.Model):
    name = models.CharField(max_length=20)
    amount = models.FloatField()
    atRate = models.FloatField( )
    time = models.DateTimeField(blank=True)

    def __str__(self):
        return f'{self.name} {self.amount} {self.time}'


class HistData(models.Model):
    time = models.DateTimeField()
    rate = models.FloatField()
    currency = models.CharField(max_length=5)

    def __str__(self):
        return f'{self.currency} {self.rate} {self.time}'
