from rest_framework import serializers
from .models import Department, Job, Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'



class EmployeeSerializer(serializers.ModelSerializer):
    # Hacer que acepte department_id y job_id directamente
    department_id = serializers.IntegerField(write_only=True)
    job_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'hire_date', 'department_id', 'job_id']  # Usar solo los campos requeridos

    def create(self, validated_data):
        # Crear el objeto Employee usando los IDs
        return Employee.objects.create(
            name=validated_data['name'],
            hire_date=validated_data['hire_date'],
            department_id=validated_data['department_id'],
            job_id=validated_data['job_id']
        )
