from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ('title','description','technology','created_at','numero')
    read_only_fields = ('created_at',)