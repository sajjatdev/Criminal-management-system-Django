from django.db import models

from criminal.models import CriminalModel
from settings.models import CriminalStatus, Punishment

# Create your models here.


class CourtModel(models.Model):
    ID = models.CharField(max_length=255, unique=True, primary_key=True)
    JudgeName = models.CharField(max_length=255)
    CourtName = models.CharField(max_length=255)

    class Meta:

        verbose_name = 'Judge'
        verbose_name_plural = 'Judge List'

    def __str__(self):
        return self.JudgeName


class PunishmentModel(models.Model):
    title = models.CharField(max_length=255)
    criminal = models.ForeignKey(CriminalModel, on_delete=models.CASCADE)
    court = models.ForeignKey(CourtModel, on_delete=models.CASCADE)
    punishment = models.ForeignKey(Punishment, on_delete=models.CASCADE)
    create_at = models.DateField(auto_now_add=True)
    status = models.ForeignKey(
        CriminalStatus,  on_delete=models.CASCADE)

    class Meta:
        db_table = "CriminalPunishment"
        verbose_name = 'Punishment'
        verbose_name_plural = 'Punishment List'

    def __str__(self):
        return str(self.pk)
