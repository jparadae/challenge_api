from django.urls import path
from .views import UploadCSVView,UploadCSVNoHeaderView, BatchInsertView

urlpatterns = [
    path('upload-csv/', UploadCSVView.as_view(), name='upload_csv'),
    path('upload-csv-no-header/', UploadCSVNoHeaderView.as_view(), name='upload_csv_no_header'),
    path('batch-insert/', BatchInsertView.as_view(), name='batch_insert'),
]
