from django.shortcuts import render

# Create your views here.
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Department, Job, Employee
from .serializers import EmployeeSerializer

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
        if not isinstance(data, list) or len(data) > 1000:
            return Response({"error": "Provide a list of up to 1000 entries"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = EmployeeSerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Batch insert successful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)