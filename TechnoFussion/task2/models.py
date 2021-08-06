from django.db import models
import uuid
# Create your models here.

class Request(models.Model):

    class Status(models.TextChoices):
        OPEN = 'Open'
        GENERATED = 'Generated'

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    status = models.CharField(max_length=15, choices=Status.choices, default=Status.OPEN)
    suppCode = models.CharField(max_length=3, unique=True)
    suppName = models.CharField(max_length=100)
    materialName = models.CharField(max_length=100)
    materialSort = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    fullBarchQty = models.IntegerField()
    fullLabelsQty = models.IntegerField()
    lastBatchQty = models.IntegerField()
    lastLabelQty = models.IntegerField()

    def __str__(self):
        return f"Request: {self.status} - {self.suppCode}"


class SuppSeq(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    year = models.IntegerField(default=21)
    suppCode = models.CharField(max_length=3)
    seq = models.IntegerField(default=0)

    class Meta:
        unique_together = ['year', 'suppCode']

    def __str__(self):
        return f"{self.suppCode} - {self.year}"



class Labels(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    requestId = models.UUIDField(editable=False)
    labelNo = models.CharField(max_length=16)

    def __str__(self):
        return self.labelNo