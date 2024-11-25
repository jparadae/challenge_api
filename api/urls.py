from django.urls import path
from .views import UploadCSVView, BatchInsertView

urlpatterns = [
    path('upload-csv/', UploadCSVView.as_view(), name='upload_csv'),
    path('batch-insert/', BatchInsertView.as_view(), name='batch_insert'),
]
