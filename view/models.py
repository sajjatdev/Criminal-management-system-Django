from django.db import models

# Create your models here.


class ReportModel(models.Model):
    STATUS = [('pending', 'Pending'), ('in_process',
                                       "In Process"), ('cancel', 'Cancel'), ('done', 'Done')]
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
        verbose_name_plural = 'Reports'

    def __str__(self):
        return self.name
