from django.db import models
from account.models import Account
from settings.models import CrimeType, CriminalStatus, Punishment


class CasesModel(models.Model):
    STATUS = [('pending', "Pending"),
              ("In_Process", "In Process"), ('open', 'Open'), ("running", 'Running'), ("done", "Done")]

    title = models.CharField(max_length=255)
    descriptions = models.TextField(max_length=500)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        choices=STATUS, default="pending", max_length=255)

    class Meta:

        verbose_name = 'Case'
        verbose_name_plural = 'Case List'

    def __str__(self):
        return self.title


class CriminalModel(models.Model):
    DOCUMENT = [("nid", "National ID card"), ("passport", "Passport"),
                ("driving licence", "Driving Licence")]
    GENDER = [("male", "Male"), ("female", "Female"), ("othere", "othere")]

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="criminal/profile/")
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=255, choices=GENDER, default="male")
    crimeType = models.ForeignKey(CrimeType, on_delete=models.CASCADE)
    case = models.ForeignKey(CasesModel, on_delete=models.CASCADE)

    documant_type = models.CharField(
        choices=DOCUMENT, default="none", max_length=255)
    documant = models.FileField(upload_to="criminal/id/")
    last_update = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "criminal"
        verbose_name = 'Criminal'
        verbose_name_plural = 'Criminal List'

    def __str__(self):
        return self.name




class VictimModel(models.Model):

    DOCUMENT = [("nid", "National ID card"), ("passport", "Passport"),
                ("driving licence", "Driving Licence")]

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    cases = models.ForeignKey(CasesModel, on_delete=models.CASCADE)
    documentType = models.CharField(
        choices=DOCUMENT, default="None", max_length=255)
    document = models.ImageField(upload_to="criminal/victim/")

    class Meta:

        verbose_name = 'Victim'
        verbose_name_plural = 'Victim List'

    def __str__(self):
        return self.name
