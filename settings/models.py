from django.db import models
# Create your models here.


class Punishment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Punishment'
        verbose_name = 'Punishment'
        verbose_name_plural = 'Punishment List'

    def __str__(self):

        return self.name


class CrimeType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'crimeType'
        verbose_name = 'Crime Type'
        verbose_name_plural = 'Crime Type List'

    def __str__(self):
        return self.name


class CriminalStatus(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'criminalStatus'
        verbose_name = 'Criminal Status'
        verbose_name_plural = 'Criminal Status List'

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'DMP'
        verbose_name_plural = 'DMP List'

    def __str__(self):
        return self.name


class Station(models.Model):
    District = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)

    class Meta:

        verbose_name = 'Station'
        verbose_name_plural = 'Station List'

    def __str__(self):
        return self.name


class Postion(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:

        verbose_name = 'Postion'
        verbose_name_plural = 'Postion List'

    def __str__(self):
        return self.name
