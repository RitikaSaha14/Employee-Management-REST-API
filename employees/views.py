from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    CRUD endpoints for employee records.
    Supports list, retrieve, create, update, partial update, and delete.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
