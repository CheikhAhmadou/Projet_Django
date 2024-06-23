from django.db import models
import geocoder

# Create your models here.
"""
class Data(models.Model):
    country = models.CharField(max_length=100, null=True)
    population = models.PositiveIntegerField(null=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = 'Data'

    def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.country).lat
        self.longitude = geocoder.osm(self.country).lng
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.country"""
    


"""""
class Data(models.Model):
    country = models.CharField(max_length=100, null=True)
    population = models.PositiveIntegerField(null=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = 'Data'

    def save(self, *args, **kwargs):
        g = geocoder.osm(self.country)
        self.latitude = g.lat if g else 0
        self.longitude = g.lng if g else 0
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.country

class Regions(models.Model):
    name = models.CharField(max_length=100, null=False)
    population = models.PositiveIntegerField(null=True)
    data = models.ForeignKey(Data, on_delete=models.CASCADE, related_name='regions', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Regions'

    def __str__(self):
        return self.name"""""


### test 2 avec l'ajout de la classe ecole

class Data(models.Model):
    country = models.CharField(max_length=100, null=True)
    population = models.PositiveIntegerField(null=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = 'Data'

    def save(self, *args, **kwargs):
        g = geocoder.osm(self.country)
        self.latitude = g.lat if g else 0
        self.longitude = g.lng if g else 0
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.country

class Regions(models.Model):
    name = models.CharField(max_length=100, null=False)
    population = models.PositiveIntegerField(null=True)
    data = models.ForeignKey(Data, on_delete=models.CASCADE, related_name='regions', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Regions'

    def __str__(self):
        return self.name

class Ecoles(models.Model):
    name = models.CharField(max_length=100, null=False)
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)
    ville = models.CharField(max_length=100, null=True)  # Ajout du champ 'ville'

    class Meta:
        verbose_name_plural = 'Ecoles'

    def __str__(self):
        return self.name
