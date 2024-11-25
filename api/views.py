from django.shortcuts import render

# Create your views here.
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Department, Job, Employee
from .serializers import EmployeeSerializer
import logging


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

class BatchInsertView(APIView):
    def post(self, request):
        data = request.data

        # Log de los datos recibidos
        logger.debug(f"Batch insert called. Data received: {data}")

        # Validar si 'records' es una lista
        records = data.get('records')
        if not isinstance(records, list):
            logger.error("Records is not a list.")
            return Response({"error": "Records must be a list"}, status=status.HTTP_400_BAD_REQUEST)

        # Log de la longitud de registros
        logger.debug(f"Number of records received: {len(records)}")

        # Validar la longitud de 'records'
        if not 1 <= len(records) <= 1000:
            logger.warning(f"Invalid number of records: {len(records)}")
            return Response({"error": f"Provide a list of 1 to 1000 entries, got {len(records)}"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            serializer = EmployeeSerializer(data=records, many=True)
            if serializer.is_valid():
                serializer.save()
                logger.info(f"{len(records)} records inserted successfully.")
                return Response({"message": f"{len(records)} records inserted successfully."}, status=status.HTTP_201_CREATED)
            logger.error(f"Validation errors: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.exception("An error occurred during batch insert.")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
