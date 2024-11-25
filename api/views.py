from django.shortcuts import render

# Create your views here.
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Department, Job, Employee
from .serializers import EmployeeSerializer
import logging
import sqlite3

logger = logging.getLogger(__name__)
class UploadCSVView(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            data = pd.read_csv(file)
            if 'employees' in file.name:
                for _, row in data.iterrows():
                    department, _ = Department.objects.get_or_create(name=row['department'])
                    job, _ = Job.objects.get_or_create(title=row['job'])
                    Employee.objects.create(
                        name=row['name'],
                        department=department,
                        job=job,
                        hire_date=row['hire_date']
                    )
            return Response({"message": "Data uploaded successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UploadCSVNoHeaderView(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        table_name = request.query_params.get('table')

        if not file or not table_name:
            return Response({"error": "File and table name are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Leer el archivo CSV sin encabezados
            df = pd.read_csv(file, header=None)

            # Asignar nombres de columnas según la tabla
            if table_name == "hired_employees":
                df.columns = ['id', 'name', 'hire_date', 'department_id', 'job_id']
            elif table_name == "departments":
                df.columns = ['id', 'name']
            elif table_name == "jobs":
                df.columns = ['id', 'title']
            else:
                return Response({"error": f"Unsupported table: {table_name}"}, status=status.HTTP_400_BAD_REQUEST)

            # Insertar en la base de datos
            conn = sqlite3.connect('database.db')
            df.to_sql(table_name, conn, if_exists='append', index=False)
            conn.close()

            return Response({"message": f"Data uploaded to {table_name} successfully."})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BatchInsertView(APIView):
    def post(self, request):
        data = request.data
        table = data.get('table')
        records = data.get('records')

        if not table or not records:
            return Response({"error": "Table and records are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Validar la tabla y manejar los datos correspondientes
            if table == "departments":
                for record in records:
                    Department.objects.create(id=record['id'], name=record['name'])
            elif table == "jobs":
                for record in records:
                    Job.objects.create(id=record['id'], title=record['title'])
            elif table == "hired_employees":
                for record in records:
                    Employee.objects.create(
                        id=record['id'],
                        name=record['name'],
                        hire_date=record['hire_date'],
                        department_id=record['department_id'],
                        job_id=record['job_id']
                    )
            else:
                return Response({"error": f"Unsupported table: {table}"}, status=status.HTTP_400_BAD_REQUEST)

            return Response({"message": f"Data inserted into {table} successfully."}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
