import random
import string
from django.db import models
from django.core.mail import send_mail


def random_string_generator(size=20, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size)).upper()


class ReportModel(models.Model):

    STATUS = [('pending', 'Pending'), ('in_process',
                                       "In Process"), ('cancel', 'Cancel'), ('done', 'Done')]
    ID = models.CharField(max_length=255, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=55)
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        choices=STATUS, default='pending', max_length=255)
    document = models.FileField(
        upload_to='report/file/', blank=True, null=True)

    class Meta:

        verbose_name = 'Report'
        verbose_name_plural = 'Report List'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not len(self.ID):
            self.ID = random_string_generator()
            send_mail(
                "Report Status Tracking ID",
                'Hello '+self.name+' Your report is accepted. Please note down this ID' +
                self.ID+'  to see your GD/ report Status anytime. Thank You',
                'nrs110906@gmail.com',
                [self.email], fail_silently=False)
        return super(ReportModel, self).save(*args, **kwargs)


class StationModel(models.Model):
    image = models.ImageField(upload_to="stations/")
    stationCode = models.CharField(max_length=255)
    stationName = models.CharField(max_length=255, verbose_name="Station Name")
    phone = models.CharField(max_length=255)
    phone2 = models.CharField(max_length=255, verbose_name="email")
    address = models.CharField(max_length=255)

    class Meta:

        verbose_name = 'Station'
        verbose_name_plural = 'Station List'

    def __str__(self):
        return self.stationName
