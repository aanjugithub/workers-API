from rest_framework import serializers

from workersapp.models import Employees

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields="__all__"
        read_only_fields=["id"]