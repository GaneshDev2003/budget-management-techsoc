from django.db import models

# Create your models here.
class PurchaseModel(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.FloatField(default=0)

class ProjectModel(models.Model):
    title = models.CharField(max_length=50)
    allocated = models.FloatField()
    purchases = models.ManyToManyField(PurchaseModel)
    used_budget = models.FloatField(null = True, default=0)
