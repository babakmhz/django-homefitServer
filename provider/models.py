from django.db import models
# Create your models here.


class provider(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=30, blank=True)
    providing_category = models.ForeignKey(
        'client.serviceCategory',
        models.CASCADE, related_name='category')
    providing_services = models.ManyToManyField(
        'client.subServiceCategory', related_name='provides')

    profile_photo = models.ImageField(upload_to='provider_images/', blank=True)

    def __str__(self):
        return '{}'.format(self.name)


class services(models.Model):
    name = models.ForeignKey('client.subServiceCategory', models.CASCADE)
    price = models.DecimalField(decimal_places=3, max_digits=10)
    provider = models.ForeignKey(provider, models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)


class availableDates(models.Model):
    provider = models.ForeignKey(provider, models.CASCADE)
    dates = models.ManyToManyField('client.availableDateTimeService')
