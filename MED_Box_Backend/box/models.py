from django.db import models

# Create your models here.


class Pill(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    weight = models.DecimalField(max_digits=3, decimal_places=3)
    company = models.CharField(max_length=255)
    inventory = models.IntegerField()


class User(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(max_length=10)
    birth_date = models.DateField
    desc = models.TextField(null=True)
    pills = models.ManyToManyField(Pill)


class PerPill(models.Model):
    pill_intake = models.TimeField()
    dose = models.IntegerField()
    pill = models.ForeignKey(Pill, on_delete=models.CASCADE)


class History(models.Model):
    taken = models.BooleanField()
    pill = models.ForeignKey(Pill, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)


