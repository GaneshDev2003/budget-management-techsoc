from rest_framework import serializers

from .models import ProjectModel,PurchaseModel

class ProjectSerializer(serializers.ModelSerializer):
    model = ProjectModel
    fields = "__all__"