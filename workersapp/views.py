from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from workersapp.serializers import EmployeesSerializer
from rest_framework import viewsets
from workersapp.models import Employees
from rest_framework import serializers


# Create your views here.


class EmployeesView(viewsets.ModelViewSet):

    serializer_class=EmployeesSerializer
    queryset=Employees.objects.all()      
