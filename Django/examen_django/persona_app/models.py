from django.db import models


# Create your models here.
class Personna(models.Model):
    # déclaration des attributs de persona
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)

    adress_street   = models.CharField(max_length=50)
    adress_number   = models.IntegerField()
    city            = models.CharField(max_length=50)
    country         = models.CharField(max_length=50)
    postcode        = models.IntegerField()

    email           = models.CharField(max_length=50)
    username        = models.CharField(max_length=50)
    password        = models.CharField(max_length=50)

    age             = models.IntegerField()
    picture         = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.id} - {self.first_name} - {self.last_name}'

