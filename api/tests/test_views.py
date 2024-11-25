import pytest
from rest_framework.test import APIClient
from api.models import Department, Job, Employee

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def setup_data():
    sales = Department.objects.create(id=1, name="Sales")
    engineer = Job.objects.create(id=1, title="Engineer")
    Employee.objects.create(id=1, name="John Doe", hire_date="2021-01-15", department=sales, job=engineer)

@pytest.mark.django_db
def test_employees_hired_by_quarter(api_client, setup_data):
    response = api_client.get('/api/employees-hired-by-quarter/')
    assert response.status_code == 200
    assert isinstance(response.data, list)
    assert len(response.data) == 1
    assert response.data[0]['department_name'] == "Sales"
    assert response.data[0]['job_title'] == "Engineer"
    assert response.data[0]['quarter'] == 1
