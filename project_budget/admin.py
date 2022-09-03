from django.contrib import admin
from .models import ProjectModel, PurchaseModel
# Register your models here.
admin.site.register(ProjectModel)
admin.site.register(PurchaseModel)