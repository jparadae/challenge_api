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
    department_id = serializers.IntegerField(write_only=True)  # Usar el ID de la clave foránea
    job_id = serializers.IntegerField(write_only=True)  # Usar el ID de la clave foránea

    class Meta:
        model = Employee
        fields = ['id', 'name', 'hire_date', 'department_id', 'job_id']  # Campos esperados

    def create(self, validated_data):
        # Crear un objeto Employee con los IDs de las claves foráneas
        return Employee.objects.create(
            name=validated_data['name'],
            hire_date=validated_data['hire_date'],
            department_id=validated_data['department_id'],
            job_id=validated_data['job_id']
        )