from django.urls import path
from .views import UploadCSVView,UploadCSVNoHeaderView, BatchInsertView,DepartmentEmployeeCountView,EmployeesHiredByQuarterView,DepartmentsAboveAverageHiresView

urlpatterns = [
    path('upload-csv/', UploadCSVView.as_view(), name='upload_csv'),
    path('upload-csv-no-header/', UploadCSVNoHeaderView.as_view(), name='upload_csv_no_header'),
    path('batch-insert/', BatchInsertView.as_view(), name='batch_insert'),
    path('department-employee-count/', DepartmentEmployeeCountView.as_view(), name='department_employee_count'),
    path('employees-hired-by-quarter/', EmployeesHiredByQuarterView.as_view(), name='employees_hired_by_quarter'),
    path('departments-above-average-hires/', DepartmentsAboveAverageHiresView.as_view(), name='departments_above_average_hires'),

]
